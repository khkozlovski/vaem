import unittest

from sync_folder import file_name, full_paths_of


class TestSyncFolder(unittest.TestCase):
    def test_extracts_file_name_from_full_path(self):
        self.assertEqual('c.txt', file_name('C:/a/b/c.txt'))

    def test_builds_full_path_to_empty_list_of_file_names(self):
        self.assertEqual([], full_paths_of([], 'C:/a/b'))

    def test_builds_full_path_to_files(self):
        self.assertEqual(['C:/a/b/a.txt', 'C:/a/b/b.txt'], full_paths_of(['a.txt', 'b.txt'], 'C:/a/b'))


if __name__ == '__main__':
    unittest.main()
