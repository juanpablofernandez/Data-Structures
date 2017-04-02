from find import find
import unittest


class TestFind(unittest.TestCase):
    def test_find_iterative(self):
        assert find("bob", "bob") == True
        assert find("BOB", "bob") == True
        assert find("bobcat", "bob") == True
        assert find("boBcat", "bob") == True
        assert find("catbob", "bob") == True
        assert find("catbob", "BoB") == True
        assert find("bocatboocatbobcatbo", "bob") == True
        assert find("akjdajbadabbokajdkabobobkajdn", "bob") == True
        assert find("ajdjadajaxjuenjxad", "ajax") == True

    def test_find_iterative_with_pattern_not_in_string(self):
        assert find("bo", "bob") == False
        assert find("bocat", "bob") == False
        assert find("catob", "bob") == False
        assert find("bocatboocatbocatbo", "bob") == False
        assert find("akjdajbadabbokajdkaboobkajdn", "bob") == False
        assert find("ajdjadajajuenjxad", "ajax") == False




if __name__ == '__main__':
    unittest.main()
