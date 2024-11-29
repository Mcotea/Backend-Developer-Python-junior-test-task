import unittest
import csv
from collections import defaultdict
from unittest.mock import patch, MagicMock
from bs4 import BeautifulSoup
from solution import main, extract_animals_from_page, get_next_page_url, save_to_csv

class TestExtractAnimalsFromPage(unittest.TestCase):

    def setUp(self):
        # HTML-контент для тестирования
        self.page_content = '''
        <div class="mw-category-group">
            <a href="/wiki/Животное_А">Акула</a>
            <a href="/wiki/Животное_А">Антилопа</a>
        </div>
        <div class="mw-category-group">
            <a href="/wiki/Животное_Б">Бобер</a>
        </div>
        '''

    def test_extract_animals(self):
        result = extract_animals_from_page(self.page_content)

        # Проверяем, что данные по буквам правильно собраны
        self.assertEqual(result['А'], 2)
        self.assertEqual(result['Б'], 1)
        self.assertEqual(result['В'], 0)


class TestGetNextPageUrl(unittest.TestCase):

    def test_next_page_exists(self):
        # Пример HTML с кнопкой "Следующая страница"
        page_content = '''
        <a href="/wiki/Категория:Животные_по_алфавиту?from=Б" title="Следующая страница">Следующая страница</a>
        '''
        soup = BeautifulSoup(page_content, 'html.parser')
        next_page_url = get_next_page_url(soup)
        self.assertEqual(next_page_url, 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту?from=Б')

    def test_no_next_page(self):
        # Пример HTML без ссылки на следующую страницу
        page_content = ''
        soup = BeautifulSoup(page_content, 'html.parser')
        next_page_url = get_next_page_url(soup)
        self.assertIsNone(next_page_url)


class TestSaveToCSV(unittest.TestCase):

    def setUp(self):
        # Пример данных для теста, где животные только для букв "А" и "Б"
        self.animals_by_letter = defaultdict(int)
        self.animals_by_letter['А'] = 3
        self.animals_by_letter['Б'] = 5
        # Нет животных для "Г", "Д"

    @patch('csv.writer')
    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    def test_save_to_csv(self, mock_open, mock_writer):

        mock_file = mock_open()
        mock_csv_writer = MagicMock()

        mock_writer.return_value = mock_csv_writer

        save_to_csv(self.animals_by_letter)

        mock_open.assert_any_call('beasts.csv', mode='w', newline='', encoding='utf-8')

        mock_csv_writer.writerow.assert_any_call(['Буква', 'Количество животных'])

        mock_csv_writer.writerow.assert_any_call(['А', 3])
        mock_csv_writer.writerow.assert_any_call(['Б', 5])

        mock_csv_writer.writerow.assert_any_call(['Г', 0])
        mock_csv_writer.writerow.assert_any_call(['Д', 0])


class TestMainFunction(unittest.TestCase):

    @patch('solution.get_animal_category_page')
    @patch('solution.extract_animals_from_page')
    def test_main(self, mock_extract_animals, mock_get_page):

        mock_get_page.side_effect = [
            '<div class="mw-category-group"><a>Акула</a><a>Антилопа</a></div>',
            '<div class="mw-category-group"><a>Бобер</a></div>',
            None  # Никакой следующей страницы
        ]

        mock_extract_animals.side_effect = [
            {'А': 2},
            {'Б': 1}
        ]

        main()


        mock_get_page.assert_called()
        mock_extract_animals.assert_called()


if __name__ == '__main__':
    unittest.main()
