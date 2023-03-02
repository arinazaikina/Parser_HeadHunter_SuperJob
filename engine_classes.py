from abc import ABC, abstractmethod

import requests

from jobs_classes import Vacancy


class Engine(ABC):
    @abstractmethod
    def get_request(self, params):
        pass

    @abstractmethod
    def get_formatted_data(self, data: dict):
        pass


class HeadHunter(Engine):
    def __init__(self, search: str, no_experience) -> None:
        self.__search = search
        self.__url = 'https://api.hh.ru/vacancies/'
        if no_experience == 'y':
            self.__experience = 'noExperience'
        else:
            self.__experience = None

    def get_request(self, params: dict):
        try:
            response = requests.get(url=self.__url, params=params)
            if response.status_code != 200:
                raise LookupError(f'статус код {response.status_code}')
            if not response:
                return []
            data = response.json()
            if not data:
                raise LookupError('Ответ пустой')
            return data
        except (requests.exceptions.RequestException, LookupError) as error:
            print(f'Не могу получить данные, {error}')
            return []

    def get_formatted_data(self, unformatted_data: dict):
        about_vacancy = {
            'name': unformatted_data['name'],
            'url': unformatted_data['alternate_url'],
            'description': self.get_formatted_description(unformatted_data=unformatted_data),
            'salary': self.get_formatted_salary(salary=unformatted_data['salary']),
            'city': unformatted_data['area']['name'],
            'employer': unformatted_data['employer']['name']
        }
        return about_vacancy

    @staticmethod
    def get_formatted_salary(salary):
        if salary is None or salary['from'] is None:
            return 0
        return salary['from']

    @staticmethod
    def get_formatted_description(unformatted_data: dict):
        str_description = ''
        if unformatted_data['snippet']['requirement'] is not None:
            str_description += unformatted_data['snippet']['requirement']
        if unformatted_data['snippet']['responsibility'] is not None:
            str_description += '\n' + unformatted_data['snippet']['responsibility']
        return str_description.replace('<highlighttext>', '').replace('</highlighttext>', '')

    def get_vacancy_list(self):
        vacancy_list = []
        page = 0
        print('Ищу вакансии по вашему запросу. Пожалуйста, подождите...')
        while True:
            params = {
                'text': self.__search,
                'experience': self.__experience,
                'page': page,
                'per_page': 100,
                'area': '113'
            }
            data = self.get_request(params=params)
            print('.', end='')
            for item in data.get('items'):
                vacancy_list.append(Vacancy(data=self.get_formatted_data(unformatted_data=item)))
            if data.get('pages') - page <= 1:
                print(f'\nКоличество найденных вакансий: {len(vacancy_list)}')
                break
            else:
                page += 1
        return vacancy_list
