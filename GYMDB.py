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


def CreateTraineeAcc(form_inputs):
 try:
    user_name = form_inputs['TNameReg']
    password = form_inputs['TPassReg']
    confpass = form_inputs['TPassConf']
    tage = form_inputs['TAge']

    if password != confpass:
        return False
    elif int(tage) < 16:
        return False
    else:

        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        Coach_info = [user_name, password, tage]
        query = 'INSERT INTO Trainee (TName, TPass, TAge) VALUES (?,?,?)'
        cur.execute(query, [Coach_info])
        conn.commit()
 except Exception as ex:
     return ex
     return 'success!'

def TraineeList():
    error = ""
    data = ""
    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("select TID,TName,TAge,Sub_Status,Balance from Trainee")
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

def StoreList():
    error = ""
    data = ""
    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("select * from Store")
        conn.commit()
        data = cur.fetchall()
    except Exception as ex:
        error = ex
    return error, data


#================================================================================

