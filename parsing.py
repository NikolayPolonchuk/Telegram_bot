# импортируем библиотеку request для работы с данными в сети
import requests


def valute_rates():
    # получаем курсы валют к рублю
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    USD_in_RUR = int(data['Valute']['USD']['Value'])
    EUR_in_RUR = int(data['Valute']['EUR']['Value'])
    return {'USD':USD_in_RUR, 'EUR':EUR_in_RUR, 'RUR':1}


def find_salary(salary_items, rates):
    # считываем зарплату (берём среднюю или ту, которая есть)
    if salary_items['from'] != None and salary_items['to'] != None:
        salary = (int(salary_items['from']) + int(salary_items['to'])) // 2
    elif salary_items['from'] != None:
        salary = int(salary_items['from'])
    else:
        salary = int(salary_items['to'])


    # если зарплата не в рублях переводим по курсу Центробанка
    try:
        salary = int(salary * rates[salary_items['currency']])
    # вакансии с зарплатой в нестандартной валюте в конец
    except:
        salary = 0

    return salary


def main_parsing(request):
    rates = valute_rates()
    vacancies = []
    #цикл, который скачивает вакансии с первых 20 страниц
    for i in range(100):
        # запрос
        url = 'https://api.hh.ru/vacancies'
        # параметры, которые будут добавлены к запросу
        par = {'text':request, 'area':'113', 'page':i, 'only_with_salary':'true', 'search_field':'name'}
        page_vacancies = requests.get(url, params=par)
        # проверка на корректное считывание
        if page_vacancies.status_code == 200:
            vacancies.append(page_vacancies.json())
    

    # объявляем переменную для хранения зарплат в вакансиях и ссылок на них
    salaries = {}


    # цикл, переберает объекты, т.е перебирает вакансии
    for vacancy in vacancies:
        for item in vacancy['items']:
            # записываем зарплату и ссылку на вакансию в хеш-таблицу
            salaries[find_salary(item['salary'], rates)] = item['alternate_url']

    # создаём массив ссылок
    links = []
    # сортируем по зарплате
    sal_keys = sorted(salaries.keys(), reverse=True)
    for key in sal_keys:
        links.append(salaries[key])

    # возвращаем массив ссылок на вакансии, отсортированные по ЗП
    return links
