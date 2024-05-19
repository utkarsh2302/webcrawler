import requests
from bs4 import BeautifulSoup
from collections import Counter
url = 'http://www.poornima.org'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
links = [a.get('href') for a in soup.find_all('a', href=True)]
link_counts = Counter(links)
sorted_links = link_counts.most_common()
for link, frequency in sorted_links:
    print(f"{link}: {frequency}")
