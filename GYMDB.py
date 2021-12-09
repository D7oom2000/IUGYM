from flask import *

import sqlite3
import sys
from sqlite3 import Error

import sqlite3

db_path = r"C:\Users\dhooo\PycharmProjects\GYMProjectFlask\GYMProject.db"

#
# def insert(form_inputs):
#     try:
#         conn = sqlite3.connect(db_path)
#         cur = conn.cursor()
#         name = form_inputs['name']
#         price = form_inputs['price']
#         query = 'insert into products (name, price) values (?,?)'
#         cur.execute(query, [name, float(price)])
#         conn.commit()
#     except Exception as ex:
#         return ex
#     return 'success!'


def check_login_coach(form_inputs):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    user_name = form_inputs['CNameLogin']
    password = form_inputs['CPassLogin']
    query = 'SELECT CPass FROM Coach WHERE CName =?'
    cur.execute(query, [user_name])
    result = cur.fetchall()
    if len(result) == 1:
        if result[0][0] == password:
            return True
        else:
            return False
    return False

def check_login_trainee(form_inputs):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    user_name = form_inputs['TNameLogin']
    password = form_inputs['TPassLogin']
    query = 'SELECT TPass FROM Trainee WHERE TName =?'
    cur.execute(query, [user_name])
    result = cur.fetchall()
    if len(result) == 1:
        if result[0][0] == password:
            return True
        else:
            return False
    return False

# def check_register_coach(form_inputs):
#
#     user_name = form_inputs['CNameReg']
#     password = form_inputs['CPassReg']
#     confpass = form_inputs['CConfPass']
#     cage = form_inputs['CAge']
#
#     if len(user_name) == 0 or len(password) == 0 or len(confpass) == 0 or len(cage) == 0:
#         flash("Please fill all fields!")
#     elif password != confpass:
#         flash("Passwords aren't match.")
#     elif int(cage) < 16:
#         flash("Illegal age")
#     else:
#         conn = sqlite3.connect("GYMProject.db")
#         cur = conn.cursor()
#
#         Coach_info = [user_name, password, cage]
#         cur.execute('INSERT INTO Coach (CName, CPass, CAge) VALUES (?,?,?)', Coach_info)
#         flash("Coach successfully added")
#         conn.commit()
#         conn.close()
#
#
#
#
# def check_register_trainee(form_inputs):
#
#     user_name = form_inputs['TNameReg']
#     password = form_inputs['TPassReg']
#     confpass = form_inputs['TConfPass']
#     tage = form_inputs['TAge']
#
#     if len(user_name) == 0 or len(password) == 0 or len(confpass) == 0 or len(tage) == 0:
#         flash("Please fill all fields!")
#     elif password != confpass:
#         flash("Passwords aren't match.")
#     elif int(tage) < 16:
#         flash("Illegal age")
#     else:
#         conn = sqlite3.connect("GYMProject.db")
#         cur = conn.cursor()
#
#         Trainee_info = [user_name, password, tage]
#         cur.execute('INSERT INTO Trainee (TName, TPass, TAge) VALUES (?,?,?)', Trainee_info)
#         flash("Trainee successfully added")
#         conn.commit()
#         conn.close()
#
#
#
def TraineeList():
    error = ""
    data = ""
    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("select * from Trainee")
        conn.commit()
        data = cur.fetchall()
    except Exception as ex:
        error = ex
    return error, data

def MachineList():
    error = ""
    data = ""
    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("select * from Machine")
        conn.commit()
        data = cur.fetchall()
    except Exception as ex:
        error = ex
    return error, data

#================================================================================

