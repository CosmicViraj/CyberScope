import matplotlib.pyplot as plt

def plot_ports_vs_risk(results):
    ports = []
    risks = []

    for port, _, state in results:
        if state == "open":
            ports.append(port)
            risks.append(10 if port in [21,23,3389] else 5)

    plt.bar(ports, risks)
    plt.xlabel("Ports")
    plt.ylabel("Risk Score")
    plt.title("Ports vs Risk")
    plt.show()
