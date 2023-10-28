import streamlit as st
import mysql.connector
from database import *
from customer import *
from admin import *
from bill import *
from tariff import *



def main():
    st.title("Electricity management system")

    menu=["Home","Customer","Admin", "Billing", "Tariff", "Custom Query"]
    choice=st.sidebar.selectbox("Menu",menu)

    if choice=="Home":
        st.subheader("Home")
        st.header("Welcome to the electricity bill management system")
        st.write("This is a simple electricity bill management system")
        st.write("Please select a menu option from the sidebar")

    if choice == "Customer":

        st.subheader("Customer details")
        customer_menu=["Add","View","Update","Delete"]
        customer_choice=st.selectbox("Menu",customer_menu)
        if customer_choice=="Add":
            st.subheader("Enter details")
            create_customer()
        elif customer_choice=="View" :
            view_customer()
        elif customer_choice=="Update" :
            update_customer()
        elif customer_choice=="Delete" :
            delete_customer()
    
    if choice == "Admin":
        st.subheader("Admin")
        admin_menu=["Add","View","Update","Delete"]
        admin_choice=st.selectbox("Menu",admin_menu)
        if admin_choice=="Add":
            st.subheader("Enter details")
            create_admin()
        elif admin_choice=="View" :
            read_admin()
        elif admin_choice=="Update" :
            update_admin()
        elif admin_choice=="Delete" :
            delete_admin()

    if choice == "Billing":
        st.subheader("Billing")
        billing_menu=["Add Bill","View Bills","Update Bills","Delete Bills"]
        billing_choice=st.selectbox("Menu",billing_menu)
        if billing_choice=="Add Bill":
            create_bill()
        elif billing_choice=="View Bills" :
            read_bill()
        elif billing_choice=="Update Bills" :
            update_bill()
        elif billing_choice=="Delete Bills" :
            delete_bill()

    if choice == "Tariff":
        st.subheader("Tariff")
        tariff_menu=["Add","View","Update","Delete"]
        tariff_choice=st.selectbox("Menu",tariff_menu)
        if tariff_choice=="Add":
            create_tariff()
        elif tariff_choice=="View" :
            read_tariff()
        elif tariff_choice=="Update" :
            update_tariff()
        elif tariff_choice=="Delete" :
            delete_tariff()

    if choice == "Custom Query":
        st.subheader("Custom Query")
        query=st.text_input("Enter query")
        submit=st.button("Submit")
        if submit:
            mycursor.execute(query)
            myresult = mycursor.fetchall()
            for x in myresult:
                st.write(x)

                
main()