import re 
import streamlit as st

#Page Styling
st.set_page_config(
    page_title="Password Strength Checker By Code With Ammar", page_icon="🛅", layout="center")
#Custom CSS
st.markdown("""
<style>
    .main {text-align: center;}
    .stTextInput {width: 60% !important; margin: auto; }
    .stButton button {width: 50%; background-color: #4CAF50; color: white; font-size: 18px; }
    .stButton button:hover { background-color: #45a049;}
</style>
""", unsafe_allow_html=True)

#Page Title and Description
st.title("🔐 Password Strength Generator")
st.write("Enter your  password below to check its security level. 🔎")

# function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1  # increased score by 1
    else:
        feedback.append("❌ Password should be **at least 8 characters long**.")
    if re.search(r'[a-z]', password) and re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("❌ Password should include **atleast both upper case (A-Z) and lower case (a-z) letters** ")
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should contain **at least one number (0-9)**.")

    # Check for Special Characters
    if re.search(r"[!@#$%^&*()_+{}\[\]:;<>,.?~\\]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one special character (e.g., !@#$%^&*()_+{}[]:;<>,.?~-)**.")

    #Display Password Strength
    if score >= 4:
        st.success("✅ **Strong Password** - your password is very strong and secure! 💪")
    elif score == 3:
        st.info("⚠️ **Moderate Password** - Consider adding more characters for better security ⚒️")
    else:
        st.error("❌ **Weak Password** - Please make your password stronger! 💔")

    #Display Feedback
    if feedback:
     with  st.expander("🔄 **Improve Your Password** :"):
         for item in feedback:
             st.write(item)

#Password Input
password = st.text_input("Enter your password here: ", type="password", help="Ensure your password is strong and secure! 🔐")

#Button Working
if st.button("Check Password Strength"):
    if password:
        check_password_strength(password)
    else:
        st.error("🚫  Please enter a password first! ❗") #Show warning if  password is empty


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
        font-size: 18px; /* Bigger Font */
        font-weight: 900; /* Maximum Bold */
    }
    
    .footer b {
        display: inline-block;
        font-size: 20px;
        font-weight: 900;
        animation: gradientText 2s infinite alternate; /* Automatic Animation */
    }
    </style>
    <div class='footer'><b>Developed by ©️CodeWithAmmar</b></div>
    """,
    unsafe_allow_html=True
)
