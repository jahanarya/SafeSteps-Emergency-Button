
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="SafeSteps - Women Safety App", layout="centered")
st.title("🛡️ SafeSteps – Emergency Alert App")

st.markdown("""
Welcome to **SafeSteps** – a safety app designed for women in danger.  
Press the **SOS** button below to send an alert to your trusted contact with your location and time.
""")

if st.button("🚨 EMERGENCY SOS"):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    alert_message = f""" 
    **🚨 ALERT SENT!**  
    _Help me, I am in danger!_  
    📍 **Location**: https://maps.google.com/?q=23.8103,90.4125 *(example)*  
    🕒 **Time**: {current_time}  
    📱 **Sent to**: Mom (+8801XXXXXXXXX)
    """
    st.markdown(alert_message)

st.markdown("---")
st.markdown("🔒 This is a demo version. Actual SMS and location tracking to be added in the full version.")
