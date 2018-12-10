import sys
import pymysql
import numpy as np
import time

def road_student_info(conn,subject):
    start_time = time.time()
    curs1 = conn.cursor()
    sql1 = "select lecture_id from lecture where lecture_name = '"+subject+"';"
    curs1.execute(sql1)
    subject_id = curs1.fetchall()
    curs2 = conn.cursor()
    sql2 = "select id,face_detection_dot from student where id in (select student_id from list_students where lecture_id = " + str(subject_id[0][0])+");"
    curs2.execute(sql2)
    result = []
    rows = curs2.fetchall()
    # print(rows)
    i=0
    #학생
    for student_String in rows:
        student = []
        student.append(student_String[0])

        student_partion = student_String[1].split("], [")
        student_dot = []
        location = []
        location_partion = student_partion[0][2:].split(", ")
        location.append(int(location_partion[0]))
        location.append(int(location_partion[1]))
        student_dot.append(location)

        #학생 얼굴 점의 좌표
        for dotLocation in student_partion[1:-1]:
            location = []
            location_partion = dotLocation.split(", ")
            location.append(int(location_partion[0]))
            location.append(int(location_partion[1]))
            student_dot.append(location)


        location = []
        location_partion = student_partion[-1].split(", ")
        location.append(int(location_partion[0]))
        location.append(int(location_partion[1][:-2]))
        student_dot.append(location)

        student.append(student_dot)
        result.append(student)
    endtime = time.time()
    print("DB process time: " + str(endtime - start_time))
    return subject_id[0][0], result
