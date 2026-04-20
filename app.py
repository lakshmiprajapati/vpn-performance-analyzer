import streamlit as st
from analyzer import run_full_test, plot_results

st.title("🚀 VPN Performance Analyzer")

# Store results
if "normal" not in st.session_state:
    st.session_state.normal = None

if "vpn" not in st.session_state:
    st.session_state.vpn = None


# Step 1: WITHOUT VPN
if st.button("Run Test WITHOUT VPN"):
    st.session_state.normal = run_full_test("WITHOUT VPN")
    st.success("✅ WITHOUT VPN test completed. Now turn ON VPN.")


# Step 2: WITH VPN
if st.button("Run Test WITH VPN"):
    st.session_state.vpn = run_full_test("WITH VPN")
    st.success("✅ WITH VPN test completed.")


# Show results
if st.session_state.normal and st.session_state.vpn:
    st.subheader("📊 Results")

    st.write("### WITHOUT VPN")
    st.write(st.session_state.normal)

    st.write("### WITH VPN")
    st.write(st.session_state.vpn)

    plot_results(st.session_state.normal, st.session_state.vpn)