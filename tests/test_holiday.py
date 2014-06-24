from unittest import TestCase

import holiday.holiday as holiday


class TestHoliday(TestCase):
    def test_match_recurring(self):
        rule = {
            'yearly': '1970-12-24'
        }

        tests = [
            ('2014-12-24', True),
            ('2014-11-23', False)
        ]

        result_set = [(holiday._match(test, rule), expected) for test, expected in tests]

        for result, expected in result_set:
            self.assertEquals(result, expected)
