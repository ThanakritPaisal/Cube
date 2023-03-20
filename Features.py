import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime

class Features:
    def __init__(self):
        # Fetch the service account key JSON file contents
        cred = credentials.Certificate("db_key.json")

        # Initialize the app with a service account, granting admin privileges
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://cube-bc9c8-default-rtdb.asia-southeast1.firebasedatabase.app/'
        })

        self.ref = db.reference('/')

    """
    This function will add friend based from friend ID
    INPUT: CurrentUserID, FriendUserID
    OUTPUT: Error if exists
    """
    def addFriend(self, curr, username):
        # Safe Guard to prevent add themselves
        if curr == username:
            return "You can't add yourself!"
        
        # Set pointer to users
        users_ref = self.ref.child('users')
        
        # Set Reference to current user
        currUserRef = self.ref.child('users').child(curr)

        # Query current user data
        currUser = currUserRef.get()
        
        # Query all users
        users = users_ref.get()

        currUserPending = currUser['pending']
        if type(currUserPending) is not list:
            currUserPending = []
            currUserPending.append(currUser['pending'])
        
        #Update database to show sending request on current user and incoming on receiver
        try:
            for user in users.keys():
                if user == username:
                    if username not in currUserPending:
                        currUserPending.append(username)
                    currUserRef.update({
                        'pending' : currUserPending
                    })
                    incomingUser = self.ref.child('users').child(username)
                    incomingUser.update({
                        'incoming' : curr
                    })
                    return "Success"
            return "No user with that ID"
        except Exception as e:
            print(e)
    
    def rejectFriendRequest(self):
        pass