import unittest

from test_with_gabri.filecounter import FileCounter


class FileCounterTests(unittest.TestCase):
    def test_directory_is_empty(self):
        file_counter = FileCounter()
        self.assertEqual(file_counter.count_file("/empty/dir"), 0)

    def test_filecount_folder_has_12_files(self):
        file_counter = FileCounter()
        test_path = "/Users/dsa25/PycharmProjects/test_with_gabry/tests/resources/filecount"
        self.assertEqual(file_counter.count_file(test_path), 12)

    def test_minions_folder_has_62_files(self):
        file_counter = FileCounter()
        test_path = "/Users/dsa25/PycharmProjects/test_with_gabry/tests/resources/minions"
        self.assertEqual(file_counter.count_file(test_path), 62)


if __name__ == '__main__':
    unittest.main()
