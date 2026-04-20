import speedtest

def run_speed_test():
    st = speedtest.Speedtest()

    st.get_best_server()

    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000

    return {
        "download": round(download_speed, 2),
        "upload": round(upload_speed, 2)
    }