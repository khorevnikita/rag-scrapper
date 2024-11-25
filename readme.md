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