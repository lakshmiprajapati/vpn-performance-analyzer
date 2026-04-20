from ping_test import run_ping
from speed_test import run_speed_test

def run_full_test(label):
    print(f"\n🔍 Running test: {label}\n")

    ping = run_ping()
    speed = run_speed_test()

    return {
        "latency": ping["avg_latency"],
        "packet_loss": ping["packet_loss"],
        "download": speed["download"],
        "upload": speed["upload"]
    }


def compare_results(normal, vpn):
    print("\n📊 COMPARISON RESULTS\n")

    print(f"Latency Change: {vpn['latency']} ms vs {normal['latency']} ms")
    print(f"Download Change: {vpn['download']} Mbps vs {normal['download']} Mbps")
    print(f"Upload Change: {vpn['upload']} Mbps vs {normal['upload']} Mbps")