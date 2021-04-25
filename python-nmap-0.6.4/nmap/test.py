import nmap3
import json
nmap = nmap3.Nmap()
results = nmap.nmap_version()

print(json.loads(results)["nmap"][1])
 {'nmap': (7, 70), 'compiled_with': ('liblua-5.3.3', 'openssl-1.1.1d', 'libssh2-1.8.0', 'libz-1.2.11', 'libpcre-8.39', 'libpcap-1.8.1', 'nmap-libdnet-1.12', 'ipv6'), 'compiled_without': ('',), 'nsock_engines': ('epoll', 'poll', 'select')}
