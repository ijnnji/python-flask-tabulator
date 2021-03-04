import ipaddress

this_ip = "8.8.8.8"
try:
    ip = ipaddress.ip_address(unicode(this_ip))
    print(1)
except ValueError:
    print(0)
