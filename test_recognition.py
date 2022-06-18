import cv2
import time
import threading


def printit():
    threading.Timer(5.0, printit).start()
    print("hi")


cap = cv2.VideoCapture(0)

# Create the haar cascade
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

wait_to_display = 0
wait_to_display_initial_value = 0
initial_value_retrieved = False
initial_value = 0
value_changed_by_100 = 0
value_changed_by_50 = 0
value_changed_by_30 = 0


def reset_values():
    global value_changed_by_100
    value_changed_by_100 = 0
    global value_changed_by_50
    value_changed_by_50 = 0
    global value_changed_by_30
    value_changed_by_30 = 0
    print("values reset")


while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(50, 50)
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        wait_to_display = wait_to_display + 1
        wait_to_display_initial_value = wait_to_display_initial_value + 1
        if wait_to_display_initial_value == 50:
            initial_value = y + h
            initial_value_retrieved = True
            print("initial value is: ")
            print(initial_value)
            # reset wait_to_display to begin counting
            wait_to_display = 0

        if wait_to_display == 20 and initial_value_retrieved is True:
            if (y + h) - initial_value > 100:
                value_changed_by_100 = value_changed_by_100 + 1
                if value_changed_by_100 >= 4:
                    reset_values()
                    print("play alert here")
            if (y + h) - initial_value > 50:
                value_changed_by_50 = value_changed_by_50 + 1
                if value_changed_by_50 >= 6:
                    reset_values()
                    print("play alert here")
            if (y + h) - initial_value > 30:
                value_changed_by_30 = value_changed_by_30 + 1
                if value_changed_by_30 >= 9:
                    reset_values()
                    print("play alert here")
            # 10 ticks - 9 seconds
            wait_to_display = 0
    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
