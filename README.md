# WebCrawler

WebCrawler is a Python-based web crawler that recursively crawls a website and prints out the internal links found on each page. It uses Flask for the web server and requests, BeautifulSoup, and urllib for crawling the website.

# Installation

1. Clone the Repositery

```
git clone https://github.com/Deepanshu276/WebCrawler

```

2. Install the Required Packages

```
pip3 install -r requirements.txt

```

# Usage

1. Start the server by running the following command:

```
python3 crawler_server.py 

```

2. In a separate terminal window, start the client by running the following command:

```
python3 crawler_client.py

```
3. Enter the URL to be crawled and the maximum depth for crawling (default is 3). Depth here means how much level of crawling the user want

4. The client will send a POST request to the server with the start URL and maximum depth, and the server will recursively crawl the website and print out the internal links found on each page on the terminal.

Crawled Link will be displayed as a sitemap in the terminal as follows

![Screenshot from 2023-05-01 21-18-25](https://user-images.githubusercontent.com/56041032/235481617-b889c4de-218c-4b91-a9b4-91f3878ef130.png)

# Testing

use the following command to run the unit test

```
python3 -m unittest test_crawler.py

```

# Limitations

This has some problem with docker image and hence it is still not created but will be resolved soon.
