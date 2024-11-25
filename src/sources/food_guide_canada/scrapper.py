from interfaces import LinkCollector, TextExtractor
from base_scraper import BaseScraper
from bs4 import BeautifulSoup


class FoodGuideCanadaLinkCollector(BaseScraper, LinkCollector):
    def collect_links(self, url: str) -> list[str]:
        xml_content = self.fetch_page(url)
        return self.parse_xml(xml_content)

    def parse_xml(self, xml_content: str) -> list[str]:
        soup = BeautifulSoup(xml_content, "lxml-xml")
        return [loc.text for loc in soup.find_all("loc") if "/en/" in loc.text]  # Берем только англ. версии страниц


class FoodGuideCanadaTextExtractor(TextExtractor):
    def extract_text(self, page_content: str) -> str:
        soup = BeautifulSoup(page_content, "html.parser")
        content = soup.find("main")
        if not content:
            raise ValueError("No article content found")
        # Возвращаем текст, если элемент найден, иначе пустой словарь
        return content.get_text(strip=True)
