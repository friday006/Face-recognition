import cv2
import face_recognition
import time


# Load the cascade  
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def process_img(img_rgb, template, name, count):
    rgb_img = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)
    try:
        img_encoding = face_recognition.face_encodings(rgb_img)[0]
        rgb_img2 = cv2.cvtColor(template, cv2.COLOR_BGR2RGB)
        img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]

        result = face_recognition.compare_faces([img_encoding], img_encoding2)
        print(f"Detected ... {name}:", result)
        
        
        try:
            cv2.imshow('Detected', img_rgb)
        except:
            pass 

    except IndexError as e:
        print(f"Detecting {name} ...") 

    

def main():
    vidcap = cv2.VideoCapture('My_video.mp4')
    template = cv2.imread("download2.jpeg")
    name = input("Enter the name of person to find in video: \n")
    count =0
    pTime =0
    while True:
        # Read the frame  
        success, img = vidcap.read()
        if not success:
            print("not working")
            break
        print("Read a new frame: ",success)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS: {int(fps)}',(20,70), cv2.FONT_HERSHEY_PLAIN,3, (0,255,0), 2)

        # Convert to grayscale  
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
        # Detect the faces  
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)  
  
        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2) 
        process_img(img, template, name, count)
        count +=1
        
        cv2.imshow('Review_Video', img)  

        k =cv2.waitKey(1) & 0xff
        if k == 27:
            break

    vidcap.release()
main()

