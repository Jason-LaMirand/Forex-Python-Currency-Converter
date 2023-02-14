from app import app
import unittest

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class CurrencyConverterTestCase(unittest.TestCase):

    def test_home_page(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Currency Converter</h1>', html)

    # def test_process(self):
    #     with app.test_client() as client:
    #         res = client.get('/answers')

    #         self.assertEqual(res.status_code, 302)
    #         self.assertEqual(res.location, 'http://localhost/')
