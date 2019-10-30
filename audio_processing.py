# importing libraries 
import speech_recognition as sr 
import wave
import contextlib
import math
from pydub.silence import split_on_silence
from pydub import AudioSegment

# Path of the input audio file 
audio_fname = 'test.wav'
# The duration of the audio 
duration = 0

# Calculating the duration of the audio input
with contextlib.closing(wave.open(audio_fname,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    if rate > 0:
	    duration = frames / float(rate)

# Create an object of the recogniser class
rcgnzr = sr.Recognizer()

# Reading the audio input
audio_input = sr.AudioFile(audio_fname)

# Records the audio from source into an AudioData instance
with audio_input as source:
	audio = rcgnzr.record(source)
	print("The audio file",audio_fname,"has been read\n")

sound = AudioSegment.from_wav(audio_fname)

chunks = split_on_silence(
	# Use the loaded audio.
	sound, 
	# Specify that a silent chunk must be at least 2 s or 2000 ms long.
	min_silence_len = 2000,
	# Consider a chunk silent if it's quieter than -16 dBFS.
	silence_thresh = sound.dBFS 
)
# Outputs the number of silences in the audio file.
print("The number of silences in the audio file is : ",len(chunks))
print()

try:
	# Recognize the text using google api
	recognized_txt = rcgnzr.recognize_google(audio)
	print("Below is the text from the audio:")
	print(recognized_txt)
	print()

	# Calculate the number of words spoken in the audio
	word_list = recognized_txt.split(' ')
	word_count = len(word_list)

	# If the duration of the audio is greater than 0s, calculate the speed of words spoken per minute.
	if duration > 0:
		speed = word_count / (duration/60)
		print("The speed in words per minute of the audio is : ",end ='')
		print(math.floor(speed))
		print()

	word_freq = {}
	# Calulate the word frequency
	for word in word_list:
		if word in word_freq.keys():
			word_freq[word] += 1
		else:
			word_freq[word] = 1

	# Output the word frequency 
	print("The word frequency of the spoken words are as below:")
	for word in word_freq.keys():
		print(word, ' : ',word_freq[word])

except Exception as e:
	print("Exception",e)