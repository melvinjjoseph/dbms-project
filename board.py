import streamlit as st
from database import *

def create_eb():
    name=st.text_input("Enter Board name")
    city=st.text_input("Enter Board City")
    state=st.selectbox("Select state",["","Karnataka","Tamil Nadu","Kerala","Andhra Pradesh","Telangana","Maharashtra","Goa","Gujarat","Rajasthan","Uttar Pradesh","Madhya Pradesh","Bihar","Jharkhand","Odisha","West Bengal","Assam","Arunachal Pradesh","Manipur","Meghalaya","Mizoram","Nagaland","Sikkim","Tripura","Himachal Pradesh","Punjab","Haryana","Uttarakhand","Jammu and Kashmir","Chhattisgarh","Uttarakhand","Delhi","Puducherry","Chandigarh","Dadra and Nagar Haveli and Daman and Diu","Ladakh","Andaman and Nicobar Islands","Lakshadweep"])
    submit=st.button("Submit")
    if submit:
        eb_id=add_eb(name,city,state) 
        st.write("Electricity board id is ",eb_id)
        st.write ("Electricity board added successfully")
    
def update_eb():
    st.write("Select electricity board id to update")
    eb_id=st.number_input("Enter electricity board id",min_value=1,step=1)
    name=st.text_input("Enter board name")
    city=st.text_input("Enter board city")
    state=st.selectbox("Select state",["","Karnataka","Tamil Nadu","Kerala","Andhra Pradesh","Telangana","Maharashtra","Goa","Gujarat","Rajasthan","Uttar Pradesh","Madhya Pradesh","Bihar","Jharkhand","Odisha","West Bengal","Assam","Arunachal Pradesh","Manipur","Meghalaya","Mizoram","Nagaland","Sikkim","Tripura","Himachal Pradesh","Punjab","Haryana","Uttarakhand","Jammu and Kashmir","Chhattisgarh","Uttarakhand","Delhi","Puducherry","Chandigarh","Dadra and Nagar Haveli and Daman and Diu","Ladakh","Andaman and Nicobar Islands","Lakshadweep"])
    submit=st.button("Submit")

    # check if electricity board id exists in database
    mycursor.execute("SELECT * FROM Board WHERE eb_id = %s", (eb_id,))
    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        st.write("Electricity board id does not exist")
        return 
    elif submit and len(myresult) > 0:
        update_eb_db(eb_id,name,city,state)

def delete_eb():
    eb_id=st.number_input("Enter electricity board id",min_value=1,step=1)
    # check if electricity board id exists in database
    mycursor.execute("SELECT * FROM Board WHERE eb_id = %s", (eb_id,))
    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        st.write("Electricity board id does not exist")
        return
    submit=st.button("Submit")
    if submit and len(myresult) > 0:
        delete_eb_db(eb_id)
    