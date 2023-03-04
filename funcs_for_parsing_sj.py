from datetime import date, timedelta

from bs4.element import Tag

RU_MONTH_VALUES = {
    'января': '01',
    'февраля': '02',
    'марта': '03',
    'апреля': '04',
    'мая': '05',
    'июня': '06',
    'июля': '07',
    'августа': '08',
    'сентября': '09',
    'октября': '10',
    'ноября': '11',
    'декабря': '12',
}


def get_formatted_name_and_url_sj(unformatted_data: Tag) -> tuple | None:
    """
    Возвращает текст элемента span с class='_26gg2 _3oXMw _2LaRg hbKbL rIDaO oDIMq _33qju _1ZV-S' и
    href элемента a, находящегося в указанном span в html-разметке страницы
    """
    name = unformatted_data.find('span', class_='_26gg2 _3oXMw _2LaRg hbKbL rIDaO oDIMq _33qju _1ZV-S')
    if name is not None:
        url = 'https://russia.superjob.ru/' + name.find('a').get('href')
        name = name.get_text(strip=True)
        return name, url
    return None, None


def get_formatted_published_date_sj(unformatted_data: Tag) -> date | None:
    """
    Находит текст элемента span с class='_2H6gy oDIMq WlSzf _3T7lp' в html-разметке страницы,
    преобразует его в дату нужного формата и возвращает объект date
    """
    published_date_row = unformatted_data.find('span', class_='_2H6gy oDIMq WlSzf _3T7lp')
    if published_date_row is not None:
        published_date = published_date_row.get_text(strip=True)
        if published_date.split(' ')[0] == 'Сегодня':
            return date.today()
        elif published_date.split(' ')[0] == 'Вчера':
            today = date.today()
            yesterday = today + timedelta(days=-1)
            return yesterday
        else:
            day = str(published_date.split(' ')[0])
            if len(day) == 1:
                day = '0' + day
            month = RU_MONTH_VALUES[f"{published_date.split(' ')[1]}"]
            year = str(date.today().year)
            return date.fromisoformat(f'{year}-{month}-{day}')
    return None


def get_formatted_description_sj(unformatted_data: Tag) -> str | None:
    """
    Возвращает текст элемента span с class='_2H6gy oDIMq _33qju _3T7lp _2R-87' в html-разметке страницы
    """
    description = unformatted_data.find('span', class_='_2H6gy oDIMq _33qju _3T7lp _2R-87')
    if description is not None:
        return description.get_text(strip=True)
    return None


def get_formatted_salary_sj(unformatted_data: Tag) -> int | None:
    """
    Находит текст элемента span с class='_2eYAG rIDaO oDIMq _33qju _3T7lp' в html-разметке страницы,
    преобразует его в нужный формат и возвращает объект int
    Если возвращает 0, это соответствует ЗП по договорённости
    """
    salary_row = unformatted_data.find('span', class_='_2eYAG rIDaO oDIMq _33qju _3T7lp')
    if salary_row is not None:
        salary = salary_row.get_text(strip=True)
        if salary.strip() == 'По договорённости':
            return 0
        elif salary.startswith('от') or salary.startswith('до'):
            result = ''
            for symbol in salary:
                if symbol.isdigit():
                    result += symbol
            return int(result)
        elif '—' in salary:
            result = ''
            for symbol in salary.split('—')[0]:
                if symbol.isdigit():
                    result += symbol
            return int(result)
        elif ' ' in salary:
            result = ''
            for symbol in salary:
                if symbol.isdigit():
                    result += symbol
            return int(result)
        return 0
    return None


def get_formatted_city_sj(unformatted_data: Tag) -> str | None:
    """
    Находит элемент div c class='WDWTW _2SOuz _3JyWQ _1CjMB -knfs' в html-разметке страницы.
    Если элемент найден, ищет элемент div с class='_32Fb8' и возвращает текст этого элемента.
    """
    city_div = unformatted_data.find('div', class_='WDWTW _2SOuz _3JyWQ _1CjMB -knfs')
    if city_div is not None:
        return city_div.find('div', class_='_32Fb8').get_text(strip=True)
    return None


def get_formatted_employer_sj(unformatted_data: Tag) -> str | None:
    """
    Находит элемент span c class='_3nMqD f-test-text-vacancy-item-company-name _2LynC oDIMq _33qju _3T7lp _2R-87'
    в html-разметке страницы. Если элемент найден, ищет элемент a внутри span и возвращает текст этого элемента.
    """
    employer_span = unformatted_data.find('span', class_='_3nMqD f-test-text-vacancy-item-company-'
                                                         'name _2LynC oDIMq _33qju _3T7lp _2R-87')
    if employer_span is not None:
        return employer_span.find('a').get_text(strip=True)
    return None
