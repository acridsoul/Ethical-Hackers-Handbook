import whois

from validator import is_registered
domain_name= "githinji.dev"

if is_registered(domain_name):
    info = whois.whois(domain_name)
    print("Domain registrar:" ,info.registrar)
    print("Domain registrar:" ,info.whois_server)
    print("Domain registrar:" ,info.creation_date)
    print("Domain registrar:" ,info.expiration_date)
    print(info)