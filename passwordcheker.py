import re
import streamlit as st

# Page Styling
st.set_page_config(
    page_title="Password Strength Checker By Code With Ammar", 
    page_icon="🛅", 
    layout="centered"
)

# Background Image Setup
background_image = "Capture.PNG"  # Ya "Capture2.PNG" jo bhi aap use karna chahain

st.markdown(
    f"""
    <style>
    .stApp {{
        background: url(data:image/png;base64,{background_image}) no-repeat center center fixed;
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Animated Page Title
st.markdown("<h1 style='text-align: center; color: white;'>🔐 Password Strength Checker</h1>", unsafe_allow_html=True)

# Centered Subtitle
st.markdown(
    "<h4 style='text-align: center; color: white;'>"
    "Enter your password below to check its security level. 🔎"
    "</h4>", 
    unsafe_allow_html=True
)

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1  
    else:
        feedback.append("❌ Password should be **at least 8 characters long**.")
    
    if re.search(r'[a-z]', password) and re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("❌ Password should include **both uppercase (A-Z) and lowercase (a-z) letters**.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should contain **at least one number (0-9)**.")

    if re.search(r"[!@#$%^&*()_+{}\[\]:;<>,.?~\\]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one special character (e.g., !@#$%^&*()_+{}[]:;<>,.?~-)**.")

    if score >= 4:
        st.success("✅ **Strong Password** - Your password is very strong and secure! 💪")
    elif score == 3:
        st.info("⚠️ **Moderate Password** - Consider adding more characters for better security ⚒️")
    else:
        st.error("❌ **Weak Password** - Please make your password stronger! 💔")

    if feedback:
        with st.expander("🔄 **Improve Your Password** :"):
            for item in feedback:
                st.write(item)

# Password Input
password = st.text_input("Enter your password here: ", type="password", help="Ensure your password is strong and secure! 🔐")

# Button Working
if st.button("Check Password Strength"):
    if password:
        check_password_strength(password)
    else:
        st.error("🚫 Please enter a password first! ❗")  

# Footer
st.markdown(
    """
    <style>
    .footer {
        text-align: center;
        margin-top: 50px;
        padding: 20px;
        font-size: 16px;
        font-weight: 900;
        color: white;
    }
    </style>
    <div class='footer'><b>Developed by ©️CodeWithAmmar</b></div>
    """,
    unsafe_allow_html=True
)
