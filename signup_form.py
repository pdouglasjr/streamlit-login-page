import streamlit as st
import streamlit_authenticator as stauth
from streamlit_authenticator.utilities.hasher import Hasher

# signup form
signup_form = st.form(key="signup_form")

with signup_form:
    name = st.text_input("Name")
    email = st.text_input("Email Address:")
    password = st.text_input("Password:", type="password")
    
    # hash password
    hashed_password = Hasher.hash(password)

    # submit form
    if st.form_submit_button("Sign Up"):
        st.text(f'Email: {email}')
        st.text(f'Password: {hashed_password}')