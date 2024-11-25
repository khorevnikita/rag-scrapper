# Парсер статей для RAG Bot

## Установка

...

## Использование

..

## Лог

### Нутрициолог-бот от Елена Ощепкова

https://t.me/elenadoc_nutr

#### Eat right

- Сайт https://www.eatright.org/
- Sitemap https://www.eatright.org/sitemap.xml

Шаги:

1. Собрать страницы sitemap (вложенность = 1)
2. Собрать HTML

Папка проекта в bucket: `elenadoc_nutr/eat_right`

```shell
cd src
python -m cli eat_right collect_links --url https://www.eatright.org/sitemap.xml --csv links.csv --folder elenadoc_nutr/eat_right
```

```shell
python -m cli eat_right extract_text --csv links.csv --folder elenadoc_nutr/eat_right
```

#### Mayo Clinic Health System

- Сайт https://www.mayoclinichealthsystem.org/wellness-hub
- Sitemap  https://www.mayoclinichealthsystem.org/sitemapmchs.xml

Шаги:

1. Собрать страницы sitemap (вложенность = 1)
2. Собрать HTML (фильтр на лишние теги)

Папка проекта в bucket: `elenadoc_nutr/mayo_clinic_health_system`

```shell
cd src
python -m cli mayo_clinic_health_system collect_links --url https://www.mayoclinichealthsystem.org/sitemapmchs.xml --folder elenadoc_nutr/mayo_clinic_health_system
```

```shell
python -m cli mayo_clinic_health_system extract_text --folder elenadoc_nutr/mayo_clinic_health_system
```

#### EuFic

- Сайт https://www.eufic.org/en/
- Sitemap  https://www.eufic.org/en/sitemap.xml

Шаги:

1. Собрать страницы sitemap (вложенность = 1)
2. Собрать HTML (фильтр на лишние теги)

Папка проекта в bucket: `elenadoc_nutr/eufic`

```shell
cd src
python -m cli eufic collect_links --url https://www.eufic.org/en/sitemap.xml --folder elenadoc_nutr/eufic
```

```shell
python -m cli eufic extract_text --folder elenadoc_nutr/eufic
```

#### Food Guide Canada

- Сайт https://food-guide.canada.ca/en/
- Sitemap  https://food-guide.canada.ca/sitemap.xml

Шаги:

1. Собрать страницы sitemap (вложенность = 1)
2. Собрать HTML (фильтр на лишние теги)

Папка проекта в bucket: `elenadoc_nutr/food_guide_canada`

```shell
cd src
python -m cli food_guide_canada collect_links --url https://food-guide.canada.ca/sitemap.xml --folder elenadoc_nutr/food_guide_canada
```

```shell
python -m cli food_guide_canada extract_text --folder elenadoc_nutr/food_guide_canada
```

#### Health harvard

- Сайт (раздел) https://www.health.harvard.edu/category/staying-healthy
- Sitemap https://www.health.harvard.edu/sitemap.xml
-

Шаги:

1. Собрать страницы sitemap (вложенность = 1)
2. Собрать HTML (фильтр на лишние теги)

Папка проекта в bucket: `elenadoc_nutr/health_harvard`

```shell
cd src
python -m cli health_harvard collect_links --url https://www.health.harvard.edu/sitemap.xml --folder elenadoc_nutr/health_harvard
```

```shell
python -m cli health_harvard extract_text --folder elenadoc_nutr/health_harvard
```

#### Help Guide
- Сайт https://www.helpguide.org/wellness/
- Sitemap https://www.helpguide.org/sitemap_index.xml

Шаги:
1. Собрать страницы sitemap (вложенность = 2)
2. Собрать HTML (фильтр на лишние теги)

Папка проекта в bucket: `elenadoc_nutr/help_guide`

```shell
cd src
python -m cli help_guide collect_links --url https://www.helpguide.org/sitemap_index.xml --folder elenadoc_nutr/help_guide
```

```shell
python -m cli help_guide extract_text --folder elenadoc_nutr/help_guide
```

#### NHS
- https://www.nhs.uk/live-well/
- Sitemap: https://www.nhs.uk/sitemaps/sitemap-content.xml

Папка проекта в bucket: `elenadoc_nutr/nhs`

```shell
cd src
python -m cli nhs collect_links --url https://www.nhs.uk/sitemaps/sitemap-content.xml --folder elenadoc_nutr/nhs
```

```shell
python -m cli nhs extract_text --folder elenadoc_nutr/nhs
```

#### World Health Organization
- Сайт https://www.who.int/publications/m?healthtopics=2e85d1d9-8b1f-4676-9aeb-991ca5b45b5b
- Список документов из API И публикаций https://www.who.int/publications/i?healthtopics=2e85d1d9-8b1f-4676-9aeb-991ca5b45b5b&publishingoffices=&healthtopics-hidden=true

Пример JSON:
https://www.who.int/api/hubs/meetingreports?sf_site=15210d59-ad60-47ff-a542-7ed76645f0c7&sf_provider=OpenAccessProvider&sf_culture=en&$orderby=PublicationDateAndTime%20desc&$select=Title,ItemDefaultUrl,FormatedDate,Tag,ThumbnailUrl,DownloadUrl,TrimmedTitle&%24format=json&%24top=100&%24count=true

Шаги:
1. Собрать страницы JSON (с пагинацией)
2. Выкачать PDF

Папка проекта в bucket: `elenadoc_nutr/nhs`

```shell
cd src
python -m cli who collect_links --url "https://www.who.int/api/hubs/meetingreports?sf_site=15210d59-ad60-47ff-a542-7ed76645f0c7&sf_provider=OpenAccessProvider&sf_culture=en&%24format=json&%24filter=healthtopics%2Fany(a%3Aa%20eq%202e85d1d9-8b1f-4676-9aeb-991ca5b45b5b)&%24count=true" --csv documents_links.csv --folder elenadoc_nutr/who
python -m cli who collect_links --url "https://www.who.int/api/hubs/publications?sf_site=15210d59-ad60-47ff-a542-7ed76645f0c7&sf_provider=OpenAccessProvider&sf_culture=en&%24format=json&%24filter=healthtopics%2Fany(a%3Aa%20eq%202e85d1d9-8b1f-4676-9aeb-991ca5b45b5b)&%24count=true" --csv publications_links.csv --folder elenadoc_nutr/who
```

```shell
python -m cli who transfer_file --folder elenadoc_nutr/who --csv documents_links.csv
python -m cli who transfer_file --folder elenadoc_nutr/who --csv publications_links.csv
```