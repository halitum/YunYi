from fastapi import APIRouter, HTTPException
from models import Student
import pymysql
from database import get_db_connection
from typing import List

router = APIRouter()

# 获取所有学生信息
@router.get("/students/", response_model=List[Student], tags=["Students"])
def read_students():
    conn = get_db_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return students

# 获取单个学生信息
@router.get("/students/{student_account}", response_model=Student, tags=["Students"])
def read_student(student_account: int):
    conn = get_db_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM students WHERE account = %s", (student_account,))
    student = cursor.fetchone()
    cursor.close()
    conn.close()
    if student is None:  # 如果未找到学生，返回404错误
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# 向数据库插入学生账号
@router.post("/students/", tags=["Students"])
def Insert_student(student: Student):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO students (name, age, position, awards, account, pwd, department, periodNum) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                    (student.name, student.age, student.position, student.awards, student.account, student.pwd, student.department, student.periodNum))
    except pymysql.MySQLError as e:
        raise HTTPException(status_code=500, detail="Input information format error.")
    cursor.close()
    conn.close()
    return {"message": "Student added successfully"}

# 更新学生信息
@router.put("/students/{student_account}", tags=["Students"])
def update_student(student_account: int, student: Student):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET name = %s, age = %s, position = %s, awards = %s, pwd = %s, department = %s, periodNum = %s WHERE account = %s",
                   (student.name, student.age, student.position, student.awards, student.pwd, student.department, student.periodNum, student_account))
    updated = cursor.rowcount
    cursor.close()
    conn.close()
    if updated == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student updated successfully"}

# 删除学生信息
@router.delete("/students/{student_account}", tags=["Students"])
def delete_student(student_account: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE account = %s", (student_account,))
    deleted = cursor.rowcount
    cursor.close()
    conn.close()
    if deleted == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}