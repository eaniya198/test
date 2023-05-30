from flask import Flask, render_template_string
from bs4 import BeautifulSoup
import requests
import random

app = Flask(__name__)

def has_color(html):
    soup = BeautifulSoup(html, 'html.parser')
    elements = soup.find_all(style=lambda value: value and 'color:' in value)
    
    for element in elements:
        style = element.get('style', '')
        if 'color:' in style:
            color_value = style.split('color:')[-1].split(';')[0].strip().lower()
            if color_value in ['red']:
                return 'red'
            if color_value in ['blue']:
                return 'blue'
    
    return None


# @app.route('/')
# def parse_html():
#     url = 'https://eaniya198.github.io/test/index.html'
#     response = requests.get(url)
#     html_content = response.text
#     assign = random.randint(1, 180)
    
#     soup = BeautifulSoup(html_content, 'html.parser')
#     table = soup.select_one(f'body > div > table:nth-of-type({assign})')
    
#     color = has_color(html_content)

#     template = '''
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>GONGMA SKILLS - IE</title>
#         <style>
#             body {
#                 font-family: Arial, sans-serif;
#             }
            
#             .message {
#                 color: red;
#                 font-weight: bold;
#             }
            
#             .button {
#                 background-color: #4CAF50;
#                 border: none;
#                 color: white;
#                 padding: 10px 20px;
#                 text-align: center;
#                 text-decoration: none;
#                 display: inline-block;
#                 font-size: 16px;
#                 margin-top: 20px;
#                 cursor: pointer;
#             }
            
#             .button:hover {
#                 background-color: #45a049;
#             }
#         </style>
#         <script>
#             function reloadPage() {
#                 location.reload();
#             }

#             document.addEventListener("keydown", function(event) {
#                 if (event.keyCode === 13) {
#                     event.preventDefault();
#                     reloadPage();
#                 }
#             });
#         </script>
#     </head>
#     <body>
#         {% if color and color not in ['red', 'blue'] %}
#         <p class="message">예상 과제에유</p>
#         {% endif %}
#         {{ table|safe }}
#         <br>
#         <button class="button" onclick="reloadPage()">다음 새로운 문제로!</button>
#     </body>
#     </html>
#     '''
    
#     return render_template_string(template, table=str(table), color=color)


@app.route('/')
def parse_html():
    url = 'https://eaniya198.github.io/test/index.html'
    response = requests.get(url)
    html_content = response.text
    assign = random.randint(1, 180)
    
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.select_one(f'body > div > table:nth-of-type({assign})')
    content = table.select_one('tr:last-child td:last-child').prettify()



    color = has_color(html_content)

    template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>GONGMA SKILLS - IE</title>
        <style>
            body {
                font-family: Arial, sans-serif;
            }
            
            .message {
                color: red;
                font-weight: bold;
            }
            
            .button {
                background-color: #4CAF50;
                border: none;
                color: white;
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin-top: 20px;
                cursor: pointer;
            }
            
            .button:hover {
                background-color: #45a049;
            }
            
            .hidden-content {
                display: none;
            }
        </style>
        <script>
            function reloadPage() {
                location.reload();
            }

            document.addEventListener("keydown", function(event) {
                if (event.keyCode === 13) {
                    event.preventDefault();
                    reloadPage();
                }
            });
            
            function toggleContent() {
                var content = document.getElementById("content");
                var toggleButton = document.getElementById("toggleButton");
                if (content.style.display === "none") {
                    content.style.display = "block";
                    toggleButton.innerHTML = "내용 감추기";
                } else {
                    content.style.display = "none";
                    toggleButton.innerHTML = "클릭하여 내용 표시";
                }
            }
        </script>
    </head>
    <body>
        {% if color and color not in ['red', 'blue'] %}
        <p class="message">예상 과제에유</p>
        {% endif %}
        {{ table|safe }}
        <br>
        <button class="button" onclick="reloadPage()">다음 새로운 문제로!</button>
        <button id="toggleButton" class="button" onclick="toggleContent()">클릭하여 내용 표시</button>
        <div id="content" class="hidden-content" style="display: none;">
            <br>
            <p><b>추가 내용:</b></p>
            {{ content|safe }}
        </div>
        <br>
    </body>
    </html>
    '''

    return render_template_string(template, table=table, content=content, color=color)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8081')
