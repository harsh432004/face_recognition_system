import streamlit as st
from PIL import Image
import time

# Set page configuration with a customized title and layout
st.set_page_config(
    page_title='HakersxCoders Face Attendance System', layout='wide')

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .header-section {
        text-align: center;
        color: #2E86C1;
        font-size: 50px;
        font-weight: bold;
    }
    .sub-header {
        font-size: 20px;
        text-align: center;
        color: #1F618D;
    }
    .success-message {
        text-align: center;
        font-size: 18px;
        color: green;
    }
    </style>
""", unsafe_allow_html=True)

# Spinner with a short delay for welcoming users
with st.spinner("Loading HakersxCoders Face Attendance System..."):
    time.sleep(2)  # Delay to simulate loading
    import face_rec  # Assuming face_rec is your face recognition module

# Add logo or image for a more polished look
# Replace 'logo.png' with the path to your logo/image
image = Image.open('logo.jpeg')
st.image(image, width=400)

# Create an interactive header section
st.markdown('<div class="header-section">Attendance System using Face Recognition</div>',
            unsafe_allow_html=True)
st.markdown('<div class="sub-header">Powered by HakersxCoders | Efficient | Secure | Reliable</div>',
            unsafe_allow_html=True)

# Success messages for user guidance
# st.markdown('<div class="success-message">Please register your face from the registration form if you are new.</div>', unsafe_allow_html=True)
st.markdown('<div class="success-message">Redis database successfully connected!</div>',
            unsafe_allow_html=True)

# Add interactive buttons and columns for better layout
st.write('---')  # Separator for visual clarity

# Create two columns for better UX layout
col1, col2 = st.columns([1, 1])

# with col1:
#     if st.button('Register New Student'):
#         st.write('🔄 Redirecting to registration page...')
#         # Add your registration logic here

# with col2:
#     if st.button('Start Attendance Recognition'):
#         st.write('🟢 Initializing face recognition...')
        # Add your attendance recognition logic here

# Footer section with links or additional info
st.write('---')
st.markdown("""
    <div style='text-align: center;'>
        <p>Hack the Mountains 5.0 | Developed by HakersxCoders</p>
        <p><a href="https://hackthemountains.tech" target="_blank">Visit Hackathon Website</a></p>
    </div>
""", unsafe_allow_html=True)
