import unittest

from test_with_gabri.filecounter import FileCounter


class FileCounterTests(unittest.TestCase):
    def test_directory_is_empty(self):
        file_counter = FileCounter()
        self.assertEqual(file_counter.count_file("/empty/dir"), 0)


if __name__ == '__main__':
    unittest.main()
