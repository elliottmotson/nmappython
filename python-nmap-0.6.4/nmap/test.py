import nmap3
import json
nmap = nmap3.Nmap()
parse = json.dumps(nmap.nmap_version())
print(parse['service']['ostype'])
