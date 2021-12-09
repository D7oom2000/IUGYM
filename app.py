from flask import *
import sys

import sqlite3
from sqlite3 import Error
from GYMDB import *
from flask import Flask, request, redirect, render_template

app = Flask(__name__)
# =============================================================
@app.route('/')
def WelcomePage():
    return render_template('CoachGate.html', result='')

# ==============================================================================
@app.route('/coach_login_link', methods=['GET', 'POST'])
def coach_login():
    return render_template('Coach_login.html')
#==============================================================================
@app.route('/coach_login_url', methods=['GET', 'POST'])
def coach_login_url():
    if request.method == 'POST':
        form_inputs = request.form
        flag = check_login_coach(form_inputs)
        if flag:
            return redirect(url_for('CoachGate'))
        else:
            error = "invalid username or password"
            return render_template('Coach_login.html', error=error)
# ==============================================================================
@app.route('/trainee_login_link', methods=['GET', 'POST'])
def trainee_login():
    return render_template('Trainee_login.html')
#==============================================================================
@app.route('/trainee_login_url', methods=['GET', 'POST'])
def trainee_login_url():
    if request.method == 'POST':
        form_inputs = request.form
        flag = check_login_trainee(form_inputs)
        if flag:
            return redirect(url_for('TraineeGate'))
        else:
            error = "invalid username or password"
            return render_template('Trainee_login.html', error=error)

# ==============================================================================
# @app.route('/coach_register_link', methods=['GET', 'POST'])
# def coach_register_url():
#     if request.method == 'POST':
#         form_inputs = request.form
#         flag = check_register_coach(form_inputs)
#         if flag:
#             return render_template('CoachGate.html')
#         else:
#             res = "invalid username or password"
#             return render_template('Coach_register.html', result=res)
# #==============================================================================
# @app.route('/trainee_register_link', methods=['GET', 'POST'])
# def trainee_register_url():
#     if request.method == 'POST':
#         form_inputs = request.form
#         flag = check_register_trainee(form_inputs)
#         if flag:
#             return render_template('TraineeGate.html')
#         else:
#             res = "invalid username or password"
#             return render_template('Trainee_register.html', result=res)
# ===============================================================================
@app.route('/coach_gate_link', methods=['GET', 'POST'])
def CoachGate():
    return render_template('CoachGate.html')
#==============================================================================
@app.route('/trainee_gate_link', methods=['GET', 'POST'])
def TraineeGate():
    return render_template('TraineeGate.html')
# #==============================================================================
@app.route('/trainee_list_url')
def TraineeTable():
    error, data = TraineeList()
    if error=="":
        return render_template("TraineesList.html", value=data)
    else:
        return render_template("TraineesList.html", result=error)
#==============================================================================
@app.route('/trainee_list_link', methods=['GET', 'POST'])
def GoTraineetable():
    return render_template('TraineesList.html')
# ==============================================================================
@app.route('/machine_list_url')
def MachineTable():
    error, data = MachineList()
    if error == "":
        return render_template("MachinesList.html", value=data)
    else:
        return render_template("MachinesList.html", result=error)

# ==============================================================================
@app.route('/trainee_list_link', methods=['GET', 'POST'])
def GoMachinetable():
    return render_template('MachinesList.html')
#==============================================================================
# @app.route('/update_product_link', methods=['GET', 'POST'])
# def update_product_url():
#     return render_template('add_product.html')
# #==============================================================================
# @app.route('/add_product', methods=['POST', 'GET'])
# def add_product_fun():
#     if request.method == 'POST':
#         form_inputs = request.form
#         msg = insert(form_inputs)
#         return render_template('add_product.html', result=msg)
#==============================================================================

# =============================================================

       # == Students Work == #             # == Students UID == #
# == Abdulrahman Ibrahim Bin Nouh == #      # == 391002643 == #
        # == Ali Ismail == #                # == 391022143 == #
