import requests
from bs4 import BeautifulSoup
from abc import ABC


class BaseScraper(ABC):
    def fetch_page(self, url: str) -> str:
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, zstd",
            "Accept-Language": "en,es;q=0.9,fr;q=0.8,en-US;q=0.7,ru;q=0.6",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "Upgrade-Insecure-Requests": "1",
            "Sec-CH-UA": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            "Sec-CH-UA-Arch": '"x86"',
            "Sec-CH-UA-Bitness": '"64"',
            "Sec-CH-UA-Full-Version-List": '"Google Chrome";v="131.0.6778.85", "Chromium";v="131.0.6778.85", "Not_A Brand";v="24.0.0.0"',
            "Sec-CH-UA-Mobile": "?0",
            "Sec-CH-UA-Model": '""',
            "Sec-CH-UA-Platform": '"Linux"',
            "Sec-CH-UA-Platform-Version": '"6.8.0"',
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
        }

        response = requests.get(url, headers=headers, allow_redirects=True)
        response.raise_for_status()
        if "gzip" in response.headers.get("Content-Encoding", ""):
            return response.content.decode("utf-8")
        return response.text

    def parse_xml(self, xml_content: str) -> list[str]:
        soup = BeautifulSoup(xml_content, "lxml-xml")
        return [loc.text for loc in soup.find_all("loc")]
