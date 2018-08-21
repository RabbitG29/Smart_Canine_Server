import speech_recognition as sr

sample_rate = 48000
chunk_size = 2048
 
# Record Audio
r = sr.Recognizer()
with sr.Microphone(device_index=2, sample_rate = sample_rate, chunk_size = chunk_size) as source:
    print("Say something!")
    audio = r.listen(source)
	 
# Speech recognition using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
	    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
	    # instead of `r.recognize_google(audio)`
    print("You said: " + r.recognize_google(audio, language='ko-KR'))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
