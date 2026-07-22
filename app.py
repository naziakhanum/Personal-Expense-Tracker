import streamlit as st
from datetime import datetime

st.title("💰 Personal Expense Tracker")

expense = st.text_input("Expense Name")
amount = st.number_input("Amount", min_value=0.0)
category = st.text_input("Category")

if st.button("Save Expense"):
    date = datetime.now().strftime("%d-%m-%Y")

    with open("expenses.txt", "a") as file:
        file.write(f"{expense},{amount},{category},{date}\n")
    st.success("Expense Saved Successfully!")
st.subheader("📋 Saved Expenses")

try:
    with open("expenses.txt", "r") as file:
        for expense in file:
            st.write(expense.strip())
except FileNotFoundError:
    st.write("No expenses found.")

st.subheader("🔍 Search Expense")

search = st.text_input("Enter Expense Name to Search")

if search:
    found = False

    with open("expenses.txt", "r") as file:
        for expense in file:
            if search.lower() in expense.lower():
                st.success(expense.strip())
                found = True

    if not found:
        st.error("Expense Not Found")

st.subheader("🗑️ Delete Expense")

delete_name = st.text_input("Enter Expense Name to Delete")

if st.button("Delete Expense"):
    new_data = []
    deleted = False

    with open("expenses.txt", "r") as file:
        expenses = file.readlines()

    for expense in expenses:
        if delete_name.lower() not in expense.lower():
            new_data.append(expense)
        else:
            deleted = True

    with open("expenses.txt", "w") as file:
        file.writelines(new_data)

    if deleted:
        st.success("Expense Deleted Successfully!")
    else:
        st.error("Expense Not Found!")