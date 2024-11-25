# Парсер статей для RAG Bot

## Установка

...

## Использование

..

## Лог
### Нутрициолог-бот от Елена Ощепкова
https://t.me/elenadoc_nutr

####  Eat right
- Сайт https://www.eatright.org/
- Sitemap https://www.eatright.org/sitemap.xml

Шаги:
1. Собрать страницы sitemap (вложенность = 1)
2. Собрать HTML

Папка проекта в bucket: `elenadoc_nutr`

```shell
cd src
python -m cli eat_right collect_links --url https://www.eatright.org/sitemap.xml --csv links.csv --folder elenadoc_nutr
```

```shell
python -m cli eat_right extract_text --csv links.csv --folder elenadoc_nutr
```