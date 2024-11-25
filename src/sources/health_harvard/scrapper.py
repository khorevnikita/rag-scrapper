from interfaces import LinkCollector, TextExtractor
from base_scraper import BaseScraper
from bs4 import BeautifulSoup


class HealthHarvardLinkCollector(BaseScraper, LinkCollector):
    def collect_links(self, url: str) -> list[str]:
        xml_content = self.fetch_page(url)
        return self.parse_xml(xml_content)


class HealthHarvardTextExtractor(TextExtractor):
    def extract_text(self, page_content: str) -> str:
        soup = BeautifulSoup(page_content, "html.parser")
        content = soup.find("article")
        if not content:
            raise ValueError("No article content found")
        # Возвращаем текст, если элемент найден, иначе пустой словарь
        return content.get_text(strip=True)
