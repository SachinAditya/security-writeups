import requests

url = input("Enter target URL (with http/https): ")

try:
    r = requests.get(url, timeout=10)
    print("\n[+] Status Code:", r.status_code)
    print("[+] Response Headers:\n")

    for k, v in r.headers.items():
        print(f"{k}: {v}")

except Exception as e:
    print("[-] Error:", e)
