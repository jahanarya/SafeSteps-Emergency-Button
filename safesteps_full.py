import streamlit as st
import datetime
import urllib.parse
import webbrowser

st.set_page_config(page_title="SafeSteps – Women's Safety", page_icon="🛡️", layout="centered")

st.title("🛡️ SafeSteps – Emergency Safety App for Women")
st.markdown("Ensure your safety with just one click – sound alert, live location, and emergency messaging.")

# --- Emergency Alarm ---
st.header("🔊 One-Click Emergency Alarm")
if st.button("Activate Loud Alarm"):
    st.audio("https://www.soundjay.com/button/beep-07.wav", autoplay=True)
    st.warning("🔊 Alarm Activated! Attracting attention...")

# --- Location Sharing ---
st.header("📍 Share Your Live Location")
with st.expander("Send your location to someone you trust"):
    name = st.text_input("Recipient's Name", placeholder="e.g., Mom")
    phone = st.text_input("Recipient's WhatsApp Number", placeholder="e.g., +8801XXXXXXXXX")
    if st.button("Generate WhatsApp Message"):
        message = f"🚨 URGENT: I am in danger. Please help!\nTrack my live location here: https://maps.app.goo.gl/?link\n- Sent via SafeSteps"
        if phone:
            whatsapp_url = f"https://wa.me/{phone}?text={urllib.parse.quote(message)}"
            st.success("✅ Message Ready!")
            st.markdown(f"[📩 Send WhatsApp Message]({whatsapp_url})", unsafe_allow_html=True)

# --- Tips for Safety ---
st.header("💡 Quick Safety Tips")
st.markdown("""
- 🚶 Stay in well-lit areas at night  
- 📱 Keep your phone battery charged  
- 🚕 Avoid unfamiliar routes alone  
- 🧍 Share your ride info with friends  
- ⏰ Set location sharing ON when outside alone
""")

# --- Footer ---
st.markdown("---")
st.markdown("Made with ❤️ by Mimtaj for WICE BD 2025")
