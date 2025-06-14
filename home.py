import streamlit as st
st.set_page_config(page_title = "Bank App", layout="wide")
st.title("DEE'S BANKING SYSTEM")
st.header("Eazy Banking")
st.divider()
st.markdown("<font size='5'>Experience a whole new world of banking,simplified</font>", unsafe_allow_html=True)


col1, col2, col3, col4 = st.columns(4)
with col1:
    st.button("Internet banking")
    st.write()

with col2:
    st.button("Open Account")

with col3:
    st.button("customer support")

with col4:
    st.button("Help")




