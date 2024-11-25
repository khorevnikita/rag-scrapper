import argparse
from .sources.scrapper import get_scrapper
from .csv_utils import save_links_to_csv, load_links_from_csv
from .s3_utils import upload_to_s3
from .base_scraper import BaseScraper


def main():
    parser = argparse.ArgumentParser(description="Scraper CLI")
    parser.add_argument("source", help="Source to collect")
    parser.add_argument("action", choices=["collect_links", "extract_text"], help="Action to perform")
    parser.add_argument("--url", help="URL to start scraping")
    parser.add_argument("--csv", help="CSV file path for saving/loading links")
    parser.add_argument("--s3-bucket", help="S3 bucket name for storing text files")
    args = parser.parse_args()

    LinkCollector, TextExtractor = get_scrapper(args.source)
    if not LinkCollector or not TextExtractor:
        print("Classes not found")
        return

    if args.action == "collect_links":
        collector = LinkCollector()
        links = collector.collect_links(args.url)
        save_links_to_csv(args.csv, links)
        print(f"Links saved to {args.csv}")

    elif args.action == "extract_text":
        extractor = TextExtractor()
        links = load_links_from_csv(args.csv)
        for link in links:
            scraper = BaseScraper()
            page_content = scraper.fetch_page(link)
            text_data = extractor.extract_text(page_content)
            for key, text in text_data.items():
                upload_to_s3(args.s3_bucket, f"{key}.txt", text)
                print(f"Uploaded {key}.txt to S3")


if __name__ == "__main__":
    main()
