import csv

def save_links_to_csv(file_path: str, links: list[str]):
    with open(file_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["URL"])
        for link in links:
            writer.writerow([link])

def load_links_from_csv(file_path: str) -> list[str]:
    with open(file_path, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        return [row["URL"] for row in reader]