# =================================================================================
#
# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'
#
#
#
#        # == Students Work == #             # == Students UID == #
# # == Abdulrahman Ibrahim Bin Nouh == #      # == 391002643 == #
#         # == Ali Ismail == #                # == 391022143 == #
# # =================================================================================
# class WelcomeScreen(QDialog): # Welcome Screen
#     def __init__(self):
#         super(WelcomeScreen, self).__init__()
#         loadUi(r"C:\Users\dhooo\PycharmProjects\GYMProject\GYMWelcomeScreen.ui",self)
#         self.CoachWindow.clicked.connect(self.OpenCoachScreen)
#         self.TraineeWindow.clicked.connect(self.OpenTraineeScreen)
# # =================================================================================
#     def OpenCoachScreen(self): # It directs to the Coach page
#         global widget
#         Coach = CoachLogin()
#         widget.addWidget(Coach)
#         widget.setCurrentIndex(widget.currentIndex()+1)
# # =================================================================================
#     def OpenTraineeScreen(self): # It directs to the Trainee page
#         global widget
#         Trainee = TraineeLogin()
#         widget.addWidget(Trainee)
#         widget.setCurrentIndex(widget.currentIndex()+1)
# # =================================================================================
# class CoachLogin(QDialog): # defining UI of login coach account page and its fields
#     def __init__(self):
#         super(CoachLogin,self).__init__()
#         loadUi(r"C:\Users\dhooo\PycharmProjects\GYMProject\CLogin.ui",self)
#         self.loginbutton.clicked.connect(self.Cloginfunction)
#         self.CPassword.setEchoMode(QtWidgets.QLineEdit.Password)
#         self.CCeateaccbutton.clicked.connect(self.Cgotocreate)
#         self.CChangePass.clicked.connect(self.OpenCChangePass)
# # ================================================================================
#     def Cloginfunction(self): # Login coach account function
#         CUsername=self.CUsername.text()
#         CPassword=self.CPassword.text()
#
#         if len(CUsername) == 0 or len(CPassword) == 0:
#             QMessageBox.information(None, "Error!","Please input all fields.", )
#
#         else:
#             conn = sqlite3.connect("GYMProject.db")
#             cur = conn.cursor()
#             query = 'SELECT CPass FROM Coach WHERE CName =?'
#             cur.execute(query, [CUsername])
#             result = cur.fetchall()
#             if len(result) == 1:
#
#                 if result[0][0] == CPassword:
#                     QMessageBox.information(None, "Completed!", "Successfully logged in.", )
#                     CGate = CoachGate()
#                     widget.addWidget(CGate)
#                     widget.setCurrentIndex(widget.currentIndex() + 1)
#                 else:
#                     QMessageBox.information(None, "Error!", "Invalid password", )
#             else:
#                 msg_box = QMessageBox()
#                 msg_box.setWindowTitle("Error")  # optional
#                 msg_box.setIcon(QMessageBox.Critical)  # optional (Information, Question, Warning, Critical)
#                 msg_box.setText("Invalid user name!")
#                 msg_box.exec()
#
#             conn.commit()
#             conn.close()
#
# # ================================================================================
#     def Cgotocreate(self): # It directs to the create coach account page
#         createacc=CoachCreateAcc()
#         widget.addWidget(createacc)
#         widget.setCurrentIndex(widget.currentIndex()+1)
# # ================================================================================
#     def OpenCChangePass(self): # It directs to the change coach password page
#         CChangepass=CoachChangePass()
#         widget.addWidget(CChangepass)
#         widget.setCurrentIndex(widget.currentIndex()+1)
# # ================================================================================
# class CoachCreateAcc(QDialog): # defining UI of create coach account page and its fields
#     def __init__(self):
#         super(CoachCreateAcc,self).__init__()
#         loadUi("CoachCreateAcc.ui",self)
#         self.signupbutton.clicked.connect(self.Ccreateaccfunction)
#         self.CPassword.setEchoMode(QtWidgets.QLineEdit.Password)
#         self.CConfirmpass.setEchoMode(QtWidgets.QLineEdit.Password)
#
# # ================================================================================
#     def Ccreateaccfunction(self): # Create coach account function
#
#         CUsername = self.CUsername.text()
#         CPassword = self.CPassword.text()
#         CConfirmpass = self.CConfirmpass.text()
#         CAge = self.CAge.text()
#
#         if len(CUsername) == 0 or len(CPassword) == 0 or len(CConfirmpass) == 0 or len(CAge) == 0:
#             QMessageBox.information(None, "Error!","Please fill the fields.", )
#
#         elif CPassword != CConfirmpass:
#             QMessageBox.information(None, "Error!","Passwords aren't match.", )
#
#         elif int(CAge) < 16:
#             QMessageBox.information(None, "Error!", "Illegal age", )
#
#         else:
#             conn = sqlite3.connect("GYMProject.db")
#             cur = conn.cursor()
#
#             Coach_info = [CUsername, CPassword, CAge]
#             cur.execute('INSERT INTO Coach (CName, CPass, CAge) VALUES (?,?,?)', Coach_info)
#             QMessageBox.information(None, "Completed!", "Coach successfully added", )
#             conn.commit()
#             conn.close()
# # ====================================================================================
# class CoachChangePass(QDialog): # defining UI of change coach password page and its fields
#     def __init__(self):
#         super(CoachChangePass,self).__init__()
#         loadUi(r"C:\Users\dhooo\PycharmProjects\GYMProject\CNewPass.ui",self)
#
#         self.CPassword.setEchoMode(QtWidgets.QLineEdit.Password)
#         self.CNewPass.setEchoMode(QtWidgets.QLineEdit.Password)
#         self.CChangePass.clicked.connect(self.ChangeCoachPass)
# # =====================================================================================
#     def ChangeCoachPass(self): # change coach password function
#         CUsername = self.CUsername.text()
#         CPassword = self.CPassword.text()
#         CNewPass = self.CNewPass.text()
#         conn = sqlite3.connect(r".\GYMProject.db")
#         cur = conn.cursor()
#         query = 'SELECT CPass FROM Coach WHERE CName =?'
#         cur.execute(query, [CUsername])
#         result = cur.fetchall()
#
#         if len(CUsername) == 0 or len(CPassword) == 0 or len(CNewPass) == 0:
#             self.ErrorReg.setText("Please input all fields.")
#         elif len(result) == 0:
#             QMessageBox.information(None, "Error!", "Invalid username!", )
#         elif len(result) == 1:
#             if str(result[0][0]) != CPassword:
#                 QMessageBox.information(None, "Error!", "Wrong password!", )
#             else:
#                 cur = conn.cursor()
#                 cur.execute('UPDATE Coach set CPass = ? WHERE CName =?', (CNewPass, CUsername))
#                 conn.commit()
#                 QMessageBox.information(None, "Completed!", "Password successfully Changed!", )
#
# # ====================================================================================
# class CoachGate(QDialog):  # Coach Gate
#     def __init__(self):
#         super(CoachGate, self).__init__()
#         loadUi(r"C:\Users\dhooo\PycharmProjects\GYMProject\CoachGate.ui", self)
#         self.ViewTrainees.clicked.connect(self.OpenViewTrainee)
#         self.ViewMachines.clicked.connect(self.OpenViewMachines)
# # ====================================================================================
#     def OpenViewTrainee(self): # It directs to the trainees table
#         global widget
#         ViewTTable = ViewTraineeTable()
#         widget.addWidget(ViewTTable)
#         widget.setCurrentIndex(widget.currentIndex() + 1)
#
# # =====================================================================================
#     def OpenViewMachines(self): # It directs to the machines table
#         global widget
#         ViewMTable = ViewMachineTable()
#         widget.addWidget(ViewMTable)
#         widget.setCurrentIndex(widget.currentIndex() + 1)
#
# # =====================================================================================
# class ViewTraineeTable(QDialog): # View Trainees table
#     def __init__(self):
#         super(ViewTraineeTable,self).__init__()
#         loadUi(r"C:\Users\dhooo\PycharmProjects\GYMProject\Trainee Table.ui",self)
#
#         with sqlite3.connect(r".\GYMProject.db") as conn:
#             cur = conn.cursor()
#             TTable = cur.execute('SELECT * FROM Trainee')
#
#             for RAWindex, RAWdata in enumerate(TTable): # Nested loop for the raws and columns of trainee table
#                 self.TraineeTable.insertRow(RAWindex)
#                 for COLMindex, COLMdata in enumerate(RAWdata):
#                     self.TraineeTable.setItem(RAWindex, COLMindex, QTableWidgetItem(str(COLMdata)))
# # =====================================================================================
# class ViewMachineTable(QDialog): # View sport machines table
#     def __init__(self):
#         super(ViewMachineTable,self).__init__()
#         loadUi(r"C:\Users\dhooo\PycharmProjects\GYMProject\Machine Table.ui",self)
#
#         with sqlite3.connect(r".\GYMProject.db") as conn:
#             cur = conn.cursor()
#             MTable = cur.execute('SELECT * FROM Machine')
#
#             for RAWindex, RAWdata in enumerate(MTable): # Nested loop for the raws and columns of machine table
#                 self.MachineTable.insertRow(RAWindex)
#                 for COLMindex, COLMdata in enumerate(RAWdata):
#                     self.MachineTable.setItem(RAWindex, COLMindex, QTableWidgetItem(str(COLMdata)))
#
# # =====================================================================================
# class TraineeLogin(QDialog): # defining UI of Trainee login page and its fields
#     def __init__(self):
#         super(TraineeLogin,self).__init__()
#         loadUi(r"C:\Users\dhooo\PycharmProjects\GYMProject\TLogin.ui",self)
#         self.loginbutton.clicked.connect(self.Tloginfunction)
#         self.TPassword.setEchoMode(QtWidgets.QLineEdit.Password)
#         self.TCeateaccbutton.clicked.connect(self.Tgotocreate)
#         self.TChangePass.clicked.connect(self.OpenTChangePass)
#
# # =================================================================================
#     def Tloginfunction(self): # Login Trainee account function
#         TUsername=self.TUsername.text()
#         TPassword=self.TPassword.text()
#         if len(TUsername) == 0 or len(TPassword) == 0:
#             QMessageBox.information(None, "Error!","Please input all fields.", )
#         else:
#             conn = sqlite3.connect("GYMProject.db")
#             cur = conn.cursor()
#             query = 'SELECT TPass FROM Trainee WHERE TName=?'
#             cur.execute(query, [TUsername])
#             result = cur.fetchall()
#             if len(result) == 1:
#                 if result[0][0] == TPassword:
#                     QMessageBox.information(None, "Completed!", "Successfully logged in.", )
#                     TGate = TraineeGate()
#                     widget.addWidget(TGate)
#                     widget.setCurrentIndex(widget.currentIndex() + 1)
#                 else:
#                     QMessageBox.information(None, "Error!", "Invalid password", )
#             else:
#                 msg_box = QMessageBox()
#                 msg_box.setWindowTitle("Error")  # optional
#                 msg_box.setIcon(QMessageBox.Critical)  # optional (Information, Question, Warning, Critical)
#                 msg_box.setText("Invalid user name!")
#                 msg_box.exec()
#
#             conn.commit()
#             conn.close()
#
# # =================================================================================
#     def Tgotocreate(self): # It directs to the create Trainee account page
#         createacc=TraineeCreateAcc()
#         widget.addWidget(createacc)
#         widget.setCurrentIndex(widget.currentIndex()+1)
# # ================================================================================
#     def OpenTChangePass(self): # It directs to the Change Trainee password page
#         TChangepass=TraineeChangePass()
#         widget.addWidget(TChangepass)
#         widget.setCurrentIndex(widget.currentIndex()+1)
# # =================================================================================
# class TraineeCreateAcc(QDialog): # defining UI of Trainee create account page and its fields
#
#     def __init__(self):
#         super(TraineeCreateAcc,self).__init__()
#         loadUi("TraineeCreateAcc.ui",self)
#         self.signupbutton.clicked.connect(self.Tcreateaccfunction)
#         self.TPassword.setEchoMode(QtWidgets.QLineEdit.Password)
#         self.TConfirmpass.setEchoMode(QtWidgets.QLineEdit.Password)
#
# # =================================================================================
#     def Tcreateaccfunction(self): # Create Trainee Account function
#
#         TUsername = self.TUsername.text()
#         TPassword = self.TPassword.text()
#         TConfirmpass = self.TConfirmpass.text()
#         TAge = self.TAge.text()
#
#         if len(TUsername) == 0 or len(TPassword) == 0 or len(TConfirmpass) == 0 or len(TAge) == 0:
#             QMessageBox.information(None, "Error!", "Please fill the fields.", )
#
#         elif TPassword != TConfirmpass:
#             QMessageBox.information(None, "Error!","Passwords aren't match.", )
#
#         elif int(TAge) < 16:
#             QMessageBox.information(None, "Error!","Illegal age", )
#
#         else:
#             conn = sqlite3.connect("GYMProject.db")
#             cur = conn.cursor()
#
#             Trainee_info = [TUsername, TPassword, TAge]
#             cur.execute('INSERT INTO Trainee (TName, TPass, TAge ) VALUES (?,?,?)', Trainee_info)
#             QMessageBox.information(None, "Completed!", "Trainee successfully added", )
#
#             conn.commit()
#             conn.close()
# # =================================================================================
# class TraineeChangePass(QDialog): # defining UI of change Trainee password page and its fields
#     def __init__(self):
#         super(TraineeChangePass, self).__init__()
#         loadUi(r"C:\Users\dhooo\PycharmProjects\GYMProject\TNewPass.ui", self)
#
#         self.TPassword.setEchoMode(QtWidgets.QLineEdit.Password)
#         self.TNewPass.setEchoMode(QtWidgets.QLineEdit.Password)
#         self.TChangePass.clicked.connect(self.ChangeTraineePass)
#
#     # =====================================================================================
#     def ChangeTraineePass(self): # Change Trainee password function
#         TUsername = self.TUsername.text()
#         TPassword = self.TPassword.text()
#         TNewPass = self.TNewPass.text()
#         conn = sqlite3.connect(r".\GYMProject.db")
#         cur = conn.cursor()
#         query = 'SELECT TPass FROM Trainee WHERE TName =?'
#         cur.execute(query, [TUsername])
#         result = cur.fetchall()
#
#         if len(TUsername) == 0 or len(TPassword) == 0 or len(TNewPass) == 0:
#             self.ErrorReg.setText("Please input all fields.")
#         elif len(result) == 0:
#             QMessageBox.information(None, "Error!", "Invalid username!", )
#         elif len(result) == 1:
#             if str(result[0][0]) != TPassword:
#                 QMessageBox.information(None, "Error!", "Wrong password!", )
#             else:
#                 cur = conn.cursor()
#                 cur.execute('UPDATE Trainee set TPass = ? WHERE TName =?', (TNewPass, TUsername))
#                 conn.commit()
#                 QMessageBox.information(None, "Completed!", "Password successfully Changed!", )
# # =================================================================================
# class TraineeGate(QDialog):  # Trainee Gate
#     def __init__(self):
#         super(TraineeGate, self).__init__()
#         loadUi(r"C:\Users\dhooo\PycharmProjects\GYMProject\TraineeGate.ui", self)

        # == Cancel Trainee's subscription was not implemented! == #

        # self.CancelSub.clicked.connect(self.OpenCancelSub)
