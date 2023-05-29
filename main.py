import requests
from bs4 import BeautifulSoup as bs

page = requests.get("https://eaniya198.github.io/test/index1.html")
soup = bs(page.text, "html.parser")

# elements = soup.select('div.esg-entry-content a > span')

print(soup)

# for index, element in enumerate(elements, 1):
# 		print("{} 번째 게시글의 제목: {}".format(index, element.text))
