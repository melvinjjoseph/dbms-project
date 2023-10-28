import streamlit as st
from database import *

def create_bill():
    cust_id=st.text_input("Enter cust_id")
    meter_no=st.text_input("Enter meter_no")
    units=st.text_input("Enter units")
    cost_per_unit=st.text_input("Enter cost_per_unit")
    submit=st.button("Submit", key="create_bill")
    #check if cust_id exists
    mycursor.execute("SELECT * FROM customer WHERE cust_id = %s",(cust_id,))
    myresult = mycursor.fetchall()
    if not myresult:
        st.write("cust_id does not exist")
        return
    if submit:
        bill_id=add_bill(cust_id,meter_no,units,cost_per_unit) 
        st.write("Bill id is ",bill_id)

def update_bill():
    bill_id=st.text_input("Enter bill_id")
    cust_id=st.text_input("Enter cust_id")
    meter_no=st.text_input("Enter meter_no")
    units=st.text_input("Enter units")
    cost_per_unit=st.text_input("Enter cost_per_unit")
    submit=st.button("Submit", key="update_bill")
    #check if bill_id exists
    mycursor.execute("SELECT * FROM bill WHERE bill_id = %s",(bill_id,))
    myresult = mycursor.fetchall()
    if not myresult:
        st.write("bill_id does not exist")
        return
    elif submit and myresult:
        update_bill_db(bill_id,cust_id,meter_no,units,cost_per_unit)

def delete_bill():
    bill_id=st.text_input("Enter bill_id")
    submit=st.button("Submit", key="delete_bill")
    #check if bill_id exists
    mycursor.execute("SELECT * FROM bill WHERE bill_id = %s",(bill_id,))
    myresult = mycursor.fetchall()
    if not myresult:
        st.write("bill_id does not exist")
        return
    elif submit and myresult:
        delete_bill_db(bill_id)
        st.write ("Bill deleted successfully")