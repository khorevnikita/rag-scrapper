from interfaces import LinkCollector, TextExtractor
from base_scraper import BaseScraper
from bs4 import BeautifulSoup


class EatRightLinkCollector(BaseScraper, LinkCollector):
    def collect_links(self, url: str) -> list[str]:
        xml_content = self.fetch_page(url)
        return self.parse_xml(xml_content)


class EatRightTextExtractor(TextExtractor):
    def extract_text(self, page_content: str) -> str:
        soup = BeautifulSoup(page_content, "html.parser")
        # Ищем заголовок h1 с указанным классом
        article_header = soup.find("h1", class_='article-detail-masthead__headline')
        if not article_header:
            raise ValueError("No article header found")
        # Ищем элемент <main id="main">
        content = soup.find("main", id="main")
        if not content:
            raise ValueError("No article content found")
        # Возвращаем текст, если элемент найден, иначе пустой словарь
        return content.get_text(strip=True)
