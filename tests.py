import unittest
import readers
import tsv_formatter
from constants import TEST_PATH


class Tests(unittest.TestCase):

    def test_read_json(self):
        result = readers.read_json(f'{TEST_PATH}jsonTestData.json')
        self.assertEqual(list(result['T2']), ['q', 'q', 'a'])
        self.assertIn(2, list(result['Z1']))

    def test_read_csv(self):
        result = readers.read_csv(f'{TEST_PATH}csvTestData.csv')
        self.assertIn(
            'Z3', result)
        self.assertIn(
            '1', result)

    def test_read_xml(self):
        result = readers.read_xml(f'{TEST_PATH}xmlTestData.xml')
        self.assertIn(
            'T3', result)
        self.assertEqual(list(result['T1']), ['E'])

    # Fails
    def test_tsv_formatter(self):
        result = tsv_formatter.format_data_tsv([
            readers.read_csv(f'{TEST_PATH}csvTestData.csv')])
        self.assertIn("Z2", result)
        self.assertEqual(list(result['Z3']), ['9o', 'u8', '4t'])


if __name__ == '__main__':
    unittest.main()
