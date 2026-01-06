import tkinter as tk
from core.nmap_scan import nmap_scan
from core.risk_engine import calculate_risk
from core.cve_lookup import lookup_cve
from core.history_manager import save_history
from core.report_pdf import generate_pdf
from gui.graphs import plot_ports_vs_risk

def run_scan():
    target = entry.get()
    output.delete(1.0, tk.END)

    results = nmap_scan(target)
    risk = calculate_risk(results)
    save_history(target, risk)

    output.insert(tk.END, f"Target: {target}\n")
    output.insert(tk.END, f"Risk Level: {risk}\n\n")

    for port, service, state in results:
        output.insert(tk.END, f"{port} | {service} | {state}\n")
        for cve in lookup_cve(service):
            output.insert(tk.END, f"   ⚠ {cve}\n")

    plot_ports_vs_risk(results)
    generate_pdf(target, results, risk)

app = tk.Tk()
app.title("CyberScope – SOC Dashboard")
app.geometry("800x550")

tk.Label(app, text="Authorized Target").pack()
entry = tk.Entry(app, width=40)
entry.pack()

tk.Button(app, text="Run Scan", command=run_scan).pack(pady=10)

output = tk.Text(app)
output.pack(expand=True, fill="both")

app.mainloop()
