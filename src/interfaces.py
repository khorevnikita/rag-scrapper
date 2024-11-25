from abc import ABC, abstractmethod

class LinkCollector(ABC):
    @abstractmethod
    def collect_links(self, url: str) -> list[str]:
        pass

class TextExtractor(ABC):
    @abstractmethod
    def extract_text(self, page_content: str) -> dict[str, str]:
        pass
