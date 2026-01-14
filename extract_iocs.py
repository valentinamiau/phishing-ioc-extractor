import re

def extract_iocs(text):
    """
    Extract URLs, domains, and IP addresses from text.
    """
    urls = re.findall(r'https?://[^\s]+', text)
    ips = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', text)

    domains = []
    for url in urls:
        domain = re.sub(r'https?://', '', url)
        domain = domain.split('/')[0]
        domains.append(domain)

    return {
        "urls": list(set(urls)),
        "domains": list(set(domains)),
        "ips": list(set(ips))
    }

def main():
    with open("sample_phishing_email.txt", "r") as f:
        email_content = f.read()

    iocs = extract_iocs(email_content)

    print("Extracted IOCs")
    print("----------------")
    for category, values in iocs.items():
        print(f"\n{category.upper()}:")
        if values:
            for v in values:
                print(f" - {v}")
        else:
            print(" - None found")

if __name__ == "__main__":
    main()
