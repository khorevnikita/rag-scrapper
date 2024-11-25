from interfaces import LinkCollector, TextExtractor
from base_scraper import BaseScraper
from bs4 import BeautifulSoup


class EatRightLinkCollector(BaseScraper, LinkCollector):
    def collect_links(self, url: str) -> list[str]:
        xml_content = self.fetch_page(url)
        return self.parse_xml(xml_content)


class EatRightTextExtractor(TextExtractor):
    def extract_text(self, page_content: str) -> dict[str, str]:
        soup = BeautifulSoup(page_content, "html.parser")
        content = soup.find("div", class_="content")
        return {"content": content.text.strip()} if content else {}
