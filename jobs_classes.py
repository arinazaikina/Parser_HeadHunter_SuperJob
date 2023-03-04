from datetime import date


class Vacancy:
    """
    Базовый класс, описывающий вакансию.
    Args:
        data (dict): отформатированные данные, полученные от сервиса поиска работы
    Attrs:
        site (str): сервис поиска работы
        name (str): название вакансии
        url (str): ссылка на вакансию
        published_at (str): дата публикации вакансии
        description (str): описание вакансии
        salary (int): заработная плата
        city (str): город
        employer (str): компания

    """
    __slots__ = ('__site', '__name', '__url', '__published_at', '__description', '__salary', '__city', '__employer')

    def __init__(self, data: dict):
        self.__site = data['site']
        self.__name = data['name']
        self.__url = data['url']
        self.__published_at = data['published_at']
        self.__description = data['description']
        self.__salary = data['salary']
        self.__city = data['city']
        self.__employer = data['employer']

    @property
    def site(self) -> str:
        """Геттер. Возвращает сайт, на котором была размещена вакансия"""
        return self.__site

    @property
    def name(self) -> str:
        """Геттер. Возвращает название вакансии"""
        return self.__name

    @property
    def url(self) -> str:
        """Геттер. Возвращает ссылку на вакансию"""
        return self.__url

    @property
    def published_at(self) -> date:
        """Геттер. Возвращает дату публикации вакансии"""
        return self.__published_at

    @property
    def description(self) -> str:
        """Геттер. Возвращает описание вакансии"""
        return self.__description

    @property
    def salary(self) -> int:
        """Геттер. Возвращает заработную плату"""
        return self.__salary

    @property
    def city(self) -> str:
        """Геттер. Возвращает город"""
        return self.__city

    @property
    def employer(self) -> str:
        """Геттер. Возвращает название компании"""
        return self.__employer

    def __repr__(self) -> str:
        return f'Vacancy(site={self.__site}, name={self.__name})'

    def __str__(self) -> str:
        return self.__site + ': ' + self.__name
