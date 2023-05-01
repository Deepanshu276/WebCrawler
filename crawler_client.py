import requests

def start_crawl(start_url, max_depth=3):
    data = {
        'start_url': start_url,
        'max_depth': max_depth
    }
    response = requests.post('http://localhost:5000/crawl', json=data)
    return response.json()

if __name__ == '__main__':
    start_url = input("Enter the URL to be crawled: ")
    max_depth = int(input("Enter the maximum depth for crawling (default is 3): ") or 3)
    result = start_crawl(start_url, max_depth)
    print(result)
