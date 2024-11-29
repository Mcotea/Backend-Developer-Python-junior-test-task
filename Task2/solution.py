import requests
from bs4 import BeautifulSoup
import csv
from collections import defaultdict


def get_animal_category_page(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def extract_animals_from_page(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    animals_by_letter = defaultdict(int)

    category_groups = soup.find_all('div', class_='mw-category-group')

    for group in category_groups:
        links = group.find_all('a')
        for link in links:
            animal_name = link.get_text(strip=True)
            if animal_name:
                first_letter = animal_name[0].upper()
                if first_letter.isalpha():
                    animals_by_letter[first_letter] += 1

    return animals_by_letter


def get_next_page_url(soup):
    next_button = soup.find('a', text='Следующая страница')
    if next_button:
        return 'https://ru.wikipedia.org' + next_button['href']
    return None


def save_to_csv(animals_by_letter):
    with open("beasts.csv", mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Буква', 'Количество животных'])

        for letter in map(chr, range(1040, 1072)):
            count = animals_by_letter.get(letter, 0)
            writer.writerow([letter, count])


def main():
    base_url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
    page_url = base_url
    animals_by_letter = defaultdict(int)

    while page_url:
        print(f'Обрабатываем страницу: {page_url}')
        page_content = get_animal_category_page(page_url)
        animals_on_page = extract_animals_from_page(page_content)

        for letter, count in animals_on_page.items():
            animals_by_letter[letter] += count

        soup = BeautifulSoup(page_content, 'html.parser')
        page_url = get_next_page_url(soup)

    save_to_csv(animals_by_letter)


if __name__ == "__main__":
    main()
