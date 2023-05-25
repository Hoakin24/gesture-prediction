# Import libraries
import pyautogui
import cv2
import mediapipe as mp
from mediapipe import solutions
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd

# Open the camera
cap = cv2.VideoCapture(0)

# Initialize Mediapipe hands and drawing utilities
mpHands = solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

# Load the dataset
d = pd.read_csv("dataset.csv", sep=',')

# Prepare the data for training
X = d.drop('gesture', axis=1)
Y = d['gesture']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=3)

# Train the Random Forest model
model = RandomForestClassifier()
model.fit(X_train, Y_train)

# These two lines are only used to measure the accuracy (not needed)
# X_test_prediction = model.predict(X_test)
# test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

# Perform predictions
def predict(hand_landmarks):
    center_x = (hand_landmarks.landmark[0].x + hand_landmarks.landmark[5].x + hand_landmarks.landmark[17].x)/3
    center_y = (hand_landmarks.landmark[0].y + hand_landmarks.landmark[5].y + hand_landmarks.landmark[17].y)/3

    thumb_tip_x = center_x - hand_landmarks.landmark[mpHands.HandLandmark.THUMB_TIP].x
    thumb_tip_y = center_y - hand_landmarks.landmark[mpHands.HandLandmark.THUMB_TIP].y
    thumb_ip_x = center_x - hand_landmarks.landmark[mpHands.HandLandmark.THUMB_IP].x
    thumb_ip_y = center_y - hand_landmarks.landmark[mpHands.HandLandmark.THUMB_IP].y
    thumb_mcp_x = center_x - hand_landmarks.landmark[mpHands.HandLandmark.THUMB_MCP].x
    thumb_mcp_y = center_y - hand_landmarks.landmark[mpHands.HandLandmark.THUMB_MCP].y
    thumb_cmc_x = center_x - hand_landmarks.landmark[mpHands.HandLandmark.THUMB_CMC].x
    thumb_cmc_y = center_y - hand_landmarks.landmark[mpHands.HandLandmark.THUMB_CMC].y

    index_tip_x = center_x - hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP].x
    index_tip_y = center_y - hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP].y
    index_dip_x = center_x - hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_DIP].x
    index_dip_y = center_y - hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_DIP].y
    index_pip_x = center_x - hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_PIP].x
    index_pip_y = center_y - hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_PIP].y
    index_mcp_x = center_x - hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_MCP].x
    index_mcp_y = center_y - hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_MCP].y
    
    middle_tip_x = center_x - hand_landmarks.landmark[mpHands.HandLandmark.MIDDLE_FINGER_TIP].x
    middle_tip_y = center_y - hand_landmarks.landmark[mpHands.HandLandmark.MIDDLE_FINGER_TIP].y
    middle_dip_x = center_x - hand_landmarks.landmark[mpHands.HandLandmark.MIDDLE_FINGER_DIP].x
    middle_dip_y = center_y - hand_landmarks.landmark[mpHands.HandLandmark.MIDDLE_FINGER_DIP].y
    middle_pip_x = center_x - hand_landmarks.landmark[mpHands.HandLandmark.MIDDLE_FINGER_PIP].x
    middle_pip_y = center_y - hand_landmarks.landmark[mpHands.HandLandmark.MIDDLE_FINGER_PIP].y
    middle_mcp_x = center_x - hand_landmarks.landmark[mpHands.HandLandmark.MIDDLE_FINGER_MCP].x
    middle_mcp_y = center_y - hand_landmarks.landmark[mpHands.HandLandmark.MIDDLE_FINGER_MCP].y
    
    ring_tip_x = center_x - hand_landmarks.landmark[mpHands.HandLandmark.RING_FINGER_TIP].x
    ring_tip_y = center_y - hand_landmarks.landmark[mpHands.HandLandmark.RING_FINGER_TIP].y
    ring_dip_x = center_x - hand_landmarks.landmark[mpHands.HandLandmark.RING_FINGER_DIP].x
    ring_dip_y = center_y - hand_landmarks.landmark[mpHands.HandLandmark.RING_FINGER_DIP].y
    ring_pip_x = center_x - hand_landmarks.landmark[mpHands.HandLandmark.RING_FINGER_PIP].x
    ring_pip_y = center_y - hand_landmarks.landmark[mpHands.HandLandmark.RING_FINGER_PIP].y
    ring_mcp_x = center_x - hand_landmarks.landmark[mpHands.HandLandmark.RING_FINGER_MCP].x
    ring_mcp_y = center_y - hand_landmarks.landmark[mpHands.HandLandmark.RING_FINGER_MCP].y
    
    pinky_tip_x = center_x - hand_landmarks.landmark[mpHands.HandLandmark.PINKY_TIP].x
    pinky_tip_y = center_y - hand_landmarks.landmark[mpHands.HandLandmark.PINKY_TIP].y
    pinky_dip_x = center_x - hand_landmarks.landmark[mpHands.HandLandmark.PINKY_DIP].x
    pinky_dip_y = center_y - hand_landmarks.landmark[mpHands.HandLandmark.PINKY_DIP].y
    pinky_pip_x = center_x - hand_landmarks.landmark[mpHands.HandLandmark.PINKY_PIP].x
    pinky_pip_y = center_y - hand_landmarks.landmark[mpHands.HandLandmark.PINKY_PIP].y
    pinky_mcp_x = center_x - hand_landmarks.landmark[mpHands.HandLandmark.PINKY_MCP].x
    pinky_mcp_y = center_y - hand_landmarks.landmark[mpHands.HandLandmark.PINKY_MCP].y

    df = pd.DataFrame([[thumb_tip_x, thumb_tip_y, thumb_ip_x, thumb_ip_y, thumb_mcp_x, thumb_mcp_y, thumb_cmc_x, thumb_cmc_y, index_tip_x, index_tip_y, index_dip_x, index_dip_y, index_pip_x, index_pip_y, index_mcp_x, index_mcp_y, middle_tip_x, middle_tip_y, middle_dip_x, middle_dip_y, middle_pip_x, middle_pip_y, middle_mcp_x, middle_mcp_y, ring_tip_x, ring_tip_y, ring_dip_x, ring_dip_y, ring_pip_x, ring_pip_y, ring_mcp_x, ring_mcp_y, pinky_tip_x, pinky_tip_y, pinky_dip_x, pinky_dip_y, pinky_pip_x, pinky_pip_y, pinky_mcp_x, pinky_mcp_y]], columns=['thumb_tip_x', 'thumb_tip_y', 'thumb_ip_x', 'thumb_ip_y', 'thumb_mcp_x', 'thumb_mcp_y', 'thumb_cmc_x', 'thumb_cmc_y', 'index_tip_x', 'index_tip_y', 'index_dip_x', 'index_dip_y', 'index_pip_x', 'index_pip_y', 'index_mcp_x', 'index_mcp_y', 'middle_tip_x', 'middle_tip_y', 'middle_dip_x', 'middle_dip_y', 'middle_pip_x', 'middle_pip_y', 'middle_mcp_x', 'middle_mcp_y', 'ring_tip_x', 'ring_tip_y', 'ring_dip_x', 'ring_dip_y', 'ring_pip_x', 'ring_pip_y', 'ring_mcp_x', 'ring_mcp_y', 'pinky_tip_x', 'pinky_tip_y', 'pinky_dip_x', 'pinky_dip_y', 'pinky_pip_x', 'pinky_pip_y', 'pinky_mcp_x', 'pinky_mcp_y'])
    return model.predict(df)

# Main loop
while True:
    # Read frame from the camera
    success, image = cap.read()
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(imageRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks: # working with each hand
            for id, lm in enumerate(handLms.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 20 :
                    cv2.circle(image, (cx, cy), 25, (255, 0, 255), cv2.FILLED)

            mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Output", image)
    cv2.waitKey(1)

    if not results.multi_hand_world_landmarks:
        continue

    for hand_landmarks in results.multi_hand_landmarks:
        gesture = predict(hand_landmarks)[0]
        if gesture == "up":
            pyautogui.keyDown('w')
        elif gesture == "down":
            pyautogui.keyDown('s')
        elif gesture == "left":
            pyautogui.keyDown('a')
        elif gesture == "right":
            pyautogui.keyDown('d')
        elif gesture == "stop":
            pyautogui.keyUp('w')
            pyautogui.keyUp('a')
            pyautogui.keyUp('s')
            pyautogui.keyUp('d')
