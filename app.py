import streamlit as st
from analyzer import run_full_test
import pandas as pd
import matplotlib.pyplot as plt

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="VPN Analyzer", layout="wide")

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>
body {
    background-color: #0f172a;
    color: white;
}

.big-title {
    font-size: 42px;
    font-weight: bold;
}

.card {
    background: linear-gradient(135deg, #1e293b, #0f172a);
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 0px 15px rgba(0,0,0,0.3);
}

.metric {
    font-size: 28px;
    font-weight: bold;
}

.good { color: #22c55e; }
.bad { color: #ef4444; }

</style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------
st.markdown('<div class="big-title">🚀 VPN Performance Analyzer</div>', unsafe_allow_html=True)
st.write("Compare your internet performance with and without VPN")

# ------------------ SESSION ------------------
if "normal" not in st.session_state:
    st.session_state.normal = None
if "vpn" not in st.session_state:
    st.session_state.vpn = None

# ------------------ BUTTONS ------------------
col1, col2 = st.columns(2)

with col1:
    if st.button("🟢 Run WITHOUT VPN"):
        st.session_state.normal = run_full_test("WITHOUT VPN")
        st.success("Test without VPN completed")

with col2:
    if st.button("🔵 Run WITH VPN"):
        st.session_state.vpn = run_full_test("WITH VPN")
        st.success("Test with VPN completed")

# ------------------ RESULTS ------------------
if st.session_state.normal and st.session_state.vpn:

    normal = st.session_state.normal
    vpn = st.session_state.vpn

    st.markdown("---")
    st.subheader("📊 Performance Comparison")

    col1, col2, col3 = st.columns(3)

    # LATENCY
    with col1:
        diff = vpn["latency"] - normal["latency"]
        color = "bad" if diff > 0 else "good"
        st.markdown(f"""
        <div class="card">
            <div>📶 Latency (ms)</div>
            <div class="metric">{vpn["latency"]:.2f}</div>
            <div class="{color}">{"↑" if diff>0 else "↓"} {abs(diff):.2f}</div>
        </div>
        """, unsafe_allow_html=True)

    # DOWNLOAD
    with col2:
        diff = vpn["download"] - normal["download"]
        color = "good" if diff > 0 else "bad"
        st.markdown(f"""
        <div class="card">
            <div>⬇ Download (Mbps)</div>
            <div class="metric">{vpn["download"]:.2f}</div>
            <div class="{color}">{"↑" if diff>0 else "↓"} {abs(diff):.2f}</div>
        </div>
        """, unsafe_allow_html=True)

    # UPLOAD
    with col3:
        diff = vpn["upload"] - normal["upload"]
        color = "good" if diff > 0 else "bad"
        st.markdown(f"""
        <div class="card">
            <div>⬆ Upload (Mbps)</div>
            <div class="metric">{vpn["upload"]:.2f}</div>
            <div class="{color}">{"↑" if diff>0 else "↓"} {abs(diff):.2f}</div>
        </div>
        """, unsafe_allow_html=True)

    # ------------------ GRAPH ------------------
    st.markdown("---")
    st.subheader("📈 Visualization")

    data = pd.DataFrame({
        "Metric": ["Latency", "Download", "Upload"],
        "Normal": [normal["latency"], normal["download"], normal["upload"]],
        "VPN": [vpn["latency"], vpn["download"], vpn["upload"]]
    })

    fig, ax = plt.subplots()
    data.set_index("Metric").plot(kind="bar", ax=ax)
    st.pyplot(fig)

    # ------------------ INSIGHTS ------------------
    st.markdown("---")
    st.subheader("🧠 Smart Analysis")

    if vpn["latency"] > normal["latency"]:
        st.warning("⚠️ VPN increases latency (expected due to routing)")

    if vpn["download"] < normal["download"]:
        st.warning("⚠️ Download speed reduced")

    if vpn["upload"] < normal["upload"]:
        st.warning("⚠️ Upload speed reduced")

    if vpn["download"] >= normal["download"]:
        st.success("✅ Download speed stable")

    if vpn["upload"] >= normal["upload"]:
        st.success("✅ Upload speed stable")

    # ------------------ FINAL CONCLUSION ------------------
    st.markdown("---")
    st.subheader("📌 Final Conclusion")

    st.info("""
Using a VPN improves privacy and security, but may affect speed.

• Latency usually increases  
• Speed may decrease depending on server  
• Trade-off: Privacy vs Performance  
""")

    # ------------------ RAW DATA ------------------
    with st.expander("🔍 View Raw Data"):
        st.json({"WITHOUT VPN": normal, "WITH VPN": vpn})