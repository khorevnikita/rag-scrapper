from interfaces import LinkCollector, TextExtractor
from base_scraper import BaseScraper
from bs4 import BeautifulSoup


class HelpGuideLinkCollector(BaseScraper, LinkCollector):
    def collect_links(self, url: str) -> list[str]:
        xml_content = self.fetch_page(url)
        xml_links = self.parse_xml(xml_content)
        links = []
        for xlm_link in xml_links:
            links += self.parse_xml(self.fetch_page(xlm_link))
        return links


class HelpGuideTextExtractor(TextExtractor):
    def extract_text(self, page_content: str) -> str:
        soup = BeautifulSoup(page_content, "html.parser")
        section = soup.find("section", id="post-main")
        content = section.find("div", class_="post-main-content")
        if not content:
            raise ValueError("No article content found")
        # Возвращаем текст, если элемент найден, иначе пустой словарь
        return content.get_text(strip=True)
