from pythonping import ping

def run_ping(host="8.8.8.8", count=5):
    response = ping(host, count=count)

    latencies = [r.time_elapsed_ms for r in response]

    avg_latency = sum(latencies) / len(latencies)

    packet_loss = (response.packet_loss * 100)

    return {
        "avg_latency": round(avg_latency, 2),
        "packet_loss": packet_loss,
        "details": str(response)
    }