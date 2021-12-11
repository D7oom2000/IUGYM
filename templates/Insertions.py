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
#
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
    sql = " INSERT INTO Trainee(TName,TPass,TAge,Sub_Status, Balance) VALUES(?,?,?,?,?)"
    cur = conn.cursor()
    cur.execute(sql,Trainee)
    conn.commit()
    return cur.lastrowid

def create_Store(conn,Store):
    sql = " INSERT INTO Store(ItemName,ItemPrice,ItemQuantity, ItemDescription) VALUES(?,?,?,?)"
    cur = conn.cursor()
    cur.execute(sql,Store)
    conn.commit()
    return cur.lastrowid

# main method conatins the direction of DB file and data insertion

def DBmain():
    database = r"C:\Users\dhooo\PycharmProjects\GYMProjectFlask\GYMProject.db"

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


        Trainee_1 = ('Omar', '123', '23', 'Valid', '15000')
        Trainee_2 = ('Ahmed', '123', '28', 'Valid', '12000')
        Trainee_3 = ('Abdo', '123', '23', 'Valid', '10000')
        Trainee_4 = ('Hamed', '1234', '30', 'Valid', '5000')
        Trainee_5 = ('Mohamed', '1234', '24', 'Valid', '4000')
        Trainee_6 = ('Suad', '1234', '42', 'Valid', '6000')
        Trainee_7 = ('Saleh', '12345', '34', 'Valid', '2000')
        Trainee_8 = ('Mazen', '12345', '48', 'Valid', '1200')
        Trainee_9 = ('Ryan', '12345', '36', 'Valid', '1000')
        Trainee_10 = ('Khaled', '123456', '23', 'Valid', '1800')
        Trainee_11 = ('Ibrahim', '123456', '19', 'Valid', '2700')
        Trainee_12 = ('Fahad', '123456', '32', 'Valid', '9000')
        Trainee_13 = ('Faisal', '1234567', '33', 'Valid', '10000')
        Trainee_14 = ('Faris', '1234567', '28', 'Valid', '2500')
        Trainee_15 = ('Badr', '1234567', '29', 'Valid', '5500')
        Trainee_16 = ('Bandar', '12345678', '34', 'Valid', '3000')
        Trainee_17 = ('Yassir', '12345678', '47', 'Valid', '3100')
        Trainee_18 = ('Yousef', '12345678', '17', 'Valid', '9000')
        Trainee_19 = ('Naif', '123456789', '26', 'Valid', '16000')
        Trainee_20 = ('Bassam', '123456789', '25', 'Valid', '10000')

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

        Store_1 = ('Muscletech', '150', '50', 'Premium 100% Whey Protein Plus 5 Lb')
        Store_2 = ('LAPERVA ISO', '200', '10', 'Protein powder with 28g protein per 30g serving')
        Store_3 = ('LAPERVA Sports Bar', '20', '30', 'Premium Sugar-free Belgian chocolate bar')
        Store_4 = ('WOWTEIN', '190', '20', 'The package contains 80 portions')
        Store_5 = ('Laperva Keto Cola', '7', '40', 'Refreshing keto cola soft drink')
        Store_6 = ('Protein Shaker Max – Onyx', '70', '20', 'Optimal Workout Accessories')
        Store_7 = ('PACK OF 5 – SQUATWOLF MINI POWER BANDS', '40', '10', 'Power Bands is a set of 5 bands')
        Store_8 = ('LAB360º Headband – Dark Gull Grey', '60', '15', 'The LAB360º headband is engineered with a double-layer construction')
        Store_9 = ('HALF GALLON BOTTLE – KHAKI', '105', '6', 'Always stay hydrated with the Half Gallon Bottle. ')
        Store_10 = ('SQUATWOLF SKIPPING ROPE – SILVER', '95', '12', 'QUATWOLF’s multi-purpose sturdy skipping')
        Store_11 = ('PACK OF 2 – GRAPHENE ENHANCED MASK', '105', '18', 'The Graphene Enhanced Mask is a technical face mask')
        Store_12 = ('PACK OF 2 – POLYGIENE®', '65', '30', 'Four-LAYER REUSABLE MASK – KEFFIYEH')
        Store_13 = ('CORE HOLDALL SMALL – ONYX', '230', '40', 'Core Holdall is your go to bag for all scenarios')
        Store_14 = ('CORE BUMBAG – ONYX', '130', '80', 'It is a multi-purpose bag given its storage functionality')
        Store_15 = ('SQUATWOLF 3D SLIDERS – MEN – ONYX', '130', '9', 'RComfortable Footwear Slide into comfortable footwear ')
        Store_16 = ('LREBEL BEANIE – ONYX', '85', '7', 'A beanie with a statement, the Rebel Beanie')
        Store_17 = ('LAB360º PERFORMANCE', '120', '100', 'The LAB360º Performance Cap is super-lightweight')
        Store_18 = ('PACK OF 3 – CORE CREW SOCKS – ONYX', '90', '13', 'Made with premium cotton')
        Store_19 = ('SQUATWOLF POWER BAND – HEAVY', '105', '25', 'Resistance Level: 25-75kg / Heavy')
        Store_20 = ('EAD THE PACK CAP – WHITE', '120', '29', 'The Pack’ Cap features a cotton base with embroidered logo ')


        create_Store(conn,Store_1)
        create_Store(conn, Store_2)
        create_Store(conn, Store_3)
        create_Store(conn, Store_4)
        create_Store(conn, Store_5)
        create_Store(conn, Store_6)
        create_Store(conn, Store_7)
        create_Store(conn, Store_8)
        create_Store(conn, Store_9)
        create_Store(conn, Store_10)
        create_Store(conn, Store_11)
        create_Store(conn, Store_12)
        create_Store(conn, Store_13)
        create_Store(conn, Store_14)
        create_Store(conn, Store_15)
        create_Store(conn, Store_16)
        create_Store(conn, Store_17)
        create_Store(conn, Store_18)
        create_Store(conn, Store_19)
        create_Store(conn, Store_20)




# if __name__ == '__main__':
#     DBmain()

