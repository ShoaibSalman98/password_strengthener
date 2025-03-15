import streamlit as st
import re

st.set_page_config(page_title="Make your Password More Secure & Powerful!", page_icon="👨‍✈️")

st.title("🕹️ Password Generator")

st.markdown("""
# Welcome to the Powerful tool to check your password's security 🔎
### Use this powerful app to check your password's vulnerability and make it stronger and safer 👨‍✈️
""")

password = st.text_input("Enter your password", type="password")

feedback = []
score = 0

if password:
    # Check for length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append(" ❌ Password should be at least 8 characters long")

    # Check for upper and lower case letters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append(" ❌ Password should contain both upper and lower case characters")

    # Check for digits or special characters
    if re.search(r'\d', password) or re.search(r'[!@#$%&*]', password):
        score += 1
    else:
        feedback.append(" ❌ Password should contain at least one digit or special character (!@#$%&*).")

    # Password strength feedback
    if score == 3:
        feedback.append(" ✅ Your Password is strong 💪")
    elif score == 2:
        feedback.append(" 🤖 Your password is medium. Make it stronger.")
    else:
        feedback.append(" ⚒️ Your password is vulnerable. Make it stronger.")

    # Display feedback
    if feedback:
        st.markdown("## 📚 Improvement Suggestions ##")
        for tip in feedback:
            st.write(tip)
else:
    st.info("Please enter your password for checking")

        

