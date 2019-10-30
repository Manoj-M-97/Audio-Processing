# Audio-Processing
This is a program the analyses an audio input to transform ot into a text form.

Libraries used:
1) Speech Recognition
2) Pydub
3) contextlib
4) math

To install:
1) pip install SpeechRecognition
2) pip install Pydub
3) //If when you run the code, if there is a warning from Pydub library for the package ffmpeg, install it.

pip install ffmpeg

To run:
python audio_processing.py
//Using python 3.6

Input:
The input audio file('test.wav') name should be initialised in the program (Path should be given).
If you dont change the input file, you dont need to make any changes.

Assumptions:
A silence is considered a pause of 2 seconds
