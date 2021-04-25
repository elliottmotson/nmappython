import nmap3
import json
nmap = nmap3.Nmap()
results = nmap.nmap_version()

print(json.dumps(results))
