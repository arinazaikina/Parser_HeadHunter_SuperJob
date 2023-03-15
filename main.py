from engine_classes import HeadHunter, SuperJob
from jobs_utils import (
    get_sorted_vacancy_list_by_salary,
    get_filtered_vacancy_list_by_city,
    get_sorted_vacancy_list_by_date,
    save_to_file
)


def main() -> None:
    search_input = input('Введите вакансию для поиска: ').strip()
    experience_input = input(
        'Введите 1, если будем искать вакансии, в которых не требуется опыт.\nВведите любой символ, если это неважно: '
    ).strip()

    # Поиск вакансий на HH
    hh = HeadHunter(search=search_input, no_experience=experience_input)
    # Поиск вакансий на SJ
    sj = SuperJob(search=search_input, no_experience=experience_input)

    hh_vacancy_list = hh.get_vacancy_list()
    sj_vacancy_list = sj.get_vacancy_list()
    # Список найденных вакансий
    vacancy_list = hh_vacancy_list + sj_vacancy_list

    while True:
        print(
            '\nМЕНЮ\n'
            '1 - выбрать топ-10 высокооплачиваемых вакансий\n'
            '2 - выбрать вакансии в определённом городе\n'
            '3 - выбрать топ-10 недавно опубликованных вакансий\n'
            'Любая клавиша - выход\n'
        )
        choice_input = input('Введите цифру: ')

        if choice_input == '1':
            result = get_sorted_vacancy_list_by_salary(vacancy_list=vacancy_list)
            save_to_file(choice=choice_input, result=result)

        elif choice_input == '2':
            city_input = input('Введите город: ')
            result = get_filtered_vacancy_list_by_city(vacancy_list=vacancy_list, city=city_input)
            save_to_file(choice=choice_input, result=result, city=city_input)

        elif choice_input == '3':
            result = get_sorted_vacancy_list_by_date(vacancy_list=vacancy_list)
            save_to_file(choice=choice_input, result=result)
        else:
            print('Программа завершила работу')
            save_to_file(choice=choice_input, result=vacancy_list)
            break


if __name__ == '__main__':
    main()
