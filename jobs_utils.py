from typing import Any, List

from jobs_classes import Vacancy


def get_top_high_paying_jobs(vacancy_list: List[Vacancy]) -> List[Vacancy]:
    """
    Возвращает топ-10 вакансий с сортировкой по уровню заработной платы
    на уменьшение.
    :param vacancy_list: список экземпляров класса Vacancy
    :return: отсортированный список экземпляров класса Vacancy
    """
    return sorted(vacancy_list, key=lambda x: x.salary, reverse=True)[:10]


def get_vacancy_list_in_city(vacancy_list: List[Vacancy], city: str, amount: int) -> Any:
    """
    Возвращает список вакансий в указанном городе.
    :param vacancy_list: список экземпляров класса Vacancy
    :param city: город РФ
    :param amount: количество вакансий
    :return: список экземпляров класса Vacancy или сообщение о том, что вакансии не найдены
    """
    filtered_by_city = list(filter(lambda x: x.city == city, vacancy_list))
    if filtered_by_city:
        return filtered_by_city[:amount]
    return 'Вакансий не найдено'


def get_vacancy_list_for_junior(vacancy_list: List[Vacancy]) -> Any:
    """
    Возвращает список вакансий, в названии которых встречается слово "junior" или "Junior".
    :param vacancy_list: список экземпляров класса Vacancy
    :return: список экземпляров класса Vacancy или сообщение о том, что вакансии не найдены
    """
    filtered_by_level = list(filter(lambda x: 'junior' in x.name or 'Junior' in x.name, vacancy_list))
    if filtered_by_level:
        return filtered_by_level
    return 'Вакансий не найдено'
