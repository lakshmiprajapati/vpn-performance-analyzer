from ping_test import run_ping
from speed_test import run_speed_test
import matplotlib.pyplot as plt
import numpy as np


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


def plot_results(normal, vpn):
    labels = ['Latency (ms)', 'Download (Mbps)', 'Upload (Mbps)']

    normal_values = [
        normal['latency'],
        normal['download'],
        normal['upload']
    ]

    vpn_values = [
        vpn['latency'],
        vpn['download'],
        vpn['upload']
    ]

    x = np.arange(len(labels))
    width = 0.35

    plt.figure()

    plt.bar(x - width/2, normal_values, width)
    plt.bar(x + width/2, vpn_values, width)

    plt.xticks(x, labels)
    plt.title("VPN vs Normal Performance")
    plt.legend(['Normal', 'VPN'])

    return plt