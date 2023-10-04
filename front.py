import ultralytics
ultralytics.checks()
from ultralytics import YOLO
model = YOLO("PAST_SEM/Data_Science/ADAS-Blind-Spot-Detection/runs/detect/train/weights/best.pt")
import cv2
from pygame import mixer

#Change 'fr' to change playback speed. Lower fr -> Greater playback speed
fr=50

# Open video file using OpenCV
video_path = "PAST_SEM/Data_Science/ADAS-Blind-Spot-Detection/SampleVideos/short_front.mp4" #EDIT INPUT FILE
cap = cv2.VideoCapture(video_path)
mixer.init()
mixer.music.load('PAST_SEM/Data_Science/ADAS-Blind-Spot-Detection/warning.mp3')

i=0

# Define alert function to display a message when "unsafe" is detected
def show_alert(i):
    print("ALERT{0}!!!INCOMING VEHICLE".format(int(i)))
    mixer.music.play()

# Loop over frames in the video
while cap.isOpened():
    # Read next frame from video
    ret, frame = cap.read()
    if not ret:
        break

    # Perform object detection inference on frame using the trained YOLOv8 model
    response = model.predict(source=frame, classes=[1], conf=0.8, show=True)
    
    if response[0].boxes.cls.shape[0] > 0:
        show_alert(i)
        i=i+1
    else:
        mixer.music.stop()
        
    cv2.waitKey(fr)
        
    if cv2.waitKey(fr) & 0xFF == ord('q'):
        break
    

# Release video capture and close window
cap.release()
cv2.destroyAllWindows()