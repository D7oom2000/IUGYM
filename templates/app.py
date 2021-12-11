
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
              with sqlite3.connect(r"C:\Users\dhooo\PycharmProjects\GYMProjectFlask\GYMProject.db") as conn:
                cur = conn.cursor()
                cur.execute('INSERT INTO Coach (CName, CPass, CAge) VALUES (?,?,?)', (user_name,password,cage))
                conn.commit()
                error = "Coach registered successfully!"
        except:
            conn.rollback()
            error = "Invalid Inputs!"
        finally:
            return render_template("Coach_register.html", error=error)
            con.close()

# ===============================================================================
@app.route('/coach_changepass_link', methods=['GET', 'POST'])
def Goto_Coach_Changepass():
    return render_template('Coach_Changepass.html')
# ===============================================================================
@app.route('/coach_ChangePass_url', methods=['GET', 'POST'])
def coach_ChangePass_url():
    error = ''
    if request.method == 'POST':
        try:
            user_name = request.form['CNameChange']
            password = request.form['CPassChange']
            newpass = request.form['CPassNew']

            conn = sqlite3.connect(r"C:\Users\dhooo\PycharmProjects\GYMProjectFlask\GYMProject.db")
            cur = conn.cursor()
            query = 'SELECT CPass FROM Coach WHERE CName =?'
            cur.execute(query, [user_name])
            result = cur.fetchall()
            if len(result) == 0:
                error = "Invalid username!"
            elif len(result) == 1:
                if str(result[0][0]) != password:
                    error = "Wrong password!"
                else:
                    cur = conn.cursor()
                    cur.execute('UPDATE Coach set CPass = ? WHERE CName =?', (newpass, user_name))
                    conn.commit()
                    error = "Password successfully Changed!"
        except:
            conn.rollback()
            error = "Invalid Inputs!"
        finally:
            return render_template("Coach_Changepass.html", error=error)
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
              with sqlite3.connect(r"C:\Users\dhooo\PycharmProjects\GYMProjectFlask\GYMProject.db") as conn:
                cur = conn.cursor()
                cur.execute('INSERT INTO Trainee (TName, TPass, TAge, Balance) VALUES (?,?,?,?)', (user_name,password,cage,balance))
                conn.commit()
                error = "Trainee registered successfully!"
        except:
            conn.rollback()
            error = "Invalid Inputs!"
        finally:
            return render_template("Trainee_register.html", error=error)
            con.close()

# ===============================================================================
@app.route('/trainee_changepass_link', methods=['GET', 'POST'])
def Goto_Trainee_Changepass():
    return render_template('Trainee_Changepass.html')
# ===============================================================================
@app.route('/trainee_ChangePass_url', methods=['GET', 'POST'])
def trainee_ChangePass_url():
    error = ''
    if request.method == 'POST':
        try:
            user_name = request.form['TNameChange']
            password = request.form['TPassChange']
            newpass = request.form['TPassNew']

            conn = sqlite3.connect(r"C:\Users\dhooo\PycharmProjects\GYMProjectFlask\GYMProject.db")
            cur = conn.cursor()
            query = 'SELECT TPass FROM Trainee WHERE TName =?'
            cur.execute(query, [user_name])
            result = cur.fetchall()
            if len(result) == 0:
                error = "Invalid username!"
            elif len(result) == 1:
                if str(result[0][0]) != password:
                    error = "Wrong password!"
                else:
                    cur = conn.cursor()
                    cur.execute('UPDATE Trainee set TPass = ? WHERE TName =?', (newpass, user_name))
                    conn.commit()
                    error = "Password successfully Changed!"
        except:
            conn.rollback()
            error = "Invalid Inputs!"
        finally:
            return render_template("Trainee_Changepass.html", error=error)
            con.close()

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
@app.route('/Cstore_list_link', methods=['GET', 'POST'])
def GoCStoretable():
    return render_template('StoreList.html')

# ==============================================================================
@app.route('/Cstore_list_url')
def CStoreTable():
    error, data = StoreList()
    if error == "":
        return render_template("CStoreList.html", value=data)
    else:
        return render_template("CStoreList.html", result=error)
# ==============================================================================
@app.route('/Tstore_list_link', methods=['GET', 'POST'])
def GoTStoretable():
    return render_template('TStoreList.html')

# ==============================================================================
@app.route('/Tstore_list_url')
def TStoreTable():
    error, data = StoreList()
    if error == "":
        return render_template("TStoreList.html", value=data)
    else:
        return render_template("TStoreList.html", result=error)
# ==============================================================================
@app.route('/add_product_link', methods=['GET', 'POST'])
def add_product_url():
    return render_template('add_product.html')
# #==============================================================================
@app.route('/add_product', methods=['POST', 'GET'])
def Add_Product():
    error = ''
    if request.method == 'POST':
        try:
            name = request.form['PName']
            price = request.form['PPrice']
            quantity = request.form['PQuantity']

            if len(name) == 0 or len(price) == 0 or len(quantity) == 0:
                error = "Please input all fields."
            else:
              with sqlite3.connect(r"C:\Users\dhooo\PycharmProjects\GYMProjectFlask\GYMProject.db") as conn:
                cur = conn.cursor()
                cur.execute('INSERT INTO Store (ItemName, ItemPrice, ItemQuantity) VALUES (?,?,?)', (name,float(price),int(quantity)))
                conn.commit()
                error = "Products Added Successfully!"
        except:
            conn.rollback()
            error = "Invalid Inputs!"
        finally:
            return render_template("add_product.html", error=error)
            con.close()

# ==============================================================================

# =============================================================
# if __name__ == '__main__':
#     app.run(host='localhost', port='5555', debug=True)
# =============================================================
