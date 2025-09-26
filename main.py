from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    quote = None
    if request.method == 'GET':
        quote = get_quote()
    return render_template("index.html", quote = quote)

def get_quote():
    api_key = "h0rfvZ7vBeVbYe0gsNYR8g==e31pGlEbKMo2j8EZ"
    url = "https://api.api-ninjas.com/v1/quotes"
    response = requests.get(url, headers={"X-Api-Key": api_key})
    data = response.json()
    return data[0]

if __name__ == "__main__":
    app.run(debug=True)