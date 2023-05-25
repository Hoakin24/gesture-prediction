# Gesture Recognition with Mediapipe and sklearn

## Video Demo:  https://www.youtube.com/watch?v=N-3Bozo3OpU

## Description:
This repository contains code that utilizes Mediapipe and sklearn to predict gestures based on hand landmarks captured from a camera feed. The predicted gestures trigger corresponding outputs, allowing for gesture-based interaction with applications.

### Requirements
- opencv-python
- mediapipe
- keyboard
- pyautogui
- statistics
- scikit-learn
- pandas

Make sure to install these dependencies before running the code.

### Usage
1. Open the camera feed by running the code.
2. The code captures the hand landmarks using Mediapipe's pose estimation and displays them on the screen.
3. The hand landmarks are used to predict the gesture using a Random Forest classifier trained with sklearn.
4. Depending on the recognized gesture, the code sends keyboard commands using `pyautogui`.
   - Gesture "up" triggers the 'w' key.
   - Gesture "down" triggers the 's' key.
   - Gesture "left" triggers the 'a' key.
   - Gesture "right" triggers the 'd' key.
   - Gesture "stop" releases all pressed keys ('w', 'a', 's', 'd').

### Dataset Creation
The `dataset_creator.py` script captures video frames from the camera feed, detects hand landmarks using Mediapipe, and allows you to record hand landmarks for different gestures by pressing the corresponding keys. The recorded hand landmarks and corresponding gestures are saved in a CSV file named "dataset.csv."

Usage Tips:

- Run the `dataset_creator.py` script and follow the on-screen instructions to record hand landmarks for each gesture of interest.
- Make sure your hand is properly positioned within the camera's field of view for accurate hand landmark detection.
- Press the corresponding keys to record hand landmarks for different gestures.
- You can modify the script to add more gestures or customize the recording process according to your needs.

### Training
The Random Forest classifier is trained using the provided dataset. It splits the dataset into training and testing sets, and the model is trained on the training set. The accuracy of the model is computed using the testing set (not necessary for runtime prediction).

### Additional Notes
- The code continuously captures frames from the camera feed and performs gesture prediction.
- Make sure to position your hand within the camera's field of view for accurate hand landmark detection.

This will be passed as the Final Project for CS50x. 

I wanted to try if I can make in-game characters move with my hand and a camera, and I did!

Feel free to modify the code according to your requirements and dataset. Enjoy exploring gesture recognition with Mediapipe and sklearn!
