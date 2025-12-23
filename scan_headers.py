import requests

SECURITY_HEADERS = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Strict-Transport-Security",
    "Referrer-Policy"
]

url = input("Enter target URL (with http/https): ")

try:
    r = requests.get(url, timeout=10)
    print("\n[+] Status Code:", r.status_code)
    print("[+] Response Headers:\n")

    headers = r.headers
    for k, v in headers.items():
        print(f"{k}: {v}")

    print("\n[+] Security Header Check:")
    for h in SECURITY_HEADERS:
        if h in headers:
            print(f"[OK] {h} is present")
        else:
            print(f"[WARN] {h} is MISSING")

except Exception as e:
    print("[-] Error:", e)

