class Vacancy:
    """
    Базовый класс, описывающий вакансию.
    Args:
        data (dict): отформатированные данные, полученные по запросу к API HeadHunter
    Attrs:
        name (str): название вакансии
        url (str): ссылка на вакансию
        description (str): описание вакансии
        salary (int): заработная плата
        city (str): город
        employer (str): компания

    """
    def __init__(self, data: dict):
        self.__name = data['name']
        self.__url = data['url']
        self.__description = data['description']
        self.__salary = data['salary']
        self.__city = data['city']
        self.__employer = data['employer']

    @property
    def name(self):
        """Геттер. Возвращает название вакансии"""
        return self.__name

    @property
    def url(self):
        """Геттер. Возвращает ссылку на вакансию"""
        return self.__url

    @property
    def description(self):
        """Геттер. Возвращает описание вакансии"""
        return self.__description

    @property
    def salary(self):
        """Геттер. Возвращает заработную плату"""
        return self.__salary

    @property
    def city(self):
        """Геттер. Возвращает город"""
        return self.__city

    @property
    def employer(self):
        """Геттер. Возвращает название компании"""
        return self.__employer

    def __repr__(self):
        return f'Vacancy(name={self.__name})'

    def __str__(self):
        return self.__name
