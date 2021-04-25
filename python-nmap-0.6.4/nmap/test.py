import nmap3
nmap = nmap3.Nmap()
results = nmap.nmap_version()

print(json.dumps(results))
