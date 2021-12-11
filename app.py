from flask import *
import sys

import sqlite3
from sqlite3 import Error
from GYMDB import *
from flask import Flask, request, redirect, render_template

app = Flask(__name__)

#       == Students Work == #             # == Students UID == #
# == Abdulrahman Ibrahim Bin Nouh == #      # == 391002643 == #
#        == Ali Ismail == #                # == 391022143 == #

# =============================================================
@app.route('/')
def WelcomePage():
    return render_template('welcome_page.html', result='')

# ==============================================================================
@app.route('/coach_login_link', methods=['GET', 'POST'])
def coach_login():
    return render_template('Coach_login.html')

# ==============================================================================
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

# ==============================================================================
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
@app.route('/coach_register_link', methods=['GET', 'POST'])
def Goto_Coach_Register():
    return render_template('Coach_register.html')

# ==============================================================================
@app.route('/coach_register_url', methods=['GET', 'POST'])
def coach_register_url():
    error = ''
    if request.method == 'POST':
        try:
            user_name = request.form['CNameReg']
            password = request.form['CPassReg']
            confpass = request.form['CPassConf']
            cage = request.form['CAge']
            if password != confpass:
                error = 'Passwords are not match!'
            elif int(cage) < 16:
                error = 'Illegal Age!'
            else:
              with sqlite3.connect(r"C:\Users\dhooo\PycharmProjects\GYMProjectFlask\GYMProject.db") as con:
                cur = con.cursor()
                cur.execute('INSERT INTO Coach (CName, CPass, CAge) VALUES (?,?,?)', (user_name,password,cage))
                con.commit()
                error = "Coach registered successfully!"
        except:
            con.rollback()
            error = "Invalid Inputs!"
        finally:
            return render_template("Coach_register.html", error=error)
            con.close()

# ===============================================================================
@app.route('/trainee_resgister_link', methods=['GET', 'POST'])
def Goto_Trainee_Register():
    return render_template('Trainee_register.html')
# ===============================================================================
@app.route('/trainee_register_url', methods=['GET', 'POST'])
def trainee_register_url():
    error = ''
    if request.method == 'POST':
        try:
            user_name = request.form['TNameReg']
            password = request.form['TPassReg']
            confpass = request.form['TPassConf']
            cage = request.form['TAge']
            balance = request.form["Balance"]
            if password != confpass:
                error = 'Passwords are not match!'
            elif int(cage) < 16:
                error = 'Illegal Age!'
            elif int(balance) <= 99:
                error = 'Balance must be at least 100!'
            else:
              with sqlite3.connect(r"C:\Users\dhooo\PycharmProjects\GYMProjectFlask\GYMProject.db") as con:
                cur = con.cursor()
                cur.execute('INSERT INTO Trainee (TName, TPass, TAge, Balance) VALUES (?,?,?,?)', (user_name,password,cage,balance))
                con.commit()
                error = "Trainee registered successfully!"
        except:
            con.rollback()
            error = "Invalid Inputs!"
        finally:
            return render_template("Trainee_register.html", error=error)
            con.close()

# ====================================================

# ===============================================================================
@app.route('/coach_gate_link', methods=['GET', 'POST'])
def CoachGate():
    return render_template('CoachGate.html')


# ==============================================================================
@app.route('/trainee_gate_link', methods=['GET', 'POST'])
def TraineeGate():
    return render_template('TraineeGate.html')


# #==============================================================================
@app.route('/trainee_list_url')
def TraineeTable():
    error, data = TraineeList()
    if error == "":
        return render_template("TraineesList.html", value=data)
    else:
        return render_template("TraineesList.html", result=error)


# ==============================================================================
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


# ==============================================================================
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
# ==============================================================================

# =================================================================================

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
# class CancelSubscription():
# def __init__(self):
# super(CancelSubscription,self).__init__()
# loadUi(r"C:\Users\dhooo\PycharmProjects\GYMProject\CancelSub.ui",self)
# self.TPassword.setEchoMode(QtWidgets.QLineEdit.Password)
# self.CancelSub.clicked.connect(self.CancelSubFun)
# ==================================================================================
# def CancelSubFun(self): # Cancel Subscription function
#  TUsername = self.TUsername.text()
# TPassword = self.TPassword.text()

#  conn = sqlite3.connect(r".\GYMProject.db")
# cur = conn.cursor()
# query = 'SELECT * FROM Trainee WHERE TName =?'
# cur.execute(query, [TUsername])
# result = cur.fetchall()

# if len(TUsername) == 0 or len(TPassword) == 0:
#   self.ErrorReg.setText("Please input all fields.")
# elif len(result) == 0:
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
