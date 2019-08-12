IPs:
- Control: 192.168.1.99/24
- Web1: 192.168.1.100/24
- Web2: 192.168.1.101/24

Hyper-V Switches:
- Configure each VM primary NIC To connect to internal switch
- Have secondary NIC connected externally

Every Bootup:
- Must add the SSH fingerprints of the managed nodes; wipe out existing entries
- ssh-keyscan Command and append to ~/.ssh/known_hosts File
