import whois

# We are checking if the domain exists
def is_registered (domain_name):
    try:
        w = whois.whois(domain_name)
    except Exception:
        return False
    else:
        return bool(w.domain_name)

if __name__ == "__main__" :
    print(is_registered("githinji.dev"))