import argparse
from sources.scrapper import get_scrapper
from csv_utils import save_links_to_csv_s3, load_links_from_csv_s3
from s3_utils import upload_to_s3
from base_scraper import BaseScraper
from urllib.parse import urlparse
from tqdm import tqdm


def main():
    parser = argparse.ArgumentParser(description="Scraper CLI")
    parser.add_argument("source", help="Source to collect")
    parser.add_argument("action", choices=["collect_links", "extract_text"], help="Action to perform")
    parser.add_argument("--url", help="URL to start scraping")
    parser.add_argument("--csv", help="CSV file path for saving/loading links")
    parser.add_argument("--folder", help="Folder in s3 bucket")
    args = parser.parse_args()

    LinkCollector, TextExtractor = get_scrapper(args.source)
    if not LinkCollector or not TextExtractor:
        print("Classes not found")
        return

    if args.action == "collect_links":
        collector = LinkCollector()
        links = collector.collect_links(args.url)
        save_links_to_csv_s3(f"{args.folder}/{args.csv}", links)
        print(f"Links saved to {args.csv}")

    elif args.action == "extract_text":
        extractor = TextExtractor()
        links = load_links_from_csv_s3(f"{args.folder}/{args.csv}")
        for link in tqdm(links, desc="Processing links", unit="link"):
            scraper = BaseScraper()
            try:
                page_content = scraper.fetch_page(link)
                text = extractor.extract_text(page_content)
            except Exception as e:
                print("Skipping", link, "error:", e)
                continue
            # Преобразуем путь URL в ключ
            parsed_url = urlparse(link)
            path = parsed_url.path.lstrip("/")  # Убираем начальный слэш
            if not path or path.endswith("/"):
                path = f"{path.rstrip('/')}/index"  # Добавляем index для пустых путей
            file_key = path.replace("/", "-")  # Заменяем / на -

            upload_to_s3(f"{args.folder}/library/{file_key}.txt", text)
            print(f"Uploaded {file_key}.txt to S3")


if __name__ == "__main__":
    main()
