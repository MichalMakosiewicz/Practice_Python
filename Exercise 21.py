import requests
from bs4 import BeautifulSoup

base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")

for story_heading in soup.find_all(class_="story-heading"):
    if story_heading.a:
        with open('Tytuly.txt', 'a') as open_file:
            open_file.write((story_heading.a.text.replace("\n", " ").strip()) + '\n')
    else:
        with open('Tytuly.txt', 'a') as open_file:
            open_file.write((story_heading.contents[0].strip()) + '\n')