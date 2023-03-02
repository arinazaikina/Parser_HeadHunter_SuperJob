from datetime import datetime
from typing import List

from jobs_classes import Vacancy


def get_sorted_vacancy_list_by_salary(vacancy_list: List[Vacancy]) -> List[Vacancy]:
    """
    Возвращает топ-10 вакансий с сортировкой по уменьшению заработной платы.
    :param vacancy_list: список экземпляров класса Vacancy
    :return: отсортированный список экземпляров класса Vacancy
    """
    return sorted(vacancy_list, key=lambda x: x.salary, reverse=True)[:10]


def get_filtered_vacancy_list_by_city(vacancy_list: List[Vacancy], city: str) -> List[Vacancy]:
    """
    Возвращает список вакансий в указанном городе.
    :param vacancy_list: список экземпляров класса Vacancy
    :param city: город РФ
    :return: список экземпляров класса Vacancy или сообщение о том, что вакансии не найдены
    """
    filtered_by_city = list(filter(lambda x: x.city == city, vacancy_list))
    if filtered_by_city:
        return filtered_by_city
    return []


def get_sorted_vacancy_list_by_date(vacancy_list: List[Vacancy]) -> List[Vacancy]:
    """
    Возвращает топ-10 вакансий с сортировкой по дате публикации.
    :param vacancy_list: список экземпляров класса Vacancy
    :return: отсортированный список экземпляров класса Vacancy
    """
    return sorted(vacancy_list, key=lambda x: x.published_at, reverse=True)[:10]


def save_to_file(path: str, title, result: List[Vacancy]) -> None:
    with open(path, 'w', encoding='utf-8') as file:
        now = datetime.now()
        date_formatted = now.strftime('%d.%m.%Y %H:%M')
        file.write(f'{date_formatted}\n')
        file.write(f'{title}\n')
        if result:
            for vacancy in result:
                print(vacancy)
                file.write('=' * 300 + '\n')
                file.write(f'{vacancy.name}\n')
                file.write(f'\tCсылка: {vacancy.url}\n')
                file.write(f'\tДата публикации: {vacancy.published_at}\n')
                file.write(f'\tОписание: {vacancy.description}\n')
                file.write(f'\tЗП: {vacancy.salary}\n')
                file.write(f'\tГород: {vacancy.city}\n')
                file.write(f'\tКомпания: {vacancy.employer}\n')
        else:
            file.write('Вакансий не найдено')
    print(f'Результаты записаны в файл {path}')
