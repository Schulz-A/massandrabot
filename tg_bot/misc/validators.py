import re


def name_validate(name: str):
    if len(name) > 50:
        raise ValueError("Название слисшком длинное, не должно превышать 50 символовю Попробуйте еще раз")
    return name


def url_validator(url: str):
    url_regex = re.compile(
        r'^(?:http|ftp)s?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    if not re.match(url_regex, url):
        raise ValueError("Это не URL адрес. Попробуйте снова")

    return url


def abr_validation(abr: str):
    if len(abr) > 5 or not abr.isupper():
        raise ValueError(
            "Аббревиатура должна быть не более 5 символов и состоять только из заглавных букв. Попробуй еще раз"
        )

    return abr


validators = {
    "name": name_validate,
    "url": url_validator,
    "abbreviation": abr_validation
}
