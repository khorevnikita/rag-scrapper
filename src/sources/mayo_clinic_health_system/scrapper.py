from interfaces import LinkCollector, TextExtractor
from base_scraper import BaseScraper
from bs4 import BeautifulSoup


class MayoClinicLinkCollector(BaseScraper, LinkCollector):
    def collect_links(self, url: str) -> list[str]:
        xml_content = self.fetch_page(url)
        return self.parse_xml(xml_content)

    def parse_xml(self, xml_content: str) -> list[str]:
        soup = BeautifulSoup(xml_content, "lxml-xml")
        return [loc.text for loc in soup.find_all("loc") if "provider" not in loc.text]


class MayoClinicTextExtractor(TextExtractor):
    def extract_text(self, page_content: str) -> str:
        soup = BeautifulSoup(page_content, "html.parser")
        # Ищем заголовок h1 с указанным классом
        article_header = soup.find("h1", class_='article-detail-masthead__headline')
        if not article_header:
            raise ValueError("No article header found")
        # Ищем элемент <main id="main">
        section = soup.find("section", class_="section")
        content = section.find("div", class_="col-main")
        if not content:
            raise ValueError("No article content found")
        # Возвращаем текст, если элемент найден, иначе пустой словарь
        return content.get_text(strip=True)
