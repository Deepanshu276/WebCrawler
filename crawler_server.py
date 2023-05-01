"""import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from collections import defaultdict

def get_internal_links(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        base_url = urlparse(url).scheme + '://' + urlparse(url).hostname

        internal_links = defaultdict(set)
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and not href.startswith('#'):
                full_url = urljoin(base_url, href)
                if urlparse(full_url).hostname == urlparse(url).hostname:
                    section = link.find_parent().get_text(strip=True)
                    if section.strip() != '':
                        internal_links[section].add(full_url)
    except Exception as e:
        print(f"Error while fetching internal links for {url}: {e}")
        internal_links = defaultdict(set)

    return internal_links

def crawl_website(start_url):
    visited = set()
    sections = defaultdict(set)
    queue = [start_url]

    while queue:
        url = queue.pop(0)
        if url not in visited:
            visited.add(url)
            internal_links = get_internal_links(url)
            for section, links in internal_links.items():
                sections[section].update(links)
            queue.extend(links)
            visited.add(tuple(internal_links))

    return sections


def print_sitemap(sections):
    for section in sections:
        print(section)
        print('-' * len(section))
        for link in sections[section]:
            print(link)
        print('')

if __name__ == '__main__':
    start_url = 'https://www.redhat.com/en'
    sections = crawl_website(start_url)
    print_sitemap(sections)

"""
"""import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from collections import defaultdict

def get_internal_links(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        base_url = urlparse(url).scheme + '://' + urlparse(url).hostname

        internal_links = defaultdict(set)
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and not href.startswith('#'):
                full_url = urljoin(base_url, href)
                if urlparse(full_url).hostname == urlparse(url).hostname:
                    section = link.find_parent().get_text(strip=True)
                    if section.strip() != '':
                        internal_links[section].add(full_url)
        return internal_links
    except Exception as e:
        print(f"Error while fetching internal links for {url}: {e}")
        return defaultdict(set)

def crawl_website(start_url):
    visited = set()
    sections = defaultdict(set)
    queue = [(start_url, 'start')]

    while queue:
        url, section = queue.pop(0)
        if url not in visited:
            visited.add(url)
            internal_links = get_internal_links(url)
            sections[section].update(internal_links[section])
            for link_section, links in internal_links.items():
                if link_section != section:
                    for link in links:
                        queue.append((link, link_section))

            # Print the current section and its links
            print(section)
            print('-' * len(section))
            for link in sections[section]:
                print(link)
            print('')

if __name__ == '__main__':
    start_url = 'https://www.redhat.com/en'
    crawl_website(start_url)
"""
"""import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from collections import defaultdict

def get_internal_links(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        base_url = urlparse(url).scheme + '://' + urlparse(url).hostname

        internal_links = defaultdict(set)
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and not href.startswith('#'):
                full_url = urljoin(base_url, href)
                if urlparse(full_url).hostname == urlparse(url).hostname:
                    section = link.find_parent().get_text(strip=True)
                    if section.strip() != '':
                        internal_links[section].add(full_url)
    except Exception as e:
        print(f"Error while fetching internal links for {url}: {e}")
        internal_links = defaultdict(set)

    return internal_links

def crawl_website(start_url, level=0, max_depth=3):
    if level > max_depth:
        return

    visited = set()
    sections = defaultdict(set)
    queue = [(start_url, 'start', level)]

    while queue:
        url, section, level = queue.pop(0)
        if url not in visited:
            visited.add(url)
            internal_links = get_internal_links(url)
            sections[section].update(internal_links[section])
            for link_section, links in internal_links.items():
                if link_section != section:
                    for link in links:
                        queue.append((link, link_section, level + 1))

            # Print the current section and its links
            print('  ' * level + section)
            print('  ' * level + '-' * len(section))
            for link in sections[section]:
                print('  ' * level + link)
            print('')

            # Recursively crawl each link in the current section
            for link in sections[section]:
                crawl_website(link, level + 1, max_depth)

if __name__ == '__main__':
    start_url = 'https://www.redhat.com/en'
    crawl_website(start_url)"""

from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from collections import defaultdict

app = Flask(__name__)
def get_internal_links(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        base_url = urlparse(url).scheme + '://' + urlparse(url).hostname

        internal_links = defaultdict(set)
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and not href.startswith('#'):
                full_url = urljoin(base_url, href)
                if urlparse(full_url).hostname == urlparse(url).hostname:
                    section = link.find_parent().get_text(strip=True)
                    if section.strip() != '':
                        internal_links[section].add(full_url)
    except Exception as e:
        print(f"Error while fetching internal links for {url}: {e}")
        internal_links = defaultdict(set)

    return internal_links


def crawl_website(start_url, level=0, max_depth=3):
    if level > max_depth:
        return

    visited = set()
    sections = defaultdict(set)
    queue = [(start_url, 'start', level)]

    while queue:
        url, section, level = queue.pop(0)
        if url not in visited:
            visited.add(url)
            internal_links = get_internal_links(url)
            sections[section].update(internal_links[section])
            for link_section, links in internal_links.items():
                if link_section != section:
                    for link in links:
                        queue.append((link, link_section, level + 1))

            # Print the current section and its links
            print('  ' * level + section)
            print('  ' * level + '-' * len(section))
            for link in sections[section]:
                print('  ' * level + link)
            print('')

            # Recursively crawl each link in the current section
            for link in sections[section]:
                crawl_website(link, level + 1, max_depth)

@app.route('/crawl', methods=['POST'])
def crawl():
    data = request.get_json()
    start_url = data.get('start_url')
    max_depth = data.get('max_depth', 3)

    if not start_url:
        return jsonify({'error': 'start_url is required'}), 400

    result = crawl_website(start_url, max_depth=max_depth)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)