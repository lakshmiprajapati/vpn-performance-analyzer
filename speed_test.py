import speedtest

def run_speed_test():
    try:
        st = speedtest.Speedtest()

        st.get_best_server()

        download = st.download() / 1_000_000
        upload = st.upload() / 1_000_000

        return {
            "download": round(download, 2),
            "upload": round(upload, 2)
        }

    except Exception as e:
        print("⚠️ Speed test failed, using fallback...")

        return {
            "download": 0,
            "upload": 0
        }