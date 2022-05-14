# install opencv-python , numpy , cmake , dlib , and face-regocnition
'''
import cv2
import face_recognition
import sys

def take_picture():
    print("Scanning Face:::")
    cam = cv2.VideoCapture(0)
    ret, frame = cam.Read()
    cv2.imwrite('Picture.jpg'   , frame)
    cv2.destroyAllWindows()
    cam.release()
    print("Face sce, comple .")


def analyse_user():
    print("Analyzin Face.....")
    baseimg = face_recognition.load_image_file("Me.jpg")
    baseimg = cv2.cvtColor(baseimg, cv2.COLOR_BGR2RGB)

    myface = face_recognition.face_locations(baseing)[0]
    encodemyface = face_recognition.face_encodings(baseimg)[0]
    cv2.rectangle(baseimg, (myface[3], myface[0]), (myface[1], myface[2]), (255,0,255), 2)



    sampleimg = face_recognition.load_image_file("Picture.jpg")
    sampleimg = cv2.cvtColor(sampleimg, cv2.COLOR_BGR2RGB)


analyse_user()
'''