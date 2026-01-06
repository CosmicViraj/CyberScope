import nmap

def nmap_scan(target):
    nm = nmap.PortScanner()
    nm.scan(target, arguments="-T4 -F")

    results = []
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            for port in nm[host][proto]:
                service = nm[host][proto][port]["name"]
                state = nm[host][proto][port]["state"]
                results.append((port, service, state))
    return results
