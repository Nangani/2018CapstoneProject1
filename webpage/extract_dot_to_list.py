import cv2
import dlib
import sys
import math
from imutils import face_utils
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def face_dot_extract(image_name):
    
    image = cv2.imread(image_name)
    width, height = image.shape[:2]

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    rects = detector(gray,1)
    for (i, rect) in enumerate(rects):
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
        minX = 5000
        minY = 5000
        maxX = 0
        maxY = 0

        center = (int((shape[8][0] + shape[27][0]) / 2), int((shape[8][1] + shape[27][1]) / 2))

        tan = (shape[8][1] - center[1])/(shape[8][0] - center[0])
        radian = math.atan(tan)*180/math.pi
        if radian > 0:
            radian = radian - 90
        elif radian < 0:
            radian = radian + 90
        #print("radian : "+str(radian))
        new_image = cv2.imread("empty_image.jpg")
        new_image[:] = (255, 255, 255)
        i=0
        # cv2.circle(new_image, (int((shape[21][0]+shape[22][0])/2), int((shape[21][1]+shape[22][1])/2)), 1, (0, 0, 255), 1)
        # cv2.circle(new_image, (center[0], center[1]), 1, (0, 255, 0), 1)
        for (x,y) in shape:
            # cv2.circle(new_image,(x,y),1,(0,0,0),-4)
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
            i = i+1
        # cv2.circle(new_image, (shape[9][0], shape[9][1]), 1, (255, 0, 0), 1)

        
        ratio = 500 / (maxX - minX)
        #print("maxX : "+str(maxX) +"minX :" + str(minX))
        #print("maxY : "+str(maxY) + "minY : "+str(minY))
        i=0
        for(x,y)in shape:
            shape[i][0] = (x-minX)*ratio
            shape[i][1] = (y-minY)*ratio
            cv2.circle(new_image, ( (shape[i][0]), (shape[i][1])), 1, (0, 0, 0), -1)
            i = i+1
        #dot_image = np.full((maxX-minX,maxY-minY,3),0,dtype=np.int16)
        # dot_image's x size is 500
        dot_x = shape[8][0]
        dot_y = shape[8][1]
        i=0
        for(x,y)in shape:
            shape[i][0] = x - dot_x
            shape[i][1] = -(y-dot_y)
            i = i+1
        # cv2.imshow("dotimage",image)
        #print(shape)
    return shape.tolist()

if __name__== "__main__" :
    output = face_dot_extract(sys.argv[1])
    print(output)