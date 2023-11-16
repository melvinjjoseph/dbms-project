import streamlit as st
from database import *

def create_bill():
    cust_id=st.text_input("Enter cust_id")
    meter_no=st.text_input("Enter meter_no")
    units=st.text_input("Enter units")
    cost_per_unit=st.text_input("Enter cost_per_unit")
    due_date=st.date_input("Enter due_date")
    submit=st.button("Submit", key="create_bill")
    #check if cust_id exists
    mycursor.execute("SELECT * FROM customer WHERE cust_id = %s",(cust_id,))
    myresult = mycursor.fetchall()
    if not myresult:
        st.write("cust_id does not exist")
        return
    if submit:
        bill_id=add_bill(cust_id,meter_no,units,cost_per_unit, due_date) 
        st.write("Bill id is ",bill_id)

def due_bills():
    mycursor.execute("DROP TABLE IF EXISTS due_bills")
    mycursor.execute("CREATE TABLE IF NOT EXISTS due_bills (bill_id INT NOT NULL, cust_id INT NOT NULL, meter_no INT NOT NULL, units INT NOT NULL, cost_per_unit INT NOT NULL, amount INT NOT NULL, due_date DATE NOT NULL, FOREIGN KEY (cust_id) REFERENCES customer(cust_id))")
    mycursor.execute("SELECT * FROM bill WHERE due_date < CURDATE()")
    myresult = mycursor.fetchall()
    if not myresult:
        st.write("No due bills")
        return
    else:
        for x in myresult:
            bill_id=x[0]
            cust_id=x[1]
            meter_no=x[2]
            units=x[3]
            cost_per_unit=x[4]
            amount=x[5]
            due_date=x[6]
            sql = "INSERT INTO due_bills (bill_id, cust_id, meter_no, units, cost_per_unit, amount, due_date) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (bill_id, cust_id, meter_no, units, cost_per_unit, amount, due_date)
            mycursor.execute(sql, val)
            mydb.commit()
        mycursor.execute("SELECT * FROM due_bills")
        myresult = mycursor.fetchall()
        df=pd.DataFrame(myresult,columns=['cust_id','meter_no','units','cost_per_unit','amount','due_date'])
        st.dataframe(df)



def update_bill():
    bill_id=st.text_input("Enter bill_id")
    cust_id=st.text_input("Enter cust_id")
    meter_no=st.text_input("Enter meter_no")
    units=st.text_input("Enter units")
    cost_per_unit=st.text_input("Enter cost_per_unit")
    due_date=st.date_input("Enter due_date")
    submit=st.button("Submit", key="update_bill")
    #check if bill_id exists
    mycursor.execute("SELECT * FROM bill WHERE bill_id = %s",(bill_id,))
    myresult = mycursor.fetchall()
    if not myresult:
        st.write("bill_id does not exist")
        return
    elif submit and myresult:
        update_bill_db(bill_id,cust_id,meter_no,units,cost_per_unit, due_date)

def delete_bill():
    bill_id=st.text_input("Enter bill_id")
    submit=st.button("Submit", key="delete_bill")
    #check if bill_id exists
    if submit:
        delete_bill_db(bill_id)

def due_bill():
    #use trigger to check if bill is due from bill table 
    #if due, add to due_bills table
    mycursor.execute("CREATE TABLE IF NOT EXISTS due_bills (cust_id INT NOT NULL, meter_no INT NOT NULL, units INT NOT NULL, cost_per_unit INT NOT NULL, amount INT NOT NULL, due_date DATE NOT NULL, FOREIGN KEY (cust_id) REFERENCES customer(cust_id))")
    mycursor.execute("CREATE TRIGGER IF NOT EXIST due_bills_trigger AFTER UPDATE ON bill FOR EACH ROW BEGIN IF NEW.due_date < CURDATE() THEN INSERT INTO due_bills (cust_id, meter_no, units, cost_per_unit, amount, due_date) VALUES (NEW.cust_id, NEW.meter_no, NEW.units, NEW.cost_per_unit, NEW.amount, NEW.due_date); END IF; END;")
    mycursor.execute("SELECT * FROM due_bills")
    myresult = mycursor.fetchall()
    df=pd.DataFrame(myresult,columns=['cust_id','meter_no','units','cost_per_unit','amount','due_date'])
    st.dataframe(df)



