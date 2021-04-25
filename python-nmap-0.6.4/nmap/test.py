import nmap3
import json
nmap = nmap3.Nmap()
results = nmap.nmap_version()
parse = json.loads(results)
print(results['service']['ostype'])
