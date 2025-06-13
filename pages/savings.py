import streamlit as st
from savings_account import SavingsAccount

st.set_page_config(page_title = "Savings Account", layout ="centered")

savings = SavingsAccount(200000)

with st.form("savings_form"):
    amount = st.number_input("Enter Amount")
    operations = st.selectbox("Deposit or withdraw",('deposit','withdraw'))
    submit = st.form_submit_button("Submit")

if submit and operations == "withdraw":
    with st.spinner("processing..."):
        if amount <= 5000:
            savings.withdraw(amount)
            st.write(savings.balance)

        elif amount > savings.balance:
            st.write("Insufficient funds")


        else:
            st.write("you have exceeded your limit")
    

    