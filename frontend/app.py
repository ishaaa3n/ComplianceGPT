import os
import requests
import streamlit as st

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

st.set_page_config(
    page_title="ComplianceGPT",
    page_icon="📘",
    layout="centered"
)

st.title("📘 ComplianceGPT")
st.caption("AI-powered compliance co-pilot for CA firms")

st.divider()

# ── Backend connection check ──
st.subheader("System Status")

try:
    response = requests.get(f"{BACKEND_URL}/health", timeout=5)
    data = response.json()

    if data["status"] == "ok":
        st.success("✅ Backend is reachable")
        st.json(data)
    else:
        st.warning("⚠️ Backend responded but status is not ok")

except requests.exceptions.ConnectionError:
    st.error("❌ Cannot reach backend. Is it running?")
except Exception as e:
    st.error(f"Unexpected error: {e}")

st.divider()
st.info("Base scaffold is live. Start building features on top of this.")

# ── Future pages will be added here as the project grows ──
