import streamlit as st
import pandas as pd
import sqlite3

# Database connection
conn = sqlite3.connect('tax_tracking.db')
c = conn.cursor()

# Function to add data to database
def add_income(user, source, amount, date_received):
    c.execute("INSERT INTO Income (user, source, amount, date_received) VALUES (?, ?, ?, ?)",
              (user, source, amount, date_received))
    conn.commit()

def add_deduction(user, deduction_type, amount, date_incurred):
    c.execute("INSERT INTO Deduction (user, deduction_type, amount, date_incurred) VALUES (?, ?, ?, ?)",
              (user, deduction_type, amount, date_incurred))
    conn.commit()

def add_tax_credit(user, credit_type, amount, date_claimed):
    c.execute("INSERT INTO TaxCredit (user, credit_type, amount, date_claimed) VALUES (?, ?, ?, ?)",
              (user, credit_type, amount, date_claimed))
    conn.commit()

# Streamlit UI
st.title("Income and Deduction Tracking")

menu = ["Add Income", "Add Deduction", "Add Tax Credit", "View Summary"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Income":
    st.subheader("Add Income Information")
    user = st.text_input("User Name")
    source = st.text_input("Income Source")
    amount = st.number_input("Amount", min_value=0.0, format="%.2f")
    date_received = st.date_input("Date Received")
    if st.button("Add Income"):
        add_income(user, source, amount, date_received)
        st.success(f"Income from {source} added successfully!")

elif choice == "Add Deduction":
    st.subheader("Add Deduction Information")
    user = st.text_input("User Name")
    deduction_type = st.text_input("Deduction Type")
    amount = st.number_input("Amount", min_value=0.0, format="%.2f")
    date_incurred = st.date_input("Date Incurred")
    if st.button("Add Deduction"):
        add_deduction(user, deduction_type, amount, date_incurred)
        st.success(f"Deduction for {deduction_type} added successfully!")

elif choice == "Add Tax Credit":
    st.subheader("Add Tax Credit Information")
    user = st.text_input("User Name")
    credit_type = st.text_input("Tax Credit Type")
    amount = st.number_input("Amount", min_value=0.0, format="%.2f")
    date_claimed = st.date_input("Date Claimed")
    if st.button("Add Tax Credit"):
        add_tax_credit(user, credit_type, amount, date_claimed)
        st.success(f"Tax Credit for {credit_type} added successfully!")

elif choice == "View Summary":
    st.subheader("Income and Deduction Summary")

    # Display Income
    st.write("### Income")
    income_df = pd.read_sql_query("SELECT * FROM Income", conn)
    st.dataframe(income_df)

    # Display Deductions
    st.write("### Deductions")
    deduction_df = pd.read_sql_query("SELECT * FROM Deduction", conn)
    st.dataframe(deduction_df)

    # Display Tax Credits
    st.write("### Tax Credits")
    tax_credit_df = pd.read_sql_query("SELECT * FROM TaxCredit", conn)
    st.dataframe(tax_credit_df)
