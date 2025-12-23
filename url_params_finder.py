from urllib.parse import urlparse, parse_qs

url = input("Enter URL with parameters: ")

parsed = urlparse(url)
params = parse_qs(parsed.query)

if params:
    print("\n[+] Parameters found:")
    for k, v in params.items():
        print(f"{k} = {v}")
else:
    print("[-] No parameters found in the URL.")
