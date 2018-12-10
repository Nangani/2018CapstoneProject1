import cv2
import face_dot_extract
import time

def calculate_distance_point_to_point(saved_image_dot,compare_image_dot):
    x = saved_image_dot[0] - compare_image_dot[0]
    y = saved_image_dot[1] - compare_image_dot[1]
    return (x*x)+(y*y)
def calculate_distance(save_face_image,decteded_face):
    value = 0
    i=0
    for face in save_face_image:
        value = value + calculate_distance_point_to_point(save_face_image[i],decteded_face[i])
        i= i+1
    return value
def calculate_face(image_DB,face):
    start_time = time.time()
    calculated_value = 999999999999
    index = 0
    i=0
    for (image_name,image_shape) in image_DB:
        distance = calculate_distance(image_shape,face)
        # print(distance)
        if calculated_value > distance :
            calculated_value = distance
            index = i
        i = i+1
    print("this face is :" + str(image_DB[index][0]))
    endtime = time.time()
    print("calculate process time : " + str(endtime - start_time))
    if calculated_value > 50000:
        return None
    else:
        return image_DB[index][0]

