import os

from engine_classes import HeadHunter
from jobs_utils import get_sorted_vacancy_list_by_salary, get_filtered_vacancy_list_by_city, get_sorted_vacancy_list_by_date, save_to_file


def main() -> None:
    search_input = input('Введите вакансию для поиска: ').strip()
    experience_input = input(
        'Введите 1, если будем искать вакансии, в которых не требуется опыт.\nВведите любой символ, если это неважно: '
    )

    hh = HeadHunter(search=search_input, no_experience=experience_input)
    hh_vacancy_list = hh.get_vacancy_list()

    while True:
        print(
            '\nМЕНЮ\n'
            '1 - выбрать топ-10 высокооплачиваемых вакансий\n'
            '2 - выбрать вакансии в определённом городе\n'
            '3 - выбрать топ-10 недавно опубликованных вакансий\n'
            'Любая клавиша - выход\n'
        )
        choice_input = input('Введите цифру: ')
        result = get_sorted_vacancy_list_by_salary(vacancy_list=hh_vacancy_list)
        if choice_input == '1':
            path = os.path.join('data', 'топ_высокооплачиваемых.txt')
            title = 'ТОП-10 ВЫСОКООПЛАЧИВАЕМЫХ ВАКАНСИЙ'
            save_to_file(path=path, title=title, result=result)

        elif choice_input == '2':
            city_input = input('Введите город: ')
            result = get_filtered_vacancy_list_by_city(vacancy_list=result, city=city_input)
            path = os.path.join('data', f'вакансии_{city_input}.txt')
            title = f'ВАКАНСИИ ГОРОД {city_input}'
            save_to_file(path=path, title=title, result=result)

        elif choice_input == '3':
            result = get_sorted_vacancy_list_by_date(vacancy_list=result)
            path = os.path.join('data', 'топ_недавних.txt')
            title = 'ТОП-10 НЕДАВНО ОПУБЛИКОВАННЫХ ВАКАНСИЙ'
            save_to_file(path=path, title=title, result=result)
        else:
            print('Программа завершила работу')
            break


if __name__ == '__main__':
    main()
