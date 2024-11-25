import csv
import io
from s3_utils import upload_to_s3, download_from_s3


def save_links_to_csv_s3(key: str, links: list[str]):
    """
    Сохранение ссылок в CSV в S3.
    """
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow(["URL"])
    for link in links:
        writer.writerow([link])
    upload_to_s3(key, buffer.getvalue())
    print(f"CSV saved to S3 at {key}")


def load_links_from_csv_s3(key: str) -> list[str]:
    """
    Загрузка ссылок из CSV из S3.
    """
    csv_content = download_from_s3(key)
    buffer = io.StringIO(csv_content)
    reader = csv.DictReader(buffer)
    return [row["URL"] for row in reader]