# =================================================================================
   # def OpenCancelSub(self):
   #     CancelSub = CancelSubscription()
   #     widget.addWidget(CancelSub)
   #     widget.setCurrentIndex(widget.currentIndex() + 1)
# =================================================================================
#class CancelSubscription():
    #def __init__(self):
        #super(CancelSubscription,self).__init__()
       # loadUi(r"C:\Users\dhooo\PycharmProjects\GYMProject\CancelSub.ui",self)
       # self.TPassword.setEchoMode(QtWidgets.QLineEdit.Password)
       # self.CancelSub.clicked.connect(self.CancelSubFun)
    # ==================================================================================
   # def CancelSubFun(self): # Cancel Subscription function
      #  TUsername = self.TUsername.text()
       # TPassword = self.TPassword.text()

      #  conn = sqlite3.connect(r".\GYMProject.db")
       # cur = conn.cursor()
        #query = 'SELECT * FROM Trainee WHERE TName =?'
       # cur.execute(query, [TUsername])
       # result = cur.fetchall()

       # if len(TUsername) == 0 or len(TPassword) == 0:
         #   self.ErrorReg.setText("Please input all fields.")
        #elif len(result) == 0:
        #    QMessageBox.information(None, "Error!", "Invalid username!", )
       # elif len(result) == 1:
        #    if str(result[0][0]) != TPassword:
          #      QMessageBox.information(None, "Error!", "Wrong password!", )
           # else:
            #    cur = conn.cursor()
             #   cur.execute('DELETE FROM Trainee  WHERE TPass = ? And TName =?', (TPassword, TUsername))
              #  conn.commit()
              #  QMessageBox.information(None, "Completed!", "Subscription successfully Canceled!", )
# ==================================================================================


# =============================================================
if __name__ == '__main__':
    app.run(host='localhost', port='5555', debug=True)
# =============================================================