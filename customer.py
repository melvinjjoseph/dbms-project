import streamlit as st
from database import *

def create_customer():
    name=st.text_input("Enter name")
    address=st.text_input("Enter address")
    city=st.text_input("Enter city")
    state=st.text_input("Enter state")
    submit=st.button("Submit")
    if submit:
        cust_id=add_customer(name,address,city,state) 
        st.write("Customer id is ",cust_id)
        st.write ("Customer added successfully")

def view_customer():
    st.write("View mode on")
    read_customer()

def delete_customer():
    st.write("Delete mode on")
    cust_id=st.number_input("Enter customer id",min_value=1,step=1)
    submit=st.button("Submit")
    if submit:
        delete_customer_db(cust_id)

def update_customer():
    st.write("Select customer id to update")
    cust_id=st.number_input("Enter customer id",min_value=1,step=1)
    name=st.text_input("Enter name")
    address=st.text_input("Enter address")
    city=st.text_input("Enter city")
    state=st.text_input("Enter state")
    submit=st.button("Submit")

    # check if customer_id exists in database
    mycursor.execute("SELECT * FROM customer WHERE cust_id = %s", (cust_id,))
    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        st.write("Customer id does not exist")
        return 
    elif submit and len(myresult) > 0:
        update_customer_db(cust_id,name,address,city,state)


