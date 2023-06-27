import requests
import argparse
import time
from tqdm import tqdm
from rich.progress import Progress

PROXY_TYPES = {
    "1": "SOCKS5",
    "2": "SOCKS4",
    "3": "HTTPS",
    "4": "HTTP",
    "5": "HTTP(S)",
    "6": "ALL",
}

def scrape_proxies(proxy_links):
    proxies = []

    for link in proxy_links:
        response = requests.get(link)
        lines = response.text.split("\n")
        for line in lines:
            if line:
                proxies.append(line.strip())

    return proxies

def main():
    proxy_links = {
        "1": [
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
            "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks5/socks5.txt",
        ],
        "2": [
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
            "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks4/socks4.txt",
        ],
        "3": [
            "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
        ],
        "4": [
            "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
        ],
        "5": [
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
        ],
        "6": [
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
            "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks5/socks5.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
            "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks4/socks4.txt",
            "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
            "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
        ],
    }

    proxy_type = input("Select the type of proxies you want to scrape:\n"
                       "1. SOCKS5\n"
                       "2. SOCKS4\n"
                       "3. HTTPS\n"
                       "4. HTTP\n"
                       "5. HTTP(S)\n"
                       "6. ALL\n"
                       "Enter your choice (1-6): ")

    if proxy_type not in PROXY_TYPES:
        print("Invalid proxy type selected.")
        return

    selected_type = PROXY_TYPES[proxy_type]
    proxy_links_selected = proxy_links[proxy_type]

    print("\nStarting proxy scraping...")
    start_time = time.time()

    proxies = scrape_proxies(proxy_links_selected)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print("\nProxy scraping completed!")
    print(f"Elapsed Time: {elapsed_time:.2f} seconds")
    print(f"Scraped Proxies: {len(proxies)}")

    output_file = f"scraped_proxies_{selected_type.upper()}.txt"

    with open(output_file, "w") as f:
        for proxy in proxies:
            f.write(proxy + "\n")

    print(f"Scraped Proxies saved to {output_file}")

if __name__ == "__main__":
    main()

