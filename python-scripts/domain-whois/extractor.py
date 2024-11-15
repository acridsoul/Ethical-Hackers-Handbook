import whois

from validator import is_registered
domain_name= "githinji.dev"

if is_registered(domain_name):
    info = whois.whois(domain_name)
    print("Domain registrar:" ,info.registrar)
    print("Domain Server:" ,info.whois_server)
    print("Creation Date:" ,info.creation_date)
    print("Expiration Date :" ,info.expiration_date)
    print("Name Servers :" ,info.name_servers)