import unittest
from main import check_straight, check_3ofa_kind, check_royal_flush, play_cards


class TestCheckStraight(unittest.TestCase):
    def test_straight(self):
        result = check_straight((12, 'SQ'), (14, 'SA'), (13, 'SK'))
        self.assertEqual(result, 14)
        result = check_straight((2, 'S2'), (4, 'S4'), (3, 'S3'))
        self.assertEqual(result, 4)
        result = check_straight((10, 'S10'), (9, 'S9'), (8, 'S8'))
        self.assertEqual(result, 10)

    def test_notstraight(self):
        result = check_straight((10, 'S10'), (4, 'S4'), (8, 'S8'))
        self.assertEqual(result, 0)
        result = check_straight((12, 'SQ'), (14, 'SA'), (8, 'S8'))
        self.assertEqual(result, 0)
        result = check_straight((2, 'S2'), (7, 'S7'), (3, 'S3'))
        self.assertEqual(result, 0)


class TestCheck3(unittest.TestCase):
    def test_3_ofa_kind_true(self):
        result = check_3ofa_kind((12, 'SQ'), (12, 'SQ'), (12, 'SQ'))
        self.assertEqual(result, 12)
        result = check_3ofa_kind((4, 'S4'), (4, 'S4'), (4, 'S4'))
        self.assertEqual(result, 4)
        result = check_3ofa_kind((2, 'S2'), (2, 'S2'), (2, 'S2'))
        self.assertEqual(result, 2)

    def test_3_ofa_kind_false(self):
        result = check_3ofa_kind((12, 'SQ'), (4, 'S4'), (12, 'SQ'))
        self.assertEqual(result, 0)
        result = check_3ofa_kind((10, 'S10'), (4, 'S4'), (8, 'S8'))
        self.assertEqual(result, 0)
        result = check_3ofa_kind((2, 'S2'), (4, 'S4'), (4, 'S4'))
        self.assertEqual(result, 0)


class TestCheckFlush(unittest.TestCase):
    def test_flush_true(self):
        result = check_royal_flush((12, 'SQ'), (14, 'SA'), (13, 'SK'))
        self.assertEqual(result, 14)
        result = check_royal_flush((14, 'SA'), (13, 'SK'), (12, 'SQ'))
        self.assertEqual(result, 14)

    def test_flush_false(self):
        result = check_royal_flush((12, 'SQ'), (4, 'S4'), (12, 'SQ'))
        self.assertEqual(result, 0)
        result = check_royal_flush((4, 'S4'), (4, 'S4'), (4, 'S4'))
        self.assertEqual(result, 0)


class TestResults(unittest.TestCase):
    def test_play_cards(self):
        result = play_cards((10, 'S10'), (9, 'S9'), (11, 'SJ'), (10, 'S10'), (9, 'S9'), (8, 'S8'))
        self.assertEqual(result, -1)
        result = play_cards((14, 'SA'), (14, 'SA'), (14, 'SA'), (10, 'S10'), (9, 'S9'), (8, 'S8'))
        self.assertEqual(result, 1)
        result = play_cards((14, 'SA'), (13, 'SK'), (12, 'SQ'), (12, 'SQ'), (13, 'SK'), (14, 'SA'))
        self.assertEqual(result, 0)
        result = play_cards((12, 'SQ'), (12, 'SQ'), (12, 'SQ'), (12, 'SQ'), (12, 'SQ'), (12, 'SQ'))
        self.assertEqual(result, 0)
        result = play_cards((12, 'SQ'), (8, 'S8'), (10, 'S10'), (12, 'SQ'), (3, 'S3'), (13, 'SK'))
        self.assertEqual(result, 0)
        result = play_cards((14, 'SA'), (13, 'SK'), (12, 'SQ'), (2, 'S2'), (7, 'S7'), (3, 'S3'))
        self.assertEqual(result, -1)
        result = play_cards((4, 'S4'), (4, 'S4'), (4, 'S4'), (2, 'S2'), (2, 'S2'), (2, 'S2'))
        self.assertEqual(result, -1)
        result = play_cards((14, 'SA'), (14, 'SA'), (14, 'SA'), (14, 'SA'), (13, 'SK'), (12, 'SQ'))
        self.assertEqual(result, 1)
        result = play_cards((10, 'S10'), (7, 'S7'), (6, 'S6'), (11, 'SJ'), (11, 'SJ'), (3, 'S3'))
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
