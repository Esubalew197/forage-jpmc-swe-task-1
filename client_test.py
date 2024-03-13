import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        # Calculate the price ratio
        ratio = getRatio(quotes[0]['top_ask']['price'], quotes[1]['top_bid']['price'])
        # Assert that the ratio is correct
        self.assertAlmostEqual(ratio, 121.2 / 120.48, delta=0.001)

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        # Calculate the price ratio
        ratio = getRatio(quotes[0]['top_ask']['price'], quotes[1]['top_bid']['price'])
        # Assert that the ratio is correct
        self.assertAlmostEqual(ratio, 119.2 / 117.87, delta=0.001)

    def test_getRatio_divideByZero(self):
        # Test when price_b is 0
        ratio = getRatio(100, 0)
        self.assertIsNone(ratio)

if __name__ == '__main__':
    unittest.main()
