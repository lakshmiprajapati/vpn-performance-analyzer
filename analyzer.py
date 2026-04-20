from ping_test import run_ping
from speed_test import run_speed_test
import matplotlib.pyplot as plt

def run_full_test(mode):
    print(f"\n🔍 Running test: {mode}")

    ping_result = run_ping()
    speed_result = run_speed_test()

    return {
        "latency": ping_result["avg_latency"],
        "packet_loss": ping_result["packet_loss"],
        "download": speed_result["download"],
        "upload": speed_result["upload"]
    }


def compare_results(normal, vpn):
    print("\n📊 COMPARISON RESULTS\n")

    print(f"Latency Change: {vpn['latency']:.2f} ms vs {normal['latency']:.2f} ms")
    print(f"Download Change: {vpn['download']:.2f} Mbps vs {normal['download']:.2f} Mbps")
    print(f"Upload Change: {vpn['upload']:.2f} Mbps vs {normal['upload']:.2f} Mbps")


def plot_results(normal, vpn):
    labels = ["Latency (ms)", "Download (Mbps)", "Upload (Mbps)"]

    normal_values = [
        normal["latency"],
        normal["download"],
        normal["upload"]
    ]

    vpn_values = [
        vpn["latency"],
        vpn["download"],
        vpn["upload"]
    ]

    x = range(len(labels))

    plt.figure(figsize=(8, 5))
    plt.bar(x, normal_values, width=0.4, label="Normal", align="center")
    plt.bar([i + 0.4 for i in x], vpn_values, width=0.4, label="VPN", align="center")

    plt.xticks([i + 0.2 for i in x], labels)
    plt.title("VPN vs Normal Performance")
    plt.legend()

    plt.tight_layout()
    plt.show()