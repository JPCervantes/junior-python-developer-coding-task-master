import unittest
import docReaders
import TSVformatter
from constants import DATA_PATH


class Tests(unittest.TestCase):

    def test_jsonReader(self):
        self.assertEqual(docReaders.read_json(f'tests/jsonTestData.json'), {'T1': ('z', 'a', 'q'), 'T3': (
            'a', 'z', 'z'), 'T2': ('q', 'q', 'a'), 'Z1': (1, 2, 5), 'Z2': (32, 3, 2), 'F4': (5, 52, 40), 'F3': (3, 3, 6)})

    def test_csvReader(self):
        self.assertIn('Z3', docReaders.read_csv('tests/csvTestData.csv'))
        self.assertIn("1", docReaders.read_csv(
            'tests/csvTestData.csv'))

    def test_xmlReader(self):
        self.assertIn('T3', docReaders.read_xml('tests/xmlTestData.xml'))
        self.assertEqual(docReaders.read_xml(
            'tests/xmlTestData.xml'), {'Z1': ('TA',), 'Z2': ('F',), 'T3': ('R3',), 'T1': ('E',), 'H2': ('5',), 'H3': ('F3',)})

    def test_TSVformatter(self):
        self.assertEqual(TSVformatter.TSVformatter(
            docReaders.read_xml('tests/xmlTestData.xml'), {'H2': (5,), 'H3': ('F3',), 'T1': ('E',), 'T3': ('R3',), 'Z1': ('TA',), 'Z2': ('F',)}))


if __name__ == '__main__':
    unittest.main()
