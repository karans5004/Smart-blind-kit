
import face_recognition
import cv2
from gtts import gTTS 
import os
import threading
language = 'en'

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

wait = 0
def speak(name):
    wait = 1
    text = 'There is a Known person near you name is '+name
    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system("mpg321 welcome.mp3")
    wait = 0
video_capture = cv2.VideoCapture(0)

karan_image = face_recognition.load_image_file("karan.jpg")
karan_face_encoding = face_recognition.face_encodings(karan_image)[0]

anand_magar_sir = face_recognition.load_image_file("magar sir.jpg")
anand_magar_sir_face_encoding = face_recognition.face_encodings(anand_magar_sir)[0]


rajeshwari_image = face_recognition.load_image_file("rajeshwari.jpg")
rajeshwari_face_encoding = face_recognition.face_encodings(rajeshwari_image)[0]

shashwati_image = face_recognition.load_image_file("shashwati.jpg")
shashwati_face_encoding = face_recognition.face_encodings(shashwati_image)[0]


nikita_image = face_recognition.load_image_file("nikita.jpg")
nikita_face_encoding = face_recognition.face_encodings(nikita_image)[0]




srushti_image = face_recognition.load_image_file("srushti.jpg")
srushti_face_encoding = face_recognition.face_encodings(srushti_image)[0]


known_face_encodings = [
	karan_face_encoding,
	rajeshwari_face_encoding,
	shashwati_face_encoding,
	nikita_face_encoding,
	srushti_face_encoding,   	
]
known_face_names = [
	"Karan Shinde",
	"Anand Magar Sir"
	"Rajeshwari Bhirud ",
	"Shash ",
	"Nikita ",
	"Chiwda",
	
]

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
current_name = ''
name = ''
while True:
    ret, frame = video_capture.read()

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    rgb_small_frame = small_frame[:, :, ::-1]

    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
		
            face_names.append(name)
            
            

    process_this_frame = not process_this_frame


    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)

    if(current_name == name or name == 'Unknown'):
        flag = 0
    else:
        flag = 1
        current_name = name

    if(flag == 1):
        t1 = threading.Thread(target=speak, args=(name,))   
        while(wait == 1):
            continue
        t1.start()





    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()



