import pre_execute
import updataDB_Student
import face_dot_extract
import download_from_server
import dlib
import pymysql
import time
import os
import tkinter
import sys

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

conn = pymysql.connect(host = 'localhost',user='root',password='rlaehgud1!',db='attendance')
curs = conn.cursor()



def checkAttendacne(lecture):
    print("start process")
    start_time = time.time()

    lecture_id, student_DB = updataDB_Student.road_student_info(conn,lecture)

    picture_list= download_from_server.load_image()
    for picture in picture_list:
        print(picture)
        student_dot = face_dot_extract.face_dot_extract(picture,detector,predictor)
        result = pre_execute.calculate_face(student_DB,student_dot)

        if result!=None:
            if picture[0]=="_":
                sql = "update list_students set attendance = 0 where student_id = "+str(result)+" AND lecture_id = "+str(lecture_id)+";"
                print(str(result)+"is absence")
                curs.execute(sql)
                conn.commit()
            else :
                sql = "update list_students set attendance = 1 where student_id = " + str(result) + " AND lecture_id = " + str(lecture_id) + ";"
                print(str(result)+'is attendance')
                curs.execute(sql)
                conn.commit()
        print("end one picture\n")
        os.remove(picture)
    print("end process")
    endtime = time.time()
    print("all process : " + str(endtime - start_time))


if __name__=="__main__" :
    while 1:
        checkAttendacne(sys.argv[1])
        print("")
        time.sleep(30)