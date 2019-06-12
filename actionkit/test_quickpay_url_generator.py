from datetime import datetime
import re
import settings
import unittest
import utils

class PaymentUrlGeneratorTest(unittest.TestCase):
    def setUp(self):
        self.token_id = '3nmqoul2'
        self.akid = '.18715613.pOX3Jq'
        self.datetime_format = '%Y%m%d%H%M'
        self.hash_separator = '.'
        self.braintree_secret = settings.BRAINTREE_ONECLICK_SECRET
    def test_quickpay_url(self): #all of these values depend on that user being the specific one it is.
        url = utils.quickpay_url(self.token_id, self.datetime_format, self.akid, self.braintree_secret, self.hash_separator)
        self.assertIn("act.moveon.org/donate/civ-donation-quickpay?", url)
        self.assertIn("payment_hash=3nmqoul2", url)
        self.assertIn("&akid=.18715613.pOX3Jq", url)
        self.assertEqual(len(url), 128)

    def test_payment_hash(self):
        payment_hash = utils.payment_hash(self.token_id, self.datetime_format, self.braintree_secret, self.hash_separator)
        self.assertIn("3nmqoul2", payment_hash)
        self.assertRegexpMatches(payment_hash, ".{8}\.\d{12}\..{8}\..{10}")

    def test_append_hash(self):
        parts = [ self.token_id, '201901011111', '12345678']
        append_hash = utils._append_hash(self.hash_separator, self.braintree_secret, *parts)

    def test_oneclick_hash(self):
        contents = self.hash_separator.join([self.token_id, datetime.now().strftime(self.datetime_format), '01234567'])
        oneclick_hash = utils.oneclick_hash(self.braintree_secret, contents)

if __name__ == '__main__':
    unittest.main()