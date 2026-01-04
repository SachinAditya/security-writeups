import requests

ZAP_API_URL = "http://localhost:8080"
API_KEY = ""  # Add your ZAP API key here if enabled

SECURITY_HEADER_KEYWORDS = [
    "Content Security Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Strict-Transport-Security",
    "Referrer-Policy"
]

def fetch_alerts():
    """
    Fetch alerts from OWASP ZAP using the ZAP API.
    """
    endpoint = f"{ZAP_API_URL}/JSON/core/view/alerts/"
    params = {"apikey": API_KEY} if API_KEY else {}

    response = requests.get(endpoint, params=params, timeout=10)
    response.raise_for_status()
    return response.json().get("alerts", [])

def show_missing_header_alerts(alerts):
    """
    Filter and display alerts related to missing security headers.
    """
    print("\n[+] Checking for missing security header alerts...\n")
    found = False

    for alert in alerts:
        alert_name = alert.get("alert", "")
        url = alert.get("url", "")

        for keyword in SECURITY_HEADER_KEYWORDS:
            if keyword.lower() in alert_name.lower():
                print(f"[WARN] {alert_name}")
                print(f"       URL: {url}\n")
                found = True

    if not found:
        print("[OK] No missing security header alerts found.")

if __name__ == "__main__":
    try:
        alerts = fetch_alerts()
        show_missing_header_alerts(alerts)
    except Exception as err:
        print("[-] Error communicating with OWASP ZAP:", err)
