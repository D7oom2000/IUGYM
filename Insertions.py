import sqlite3
from sqlite3 import *


# ----- Just for insert exiting data! -----

# Make connection to database in SQLite
def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def create_Coach(conn,Coach):
    sql = " INSERT INTO Coach(CName,CPass,CAge) VALUES(?,?,?)"
    cur = conn.cursor()
    cur.execute(sql, Coach)
    conn.commit()
    return cur.lastrowid

def create_Machine(conn,Machine):
    sql = " INSERT INTO Machine(MName,MStatus) VALUES(?,?)"
    cur = conn.cursor()
    cur.execute(sql, Machine)
    conn.commit()
    return cur.lastrowid

def create_Trainee(conn,Trainee):
    sql = " INSERT INTO Trainee(TName,TPass,TAge,Sub_Status) VALUES(?,?,?,?)"
    cur = conn.cursor()
    cur.execute(sql,Trainee)
    conn.commit()
    return cur.lastrowid

# main method conatins the direction of DB file and data insertion

def DBmain():
    database = r"C:\Users\dhooo\Desktop\Special for Laptop\Books And Solution\about the university\Third Year of The Specialize\Advanced Programming\Project\GYMProject-Final Project\GYMProject.db"

    conn = create_connection(database)
    with conn:
        Coach_1 = ('Talal', '123', '22')
        Coach_2 = ('Abdo', '1234', '21')
        Coach_3 = ('Sultan', '12345', '20')
        Coach_4 = ('Ali', '123456', '24')
        Coach_5 = ('Moayad', '123457', '18')


        create_Coach(conn,Coach_1)
        create_Coach(conn,Coach_2)
        create_Coach(conn,Coach_3)
        create_Coach(conn,Coach_4)
        create_Coach(conn,Coach_5)

        Machine_1 = ('Bunch Press 1', 'Availble')
        Machine_2 = ('Bunch Press 2', 'Availble')
        Machine_3 = ('Bunch Press 3', 'Busy')
        Machine_4 = ('Bunch Press 4', 'Availble')
        Machine_5 = ('Bunch Press 5', 'Busy')
        Machine_6 = ('Smith 1', 'Availble')
        Machine_7 = ('Smith 2', 'Busy')
        Machine_8 = ('Smith 3', 'Availble')
        Machine_9 = ('Smith 4', 'Busy')
        Machine_10 = ('Smith 5', 'Availble')
        Machine_11 = ('Barbell 1', 'Busy')
        Machine_12 = ('Barbell 2', 'Availble')
        Machine_13 = ('Barbell 3', 'Busy')
        Machine_14 = ('Barbell 4', 'Availble')
        Machine_15 = ('Barbell 5', 'Availble')


        create_Machine(conn,Machine_1)
        create_Machine(conn,Machine_2)
        create_Machine(conn,Machine_3)
        create_Machine(conn,Machine_4)
        create_Machine(conn,Machine_5)
        create_Machine(conn,Machine_6)
        create_Machine(conn,Machine_7)
        create_Machine(conn,Machine_8)
        create_Machine(conn,Machine_9)
        create_Machine(conn,Machine_10)
        create_Machine(conn,Machine_11)
        create_Machine(conn,Machine_12)
        create_Machine(conn,Machine_13)
        create_Machine(conn,Machine_14)
        create_Machine(conn,Machine_15)


        Trainee_1 = ('Omar', '123', '23', 'Valid')
        Trainee_2 = ('Ahmed', '123', '28', 'Valid')
        Trainee_3 = ('Abdo', '123', '23', 'Valid')
        Trainee_4 = ('Hamed', '1234', '30', 'Valid')
        Trainee_5 = ('Mohamed', '1234', '24', 'Valid')
        Trainee_6 = ('Suad', '1234', '42', 'Valid')
        Trainee_7 = ('Saleh', '12345', '34', 'Valid')
        Trainee_8 = ('Mazen', '12345', '48', 'Valid')
        Trainee_9 = ('Ryan', '12345', '36', 'Valid')
        Trainee_10 = ('Khaled', '123456', '23', 'Valid')
        Trainee_11 = ('Ibrahim', '123456', '19', 'Valid')
        Trainee_12 = ('Fahad', '123456', '32', 'Valid')
        Trainee_13 = ('Faisal', '1234567', '33', 'Valid')
        Trainee_14 = ('Faris', '1234567', '28', 'Valid')
        Trainee_15 = ('Badr', '1234567', '29', 'Valid')
        Trainee_16 = ('Bandar', '12345678', '34', 'Valid')
        Trainee_17 = ('Yassir', '12345678', '47', 'Valid')
        Trainee_18 = ('Yousef', '12345678', '17', 'Valid')
        Trainee_19 = ('Naif', '123456789', '26', 'Valid')
        Trainee_20 = ('Bassam', '123456789', '25', 'Valid')

        create_Trainee(conn,Trainee_1)
        create_Trainee(conn,Trainee_2)
        create_Trainee(conn,Trainee_3)
        create_Trainee(conn,Trainee_4)
        create_Trainee(conn,Trainee_5)
        create_Trainee(conn,Trainee_6)
        create_Trainee(conn,Trainee_7)
        create_Trainee(conn,Trainee_8)
        create_Trainee(conn,Trainee_9)
        create_Trainee(conn,Trainee_10)
        create_Trainee(conn,Trainee_11)
        create_Trainee(conn,Trainee_12)
        create_Trainee(conn,Trainee_13)
        create_Trainee(conn,Trainee_14)
        create_Trainee(conn,Trainee_15)
        create_Trainee(conn,Trainee_16)
        create_Trainee(conn,Trainee_17)
        create_Trainee(conn,Trainee_18)
        create_Trainee(conn,Trainee_19)
        create_Trainee(conn,Trainee_20)


# if __name__ == '__main__':
#    DBmain()

