import unittest
from unittest.mock import patch
from crawler_server import app, get_internal_links, crawl_website
from crawler_client import start_crawl
from unittest.mock import MagicMock

class TestCrawlerServer(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_internal_links(self):
        url = 'https://www.redhat.com/en'
        internal_links = get_internal_links(url)
        self.assertIsInstance(internal_links, dict)

    def test_crawl_website(self):
        url = 'https://www.redhat.com/en'
        with patch('crawler_server.requests.get') as mocked_get:
            mocked_get.return_value.status_code = 200
            mocked_get.return_value.text = '<html><body></body></html>'
            result = crawl_website(url)
            self.assertIsNone(result)

   

def test_crawl_endpoint(self):
    data = {'start_url': ''}

    with patch('crawler_server.crawl_website', new=MagicMock(return_value=None)) as mocked_crawl_website:
        response = self.app.post('/crawl', json=data)
        self.assertEqual(response.status_code, 200)
        mocked_crawl_website.assert_called_once_with(data['start_url'])


class TestCrawlerClient(unittest.TestCase):

    def test_start_crawl(self):
        start_url = 'https://www.redhat.com/en'
        with patch('crawler_client.requests.post') as mocked_post:
            mocked_post.return_value.status_code = 200
            mocked_post.return_value.json.return_value = {}
            result = start_crawl(start_url)
            self.assertIsInstance(result, dict)

if __name__ == '__main__':
    unittest.main()
