from ping_test import run_ping

print("🚀 Running Ping Test...\n")

result = run_ping()

print(f"📡 Avg Latency: {result['avg_latency']} ms")
print(f"📉 Packet Loss: {result['packet_loss']} %")