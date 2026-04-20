from ping_test import run_ping
from speed_test import run_speed_test

print("🚀 Running Ping Test...\n")
ping_result = run_ping()

print(f"📡 Avg Latency: {ping_result['avg_latency']} ms")
print(f"📉 Packet Loss: {ping_result['packet_loss']} %\n")

print("⚡ Running Speed Test...\n")
speed_result = run_speed_test()

print(f"⬇ Download Speed: {speed_result['download']} Mbps")
print(f"⬆ Upload Speed: {speed_result['upload']} Mbps")