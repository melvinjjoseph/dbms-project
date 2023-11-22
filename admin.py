import streamlit as st
from database import *

def create_admin():
    name=st.text_input("Enter name")
    Customer_id=st.text_input("Enter Customer_id")
    submit=st.button("Submit")
    if submit:
        admin_id=add_admin(name,Customer_id) 
        st.write("Admin id is ",admin_id)
        st.write ("Admin added successfully")
    
def update_admin():
    admin_id=st.text_input("Enter admin_id")
    name=st.text_input("Enter name")
    Customer_id=st.text_input("Enter Customer_id")
    submit=st.button("Submit")
    #check if admin_id exists
    mycursor.execute("SELECT * FROM admin WHERE admin_id = %s",(admin_id,))
    myresult = mycursor.fetchall()
    if not myresult:
        st.write("admin_id does not exist")
        return
    elif submit and myresult:
        update_admin_db(admin_id,name,Customer_id)
        st.write ("Admin updated successfully")

def delete_admin():
    admin_id=st.text_input("Enter admin_id")
    submit=st.button("Submit")
    #check if admin_id exists
    mycursor.execute("SELECT * FROM admin WHERE admin_id = %s",(admin_id,))
    myresult = mycursor.fetchall()
    if not myresult:
        st.write("admin_id does not exist")
        return
    elif submit and myresult:
        delete_admin_db(admin_id)