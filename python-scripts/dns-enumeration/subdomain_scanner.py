import requests

domain = input("Enter Domain: ").strip()

# Read subdomains from file
with open("subdomains-100.txt") as file:
    subdomains = file.read().splitlines()

discovered_subdomains = []

# Loop through subdomains
for subdomain in subdomains:
    url = f"http://{subdomain}.{domain}"  # Removed the extra space
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            print("[+] Discovered subdomain:", url)
            discovered_subdomains.append(url)
    except requests.RequestException as e:  # Catch all request-related exceptions
        pass

# Save results to a file
if discovered_subdomains:
    with open("discovered_subdomains.txt", "w") as f:
        for subdomain in discovered_subdomains:
            print(subdomain, file=f)
    print(f"\nDiscovered subdomains saved to 'discovered_subdomains.txt'.")
else:
    print("\nNo subdomains discovered.")
