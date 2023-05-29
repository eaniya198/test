import requests
from lxml import etree

url = "https://eaniya198.github.io/test/index.html"  # 크롤링할 웹사이트 URL을 입력하세요.

# 웹페이지 요청
response = requests.get(url)
html = response.text

# HTML 파싱
parser = etree.HTMLParser()
tree = etree.fromstring(html, parser)

# XPath를 사용하여 요소 추출
div_elements = tree.xpath("/html/body/div")  # div 태그 요소들을 추출합니다.

for i, div in enumerate(div_elements, start=1):
    xpath_hcI = "./div[2]"  # hcD 클래스 요소의 위치를 XPath로 지정합니다.
    hcI_elements = div.xpath(xpath_hcI)  # div 태그 내의 hcI 클래스 요소들을 추출합니다.

    count = 0
    for hcI in hcI_elements:
        xpath_hls = "./div/div[contains(@class, 'hls') and contains(@class, 'ps0')]"
        hls_elements = hcI.xpath(xpath_hls)  # hcI 클래스 요소 내의 hls ps0 클래스 요소들을 추출합니다.
        count += len(hls_elements)

    print(f"/html/body/div[{i}]: {count}개")
