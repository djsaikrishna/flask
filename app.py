from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def scrape_links():
    extracted_links = []

    if request.method == 'POST':
        url = request.form['url']
        if url:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a')
            extracted_links = [link.get('href') for link in links if link.get('href')]

    return render_template('index.html', links=extracted_links)

if __name__ == '__main__':
    app.run()
