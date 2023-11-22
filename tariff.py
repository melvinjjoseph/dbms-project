import streamlit as st
from database import *

def create_tariff():
    tariff_type=st.text_input("Enter tariff_type")
    tariff_cost=st.text_input("Enter tariff_cost")
    submit=st.button("Submit")
    if submit:
        tariff_id=add_tariff(tariff_type,tariff_cost) 
        st.write("Tariff id is ",tariff_id)
        st.write ("Tariff added successfully")

def update_tariff():
    tariff_id=st.text_input("Enter tariff_id")
    tariff_type=st.text_input("Enter tariff_type")
    tariff_cost=st.text_input("Enter tariff_cost")
    submit=st.button("Submit")
    #check if tariff_id exists
    mycursor.execute("SELECT * FROM tariff WHERE tariff_id = %s",(tariff_id,))
    myresult = mycursor.fetchall()
    if not myresult:
        st.write("tariff_id does not exist")
        return
    elif submit and myresult:
        update_tariff_db(tariff_id,tariff_type,tariff_cost)

def delete_tariff():
    tariff_id=st.text_input("Enter tariff_id")
    submit=st.button("Submit")
    #check if tariff_id exists
    mycursor.execute("SELECT * FROM tariff WHERE tariff_id = %s",(tariff_id,))
    myresult = mycursor.fetchall()
    if not myresult:
        st.write("tariff_id does not exist")
        return
    elif submit and myresult:
        delete_tariff_db(tariff_id)