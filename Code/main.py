import cv2
import face_recognition
#import SimpleFaceRec
import simple_facerec

from simple_facerec import SimpleFacerec


#import faces from my folder


sfr = SimpleFacerec()

sfr.load_encoding_images("images/")


#load camera
cap=cv2.VideoCapture(0)




while True:
    ret,frame=cap.read()
#detect faces
    face_locations,face_names= sfr.detect_known_faces(frame)
    for face_loc ,name in zip(face_locations,face_names):
        top,left,bottom,right=face_loc[0], face_loc[1], face_loc[2], face_loc[3]
       # print(face_loc)
       # cv2.putText(frame,name(x1,y1-10),cv2.FONT_HERSHEY_DUPLEX, 1,(0, 0, 0), 2)
        #cv2.rectangle(frame,(x1, y1),(x2, y2),(0,0,200),4)

        cv2.putText(frame,name,(left,top-10),cv2.FONT_HERSHEY_DUPLEX, 1,(0, 0, 0), 2)
        cv2.rectangle(frame,(left, top),(right, bottom),(0,0,200),4)
    cv2.imshow("Frame",frame)
    key=cv2.waitKey(1)
    if key==27:
        break
    cap.release
    cv2.destroyAllWindows()
