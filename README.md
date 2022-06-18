# posture-corrector
Detects bad posture based on where your face is located on your webcam using [OpenCV](#https://opencv.org/)

When the program boots up, it will assume you are in an upright posture and take the position of your face as an initial value.

If this value changes by too much, a sound alert will be played.

To run, make sure python is installed with opencv, keyboard and the 1.2.2 playsound dependencies and run

`python posture_correctory.py`

To stop posture tracking, hit the tilda (`) key or ctrl c out of program

To change the error sound replace error_sound.wav with a new file with the same name or change line 32 to point to a new file.


# TODO
Add simple GUI



