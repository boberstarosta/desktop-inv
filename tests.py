import unittest
from app.currency import Currency


class CurrencyCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_constructor(self):
        self.assertEqual(Currency(), Currency(0))
        self.assertEqual(Currency(""), Currency(0))
        self.assertEqual(Currency(0.001), Currency(0))
        self.assertEqual(Currency("1.234"), Currency(123))
        self.assertEqual(Currency("1,234"), Currency(123))
        self.assertEqual(Currency("1.235"), Currency(123))
        self.assertEqual(Currency(1.233), Currency(123))
        self.assertEqual(Currency(-123), -123)
        self.assertEqual(Currency(-12), -12)
        self.assertEqual(Currency(0), 0)
        self.assertEqual(Currency(12), 12)
        self.assertEqual(Currency(123), 123)
        self.assertRaises(ValueError, Currency, 1, 23)
        self.assertRaises(ValueError, Currency, 1, 2, 3)

    def test_cast(self):
        self.assertEqual(int(Currency(123)), 123)
        self.assertEqual(int(Currency(-123)), -123)
        self.assertEqual(float(Currency(123)), 123.0)

    def test_parse(self):
        self.assertEqual(Currency.parse(""), 0)
        self.assertEqual(Currency.parse("0"), 0)
        self.assertEqual(Currency.parse("1.23456"), 123)
        self.assertEqual(Currency.parse("-1,23"), -123)
        self.assertEqual(Currency.parse("-123"), -12300)
        self.assertEqual(Currency.parse("0.00"), 0)
        self.assertEqual(Currency.parse("1.23 PLN"), 123)
        self.assertEqual(Currency.parse("123"), 12300)
        self.assertEqual(Currency.parse("-1.23-"), -123)
        self.assertEqual(Currency.parse("+1.23"), 123)
        self.assertRaises(ValueError, Currency.parse, "-1.-23")
        self.assertRaises(ValueError, Currency.parse, "--1.23")
        self.assertRaises(ValueError, Currency.parse, "0.1.23")

    def test_to_str(self):
        self.assertEqual(Currency(123).to_str(), "1.23")
        self.assertEqual(Currency(-123).to_str(), "-1.23")
        self.assertEqual(Currency(100).to_str(), "1.00")
        self.assertEqual(Currency(-200).to_str(), "-2.00")
        self.assertEqual(Currency(-12).to_str(), "-0.12")
        self.assertEqual(Currency(12).to_str(), "0.12")

    def test_arithmetic(self):
        self.assertIsInstance(Currency(123) + Currency(321), Currency)
        self.assertIsInstance(Currency(123) - Currency(321), Currency)
        self.assertIsInstance(Currency(123) * Currency(321), Currency)
        self.assertIsInstance(Currency(123) // Currency(321), Currency)
        self.assertEqual(Currency(123) + Currency(-123), 0)
        self.assertEqual(Currency(123) - Currency(123), 0)
        self.assertEqual(Currency(123) * Currency(200), 24600)
        self.assertEqual(Currency(123) // Currency(123), 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)

