import streamlit as st
from analyzer import run_full_test, plot_results

# Page config
st.set_page_config(page_title="VPN Analyzer", layout="wide")

st.title("🚀 VPN Performance Analyzer")
st.markdown("Compare your internet performance with and without VPN")

# Session state
if "normal" not in st.session_state:
    st.session_state.normal = None

if "vpn" not in st.session_state:
    st.session_state.vpn = None


# -----------------------------
# BUTTONS
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    if st.button("🟢 Run WITHOUT VPN"):
        st.session_state.normal = run_full_test("WITHOUT VPN")
        st.success("WITHOUT VPN test completed. Now turn ON VPN.")

with col2:
    if st.button("🔵 Run WITH VPN"):
        st.session_state.vpn = run_full_test("WITH VPN")
        st.success("WITH VPN test completed.")


# -----------------------------
# RESULTS
# -----------------------------
if st.session_state.normal and st.session_state.vpn:

    normal = st.session_state.normal
    vpn = st.session_state.vpn

    st.divider()
    st.subheader("Performance Comparison")

    col1, col2, col3 = st.columns(3)

    # LATENCY
    with col1:
        diff = vpn["latency"] - normal["latency"]

        color = "normal"
        if diff > 0:
            color = "inverse"  # higher latency = bad

        st.metric(
            label="📡 Latency (ms)",
            value=f"{vpn['latency']}",
            delta=f"{diff:.2f}",
            delta_color=color
        )

    # DOWNLOAD
    with col2:
        diff = vpn["download"] - normal["download"]

        color = "normal"
        if diff < 0:
            color = "inverse"  # lower speed = bad

        st.metric(
            label="⬇ Download (Mbps)",
            value=f"{vpn['download']}",
            delta=f"{diff:.2f}",
            delta_color=color
        )

    # UPLOAD
    with col3:
        diff = vpn["upload"] - normal["upload"]

        color = "normal"
        if diff < 0:
            color = "inverse"

        st.metric(
            label="⬆ Upload (Mbps)",
            value=f"{vpn['upload']}",
            delta=f"{diff:.2f}",
            delta_color=color
        )

    # -----------------------------
    # SMART ANALYSIS
    # -----------------------------
    st.divider()
    st.subheader("Analysis")

    latency_diff = vpn["latency"] - normal["latency"]

    if latency_diff > 50:
        st.error("⚠️ VPN significantly increases latency (slower response time)")
    elif latency_diff > 10:
        st.warning("⚠️ VPN slightly increases latency")
    else:
        st.success("✅ VPN has minimal impact on latency")

    if vpn["download"] < normal["download"]:
        st.warning("⬇ Download speed decreased with VPN")
    else:
        st.success("⬇ Download speed stable")

    if vpn["upload"] < normal["upload"]:
        st.warning("⬆ Upload speed decreased with VPN")
    else:
        st.success("⬆ Upload speed stable")

    # -----------------------------
    # RAW DATA
    # -----------------------------
    st.divider()
    with st.expander("View Raw Data"):
        st.write("WITHOUT VPN", normal)
        st.write("WITH VPN", vpn)

    # -----------------------------
    # GRAPH
    # -----------------------------
    st.divider()
    st.subheader("Visualization")

    fig = plot_results(normal, vpn)
    st.pyplot(fig)

    # -----------------------------
    # FINAL CONCLUSION
    # -----------------------------
    st.divider()
    st.subheader("Final Conclusion")

    st.info("""
Using a VPN improves privacy and security, but may impact performance.

In this test:
- Latency increased due to encryption and longer routing paths
- Speed may decrease depending on server and network conditions

This demonstrates the trade-off between **privacy and performance** in real-world networking.
""")