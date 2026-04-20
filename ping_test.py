import subprocess
import re
import platform

def run_ping(host="google.com", count=4):
    try:
        # Detect OS
        param = "-n" if platform.system().lower() == "windows" else "-c"

        command = ["ping", param, str(count), host]

        output = subprocess.check_output(
            command,
            stderr=subprocess.STDOUT,
            universal_newlines=True
        )

        # Extract average latency (works for Linux)
        match = re.search(r"= .*?/([0-9.]+)/", output)

        if match:
            avg_latency = float(match.group(1))
        else:
            avg_latency = 0

        # Extract packet loss
        loss_match = re.search(r"(\d+)% packet loss", output)
        packet_loss = float(loss_match.group(1)) if loss_match else 0

        return {
            "avg_latency": avg_latency,
            "packet_loss": packet_loss
        }

    except Exception as e:
        print("Ping failed:", e)
        return {
            "avg_latency": 0,
            "packet_loss": 100
        }