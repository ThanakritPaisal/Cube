# Cube

Cube is a 3 dimentional texting platform which it's aim is to combine emotions with text. The emotion is captured from the webcam and the user's emotion will be determined by an Artificial Intelligence (AI) which will then be represented in the chat using emojis. This project is a university project made for grading in a class called "Cognitive Computing".

## How does it work?

### Overall

[![1682407723120](image/README/1682407723120.png)]()

*Figure 1: Block diagram of how the overall chat works*

The app works as seen in the flowchat. First, the sender sends message which will be stored on the Firebase's Real Time Database. Next, the thread on the reciever's side will detect change on the number of messages stored on the Firebase's message database and would retrieve the updated message as a dictionary. The message is then displayed and updates on the Tkinter. After the message is shown, the reciever's camera will turn on and the AI would record the emotion of the reader for a period of time. Then it would return the information on the current emotion and send it to Firebase. The sender's emotion thread would detect change on the message emotions and updates the emotion's emoji. This works in both ways as the reciever can be sender and the sender can also be reciever.

### GUI with Tkinter

Our decision to use Tkinter for this project is because we want to make this project 100% Python. Also all of our members are familiar with Tkinter since we worked with Tkinter for our last projects, therefore we can effeciently transfer our knowledge from our previous project to this project.

### Sending Message through Firebase

We decided to use Google's Firebase to store and retrieve our chat data since it's online and there are support for python. In addition, Firebase can not only store data and query, but also store pictures and host the application which we find very convenience and time saving.


### Emotion AI using YOLO

![1682599379411](image/README/1682599379411.png)

*Figure 2.1: Pattarapark's face emotion detection*

For our emotion AI, we decided to use YOLO ( You Only Look Once ) to detect our emotions. There are a total of 6 emotions that we can detect which is Happy, Sad, Neutral, Angry, Disguss and Surprised.

![1682599874381](image/README/1682599874381.png)

*Figure 2.2: Data collection block diagram*


When we want to detect our emotion, we need to first capture the user's emotions. We do this by detect frames using the user's camera. We make sure we got enough frames in order to process and detect emotions and store it into a CSV file. We make sure we get 150 frames in order to do the detection.

```
{"happy": 0, "sad": 0, "neutral": 0, "angry": 0, "disgust": 0, "surprise": 0}
```

*Figure 2.3: A dictionary of emotions and their value*

![1682600451586](image/README/1682600451586.png)

*Figure 2.4: Detection Process Flowchart*

Now you might be wondering at this point, how do we detect our actual emotions since we might be reading and that is not our actual emotion? We decided to solve this problem by record all the emotions detected for a period of time to a dictionary as shown in *Figure 2.3.* Then, we remove noise from the data and determine emotion spike from all the emotions to output the absolute emotion that the user is feeling using the Decision Tree. After the detection, it will return an emoji which is stored inside Firebase and updates the emotion emoji.

## Problems we encountered

## Required Libraries

- Firebase_admin
- Tkinter
- Pillow
- Customtkinter

## Collaborators

Chissanu Kittipakorn 64011728

Pattarapark Chutisamoot 64011532

Phanuruj Sotthidat 64011544

Puttipong Aunggulsant 64011595

Siraphop Mukdaphetcharat 64011614

Thanakrit Paisal 64011666
