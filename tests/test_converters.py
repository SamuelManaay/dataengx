import unittest
from dataengx import csv_to_json
import os
import json

class TestConverters(unittest.TestCase):
    def setUp(self):
        self.sample_csv = "tests/sample.csv"
        self.output_json = "tests/output.json"
        os.makedirs("tests", exist_ok=True)
        with open(self.sample_csv, "w") as f:
            f.write("name,age\nAlice,30\nBob,25\n")

    def test_csv_to_json(self):
        csv_to_json(self.sample_csv, self.output_json)
        self.assertTrue(os.path.exists(self.output_json))
        with open(self.output_json) as f:
            data = json.load(f)
            self.assertEqual(len(data), 2)
            self.assertEqual(data[0]['name'], 'Alice')

    def tearDown(self):
        os.remove(self.sample_csv)
        os.remove(self.output_json)

if __name__ == "__main__":
    unittest.main()
