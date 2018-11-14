import dlib
import cv2
from imutils import face_utils
import math
import timeit

pre = timeit.default_number
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
def face_dot_extract(image_name):
    start = timeit.default_timer()
    image = cv2.imread(image_name)
    width, height = image.shape[:2]

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    rects = detector(gray,1)
    for (i, rect) in enumerate(rects):
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
        minX = 1000
        minY = 1000
        maxX = 0
        maxY = 0

        center = (int((shape[8][0] + shape[27][0]) / 2), int((shape[8][1] + shape[27][1]) / 2))

        tan = (shape[8][1] - center[1])/(shape[8][0] - center[0])
        radian = math.atan(tan)*180/math.pi
        if radian > 0:
            radian = radian - 90
        elif radian < 0:
            radian = radian + 90
        print("radian : "+str(radian))
        new_image = cv2.imread("empty_image.jpg")
        new_image[:] = (255, 255, 255)

        for (x,y) in shape:
            cv2.circle(image,(x,y),1,(0,0,255),-1)
            trans_x = x - center[0]
            trans_y = y - center[1]
            shape[i][0] = math.cos(-math.radians(radian))*trans_x - math.sin(-math.radians(radian))*trans_y + center[0]
            shape[i][1] = math.sin(-math.radians(radian))*trans_x + math.cos(-math.radians(radian))*trans_y + center[1]
            if minX > shape[i][0]:
                minX = shape[i][0]
            if maxX < shape[i][0]:
                maxX = shape[i][0]
            if minY > shape[i][1]:
                minY = shape[i][1]
            if maxY < shape[i][1]:
                maxY = shape[i][1]
        ratio = 500 / (maxX - minX)
        print("maxX : "+str(maxX) +"minX :" + str(minX))
        print("maxY : "+str(maxY) + "minY : "+str(minY))
        print(shape)
        for(x,y)in shape:
            shape[i][0] = (x-minX)*ratio
            shape[i][1] = (y-minY)*ratio
            cv2.circle(new_image, ( (shape[i][0]), (shape[i][1])), 1, (0, 0, 0), -1)
            i = i+1
        #dot_image = np.full((maxX-minX,maxY-minY,3),0,dtype=np.int16)
        # dot_image's x size is 500
        print(shape)
        #cv2.imshow("dotimage",dot_image)
    stop = timeit.default_timer()
    print(stop - start)

    cv2.imshow("dots",new_image)
    return shape
# show the output image with the face detections + facial landmarks
# cv2.imshow("original",image)
# cv2.imshow("dots",new_image)
face_dot_extract("face.jpg")
cv2.waitKey(0)