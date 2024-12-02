from ultralytics import YOLO
import cv2




model = YOLO('yolov8n.pt')

video_path = 'cars.mp4'
cap = cv2.VideoCapture(video_path)

isTrue = True

# read frames

while isTrue:
    isTrue , frame = cap.read()

    # detect and track objects

    results = model.track(frame, persist=True)

    # plot results

    frame1 = results[0].plot()

    # visualize

    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)  # Create a resizable window
    cv2.resizeWindow('frame', 1380, 760)  # Set the window size to 800x600

    cv2.imshow('frame', frame1)  # Display the frame

    if cv2.waitKey(25) & 0xFF == ord('q'):  # Break the loop when 'q' is pressed
        break






