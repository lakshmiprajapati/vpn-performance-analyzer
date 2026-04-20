from analyzer import run_full_test, compare_results
from analyzer import run_full_test, compare_results, plot_results

print("🚀 VPN Performance Analyzer\n")

input("👉 Make sure VPN is OFF, then press ENTER...")

normal = run_full_test("WITHOUT VPN")

input("\n👉 Now turn ON VPN, then press ENTER...")

vpn = run_full_test("WITH VPN")

compare_results(normal, vpn)

compare_results(normal, vpn)

plot_results(normal, vpn)