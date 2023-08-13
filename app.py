from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        output_file = "output.txt"

        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        links = soup.find_all("a")

        with open(output_file, "w") as f:
            for link in links:
                href = link.get("href")
                if href:
                    f.write(href + "\n")

        return render_template('index.html', links=links, output_file=output_file)

    return render_template('index.html', links=[])

if __name__ == '__main__':
    app.run(debug=True)
