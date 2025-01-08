

### Article Parser for RAG Bot

#### Installation

```
pip install -r requirements.txt
```

#### Usage
```
Follow instructions for each of source
```

#### Sources

### Nutritionist Bot by Elena Oshchepkova

[Telegram Channel](https://t.me/elenadoc_nutr)

#### Eat Right

- Website: [https://www.eatright.org/](https://www.eatright.org/)
- Sitemap: [https://www.eatright.org/sitemap.xml](https://www.eatright.org/sitemap.xml)

**Steps:**

1. Collect pages from the sitemap (depth = 1).
2. Extract HTML content.

Project folder in the bucket: `elenadoc_nutr/eat_right`

```shell
cd src
python -m cli eat_right collect_links --url https://www.eatright.org/sitemap.xml --csv links.csv --folder elenadoc_nutr/eat_right
```

```shell
python -m cli eat_right extract_text --csv links.csv --folder elenadoc_nutr/eat_right
```

---

#### Mayo Clinic Health System

- Website: [https://www.mayoclinichealthsystem.org/wellness-hub](https://www.mayoclinichealthsystem.org/wellness-hub)
- Sitemap: [https://www.mayoclinichealthsystem.org/sitemapmchs.xml](https://www.mayoclinichealthsystem.org/sitemapmchs.xml)

**Steps:**

1. Collect pages from the sitemap (depth = 1).
2. Extract HTML content (filtering out unnecessary tags).

Project folder in the bucket: `elenadoc_nutr/mayo_clinic_health_system`

```shell
cd src
python -m cli mayo_clinic_health_system collect_links --url https://www.mayoclinichealthsystem.org/sitemapmchs.xml --folder elenadoc_nutr/mayo_clinic_health_system
```

```shell
python -m cli mayo_clinic_health_system extract_text --folder elenadoc_nutr/mayo_clinic_health_system
```

---

#### EuFic

- Website: [https://www.eufic.org/en/](https://www.eufic.org/en/)
- Sitemap: [https://www.eufic.org/en/sitemap.xml](https://www.eufic.org/en/sitemap.xml)

**Steps:**

1. Collect pages from the sitemap (depth = 1).
2. Extract HTML content (filtering out unnecessary tags).

Project folder in the bucket: `elenadoc_nutr/eufic`

```shell
cd src
python -m cli eufic collect_links --url https://www.eufic.org/en/sitemap.xml --folder elenadoc_nutr/eufic
```

```shell
python -m cli eufic extract_text --folder elenadoc_nutr/eufic
```

---

#### Food Guide Canada

- Website: [https://food-guide.canada.ca/en/](https://food-guide.canada.ca/en/)
- Sitemap: [https://food-guide.canada.ca/sitemap.xml](https://food-guide.canada.ca/sitemap.xml)

**Steps:**

1. Collect pages from the sitemap (depth = 1).
2. Extract HTML content (filtering out unnecessary tags).

Project folder in the bucket: `elenadoc_nutr/food_guide_canada`

```shell
cd src
python -m cli food_guide_canada collect_links --url https://food-guide.canada.ca/sitemap.xml --folder elenadoc_nutr/food_guide_canada
```

```shell
python -m cli food_guide_canada extract_text --folder elenadoc_nutr/food_guide_canada
```

---

#### Harvard Health

- Section: [https://www.health.harvard.edu/category/staying-healthy](https://www.health.harvard.edu/category/staying-healthy)
- Sitemap: [https://www.health.harvard.edu/sitemap.xml](https://www.health.harvard.edu/sitemap.xml)

**Steps:**

1. Collect pages from the sitemap (depth = 1).
2. Extract HTML content (filtering out unnecessary tags).

Project folder in the bucket: `elenadoc_nutr/health_harvard`

```shell
cd src
python -m cli health_harvard collect_links --url https://www.health.harvard.edu/sitemap.xml --folder elenadoc_nutr/health_harvard
```

```shell
python -m cli health_harvard extract_text --folder elenadoc_nutr/health_harvard
```

---

#### Help Guide

- Website: [https://www.helpguide.org/wellness/](https://www.helpguide.org/wellness/)
- Sitemap: [https://www.helpguide.org/sitemap_index.xml](https://www.helpguide.org/sitemap_index.xml)

**Steps:**

1. Collect pages from the sitemap (depth = 2).
2. Extract HTML content (filtering out unnecessary tags).

Project folder in the bucket: `elenadoc_nutr/help_guide`

```shell
cd src
python -m cli help_guide collect_links --url https://www.helpguide.org/sitemap_index.xml --folder elenadoc_nutr/help_guide
```

```shell
python -m cli help_guide extract_text --folder elenadoc_nutr/help_guide
```

---

#### NHS

- Website: [https://www.nhs.uk/live-well/](https://www.nhs.uk/live-well/)
- Sitemap: [https://www.nhs.uk/sitemaps/sitemap-content.xml](https://www.nhs.uk/sitemaps/sitemap-content.xml)

Project folder in the bucket: `elenadoc_nutr/nhs`

```shell
cd src
python -m cli nhs collect_links --url https://www.nhs.uk/sitemaps/sitemap-content.xml --folder elenadoc_nutr/nhs
```

```shell
python -m cli nhs extract_text --folder elenadoc_nutr/nhs
```

---

#### World Health Organization

- Website: [WHO Publications](https://www.who.int/publications/m?healthtopics=2e85d1d9-8b1f-4676-9aeb-991ca5b45b5b)
- Document List API: [WHO API Example](https://www.who.int/api/hubs/meetingreports)

**Steps:**

1. Collect pages from JSON (with pagination).
2. Download PDFs.

Project folder in the bucket: `elenadoc_nutr/who`

```shell
cd src
python -m cli who collect_links --url "https://www.who.int/api/hubs/meetingreports?..." --csv documents_links.csv --folder elenadoc_nutr/who
python -m cli who collect_links --url "https://www.who.int/api/hubs/publications?..." --csv publications_links.csv --folder elenadoc_nutr/who
```

```shell
python -m cli who transfer_file --folder elenadoc_nutr/who --csv documents_links.csv
python -m cli who transfer_file --folder elenadoc_nutr/who --csv publications_links.csv
```

---

#### Dietary Guidelines

- [Consumer Resources](https://www.dietaryguidelines.gov/resources/consumer-resources)
- [2020-2025 Dietary Guidelines](https://www.dietaryguidelines.gov/resources/2020-2025-dietary-guidelines-online-materials): Download one file.
- [Professional Resources](https://www.dietaryguidelines.gov/professional-resources): Extract PDF links from HTML and download PDFs.
