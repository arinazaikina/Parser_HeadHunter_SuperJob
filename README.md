# Парсер вакансий
## Финальная работа по курсу ООП (Skypro)

### Описание
После запуска программа просит ввести пользователя искомую вакансию.<br>
Также программа просит указать нужно искать вакансии, не требующие опыт (ввести 1 с клавиатуры) или это неважно (ввести любой символ).<br>
Далее программа осуществляет поиск вакансий на сайте HeadHunter, а затем на сайте SuperJob.<br>
После завершения поиска программа показывает пользователю меню со следующими опциями:
* **Цифра 1**: поиск топ-10 высокооплачиваемых вакансий.
* **Цифра 2**: поиск вакансий в определённом городе (программа просит пользователя ввести город для поиска).
* **Цифра 3**: поиск топ-10 недавно опубликованных вакансий.
* **Любой другой символ**: выход их программы.

Все результаты поиска записываются в файлы, которые хранятся в папке results.

### Структура репозитория
* **main.py**: запуск программы
* **engine_classes.py**: классы, описывающие сервисы по поиску работы (HeadHunter и SuperJob)
* **funcs_for_parsing_hh.py**: функции, преобразующие необходимые данные, полученные от сервиса HeadHunter, в нужный формат
* **funcs_for_parsing_sj.py**: функции, преобразующие необходимые данные, полученные от сервиса SuperJob, в нужный формат
* **jobs_classes.py**: класс, описывающий вакансию
* **jobs_utils.py***: функции, выполняющие сортировку и фильтрацию вакансий (по уровню заработной платы, по городу, по дате публикации)
* **flake8**: конфигурационный файл для линтера flake8
* **requirements.txt**: библиотеки, необходимые для работы
### Используемые технологии
* python (3.10)
* requests
* beautifulsoup4
* flake8
### Установка
1. Скопировать всё содержимое из репозитория в новый каталог.<br><br>
2. Создать виртуальное окружение и активировать его<br><br>
``python3 -m venv venv``
``venv/Scripts/activate``<br><br>
3. Перейти в корневую папку и установить требуемые пакеты<br><br>
``pip install -r requirements.txt``<br><br>
4. Запустить программу<br><br>
``python main.py``