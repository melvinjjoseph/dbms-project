import streamlit as st
import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(user="root", password="246810", host="localhost")
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS electricity")
mycursor.execute("USE electricity")

def add_customer(name,address,city,state):
    mycursor.execute("CREATE TABLE IF NOT EXISTS customer (cust_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255), city VARCHAR(255), state VARCHAR(255))")
    sql = "INSERT INTO customer (name, address, city, state) VALUES (%s, %s, %s, %s)"
    val = (name, address, city, state)
    mycursor.execute(sql, val)
    mydb.commit()
    
    return mycursor.lastrowid

def read_customer():
    mycursor.execute("SELECT * FROM customer")
    myresult = mycursor.fetchall()
    st.write("Customer details")
    df=pd.DataFrame(myresult,columns=['cust_id','name','address','city','state'])
    st.dataframe(df)


def delete_customer_db(cust_id):
    #check if cust_id exists
    mycursor.execute("SELECT * FROM customer WHERE cust_id = %s",(cust_id,))
    myresult = mycursor.fetchall()
    if not myresult:
        st.write("cust_id does not exist")
        return
    sql = "DELETE FROM customer WHERE cust_id = %s"
    val = (cust_id,)
    mycursor.execute(sql, val)
    mydb.commit()
    st.write("Customer deleted successfully")

def update_customer_db(cust_id,name,address,city,state):
    sql = "UPDATE customer SET name = %s, address = %s, city = %s, state = %s WHERE cust_id = %s"
    val = (name, address, city, state, cust_id)
    mycursor.execute(sql, val)
    mydb.commit()
    st.write("Customer updated successfully")

def add_admin(name,Customer_id):
    mycursor.execute("CREATE TABLE IF NOT EXISTS admin (admin_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), Customer_id INT NOT NULL, FOREIGN KEY (Customer_id) REFERENCES customer(cust_id))")
    sql = "INSERT INTO admin (name, Customer_id) VALUES (%s, %s)"
    val = (name, Customer_id)
    mycursor.execute(sql, val)
    mydb.commit()
    return mycursor.lastrowid

def read_admin():
    mycursor.execute("SELECT * FROM admin")
    myresult = mycursor.fetchall()
    st.write("Admin details")
    df=pd.DataFrame(myresult,columns=['admin_id','name','Customer_id'])
    st.dataframe(df)


def update_admin_db(admin_id,name,Customer_id):
    sql = "UPDATE admin SET name = %s, Customer_id = %s WHERE admin_id = %s"
    val = (name, Customer_id, admin_id)
    mycursor.execute(sql, val)
    mydb.commit()
    st.write("Admin updated successfully")

def delete_admin_db(admin_id):
    #check if admin_id exists
    mycursor.execute("SELECT * FROM admin WHERE admin_id = %s",(admin_id,))
    myresult = mycursor.fetchall()
    if not myresult:
        st.write("admin_id does not exist")
        return
    sql = "DELETE FROM admin WHERE admin_id = %s"
    val = (admin_id,)
    mycursor.execute(sql, val)
    mydb.commit()
    st.write("Admin deleted successfully")

def add_bill(cust_id,meter_no,units,cost_per_unit,due_date):
    mycursor.execute("CREATE TABLE IF NOT EXISTS bill (bill_id INT AUTO_INCREMENT PRIMARY KEY, cust_id INT NOT NULL, meter_no INT NOT NULL, units INT NOT NULL, cost_per_unit INT NOT NULL, amount INT NOT NULL, due_date DATE NOT NULL, FOREIGN KEY (cust_id) REFERENCES customer(cust_id))")
    sql = "INSERT INTO bill (cust_id, meter_no, units, cost_per_unit, amount, due_date) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (cust_id, meter_no, units, cost_per_unit, int(units)*int(cost_per_unit), due_date)
    mycursor.execute(sql, val)
    mydb.commit()
    st.write("Bill added successfully")
    return mycursor.lastrowid

def read_bill():
    mycursor.execute("SELECT * FROM bill")
    myresult = mycursor.fetchall()
    st.write("Bill details")
    df=pd.DataFrame(myresult,columns=['bill_id','cust_id','meter_no','units','cost_per_unit','amount','due_date'])
    st.dataframe(df)


def update_bill_db(bill_id,cust_id,meter_no,units,cost_per_unit, due_date):
    sql = "UPDATE bill SET cust_id = %s, meter_no = %s, units = %s, cost_per_unit = %s, amount = %s, due_date=%s WHERE bill_id = %s"
    val = (cust_id, meter_no, units, cost_per_unit, int(units)*int(cost_per_unit), due_date, bill_id)
    mycursor.execute(sql, val)
    mydb.commit()
    st.write("Bill updated successfully")

def delete_bill_db(bill_id):
    #check if bill_id exists
    mycursor.execute("SELECT * FROM bill WHERE bill_id = %s",(bill_id,))
    myresult = mycursor.fetchall()
    if not myresult:
        st.write("bill_id does not exist")
        return
    sql = "DELETE FROM bill WHERE bill_id = %s"
    val = (bill_id,)
    mycursor.execute(sql, val)
    mydb.commit()
    st.write("Bill deleted successfully")

def add_tariff(tariff_type,tariff_cost):
    mycursor.execute("CREATE TABLE IF NOT EXISTS tariff (tariff_id INT AUTO_INCREMENT PRIMARY KEY, tariff_type VARCHAR(255), tariff_cost INT NOT NULL)")
    sql = "INSERT INTO tariff (tariff_type, tariff_cost) VALUES (%s, %s)"
    val = (tariff_type, tariff_cost)
    mycursor.execute(sql, val)
    mydb.commit()
    return mycursor.lastrowid

def read_tariff():
    mycursor.execute("SELECT * FROM tariff")
    myresult = mycursor.fetchall()
    st.write("Tariff details")
    df=pd.DataFrame(myresult,columns=['tariff_id','tariff_type','tariff_cost'])
    st.dataframe(df)

def update_tariff_db(tariff_id,tariff_type,tariff_cost):
    sql = "UPDATE tariff SET tariff_type = %s, tariff_cost = %s WHERE tariff_id = %s"
    val = (tariff_type, tariff_cost, tariff_id)
    mycursor.execute(sql, val)
    mydb.commit()
    st.write("Tariff updated successfully")

def delete_tariff_db(tariff_id):
    sql = "DELETE FROM tariff WHERE tariff_id = %s"
    val = (tariff_id,)
    mycursor.execute(sql, val)
    mydb.commit()
    st.write("Tariff deleted successfully")