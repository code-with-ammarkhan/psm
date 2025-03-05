import re
import streamlit as st
import base64

# Set Page Configuration
st.set_page_config(
    page_title="Password Strength Checker By Code With Ammar",
    page_icon="🔐",
    layout="centered"
)

# Function to Convert Image to Base64
def get_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Path of Uploaded Image
image_path = "/mnt/data/A_high-tech_abstract_background_featuring_a_glowin.png"

# Encode Image to Base64
image_base64 = get_base64(image_path)

# Custom CSS for Background Image
page_bg_img = f"""
<style>
    .stApp {{
        background-image: url("data:image/png;base64,{image_base64}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    @keyframes moveText {{
        0% {{ transform: translateX(-10px); }}
        50% {{ transform: translateX(10px); }}
        100% {{ transform: translateX(-10px); }}
    }}
    .animated-heading {{
        text-align: center;
        font-size: 32px;
        font-weight: bold;
        animation: moveText 2s infinite alternate ease-in-out;
        color: white;
    }}
    .stTextInput {{
        width: 60% !important;
        margin: auto;
    }}
    .stButton button {{
        width: 50%;
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
    }}
    .stButton button:hover {{
        background-color: #45a049;
    }}
</style>
"""

# Apply Background Image
st.markdown(page_bg_img, unsafe_allow_html=True)

# Animated Title
st.markdown("<h1 class='animated-heading'>🔐 Password Strength Checker</h1>", unsafe_allow_html=True)

# Subtitle
st.markdown(
    "<h4 style='text-align: center; font-size: 18px; font-weight: bold; color: white;'>"
    "Enter your password below to check its security level. 🔎"
    "</h4>", 
    unsafe_allow_html=True
)

# Function to Check Password Strength
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

# Password Input Field
password = st.text_input("Enter your password here: ", type="password", help="Ensure your password is strong and secure! 🔐")

# Button to Check Password Strength
if st.button("Check Password Strength"):
    if password:
        check_password_strength(password)
    else:
        st.error("🚫 Please enter a password first! ❗")  

# Footer
st.markdown(
    """
    <style>
    @keyframes gradientText {
        0% { color: rgb(148, 11, 98); }
        100% { color: #00c9ff; }
    }
    
    .footer {
        text-align: center;
        margin-top: 50px;
        padding: 20px;
        font-size: 18px;
        font-weight: 900;
        color: white;
    }
    
    .footer b {
        display: inline-block;
        font-size: 20px;
        font-weight: 900;
        animation: gradientText 2s infinite alternate;
    }
    </style>
    <div class='footer'><b>Developed by ©️CodeWithAmmar</b></div>
    """,
    unsafe_allow_html=True
)
