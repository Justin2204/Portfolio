# b25-threat-intel.py — VirusTotal Threat Intelligence Module
# CITS2006 Portfolio — B25 | Justin Roy | 23472969

import requests
import json

API_KEY = "YOUR_API_KEY_HERE"
HEADERS = {"x-apikey": API_KEY}
BASE = "https://www.virustotal.com/api/v3"


def check_url(url):
    """Submit a URL to VirusTotal and return reputation stats."""
    print(f"\n[*] Checking URL: {url}")

    # Step 1: Submit URL for analysis
    response = requests.post(f"{BASE}/urls", headers=HEADERS, data={"url": url})
    if response.status_code != 200:
        print(f"    [!] Submission failed: {response.status_code}")
        return None

    analysis_id = response.json()["data"]["id"]

    # Step 2: Retrieve analysis results
    result = requests.get(f"{BASE}/analyses/{analysis_id}", headers=HEADERS)
    stats = result.json()["data"]["attributes"]["stats"]

    print(f"    Malicious  : {stats['malicious']}")
    print(f"    Suspicious : {stats['suspicious']}")
    print(f"    Harmless   : {stats['harmless']}")
    print(f"    Undetected : {stats['undetected']}")

    if stats["malicious"] > 0:
        print(f"    [!] VERDICT: MALICIOUS — flagged by {stats['malicious']} vendor(s)")
    elif stats["suspicious"] > 0:
        print(f"    [!] VERDICT: SUSPICIOUS — flagged by {stats['suspicious']} vendor(s)")
    else:
        print(f"    [+] VERDICT: CLEAN")

    return stats


def check_ip(ip):
    """Query VirusTotal for the reputation of an IP address."""
    print(f"\n[*] Checking IP: {ip}")

    response = requests.get(f"{BASE}/ip_addresses/{ip}", headers=HEADERS)
    if response.status_code != 200:
        print(f"    [!] Lookup failed: {response.status_code}")
        return None

    attributes = response.json()["data"]["attributes"]
    stats = attributes.get("last_analysis_stats", {})
    country = attributes.get("country", "Unknown")
    owner = attributes.get("as_owner", "Unknown")

    print(f"    Country    : {country}")
    print(f"    Owner      : {owner}")
    print(f"    Malicious  : {stats.get('malicious', 0)}")
    print(f"    Suspicious : {stats.get('suspicious', 0)}")
    print(f"    Harmless   : {stats.get('harmless', 0)}")

    if stats.get("malicious", 0) > 0:
        print(f"    [!] VERDICT: MALICIOUS — flagged by {stats['malicious']} vendor(s)")
    else:
        print(f"    [+] VERDICT: CLEAN")

    return stats


# === Run the module ===
print("=" * 45)
print("  Threat Intelligence Report — VirusTotal")
print("=" * 45)

check_url("https://www.google.com")
check_url("http://testsafebrowsing.appspot.com/s/phishing.html")

check_ip("8.8.8.8")
check_ip("185.220.101.45")

print("\n" + "=" * 45)
print("  Scan complete.")
print("=" * 45)
