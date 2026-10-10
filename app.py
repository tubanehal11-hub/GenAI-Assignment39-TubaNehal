
import streamlit as st

st.set_page_config(
    page_title="GenAI App",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 GenAI Application Deployment")
st.write("Welcome to my GenAI application!")

st.subheader("Text Assistant")
user_input = st.text_area("Enter your text or question:")

if st.button("Submit"):
    if user_input.strip():
        st.write("### Your Input")
        st.write(user_input)
        st.success("Your application is running successfully!")
    else:
        st.warning("Please enter some text first.")

st.divider()
st.caption("Created for GenAI Assignment 39")
