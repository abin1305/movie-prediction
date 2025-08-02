from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)

# Load dataset once when app starts
movie_dataset = {}
with open('indian movies.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        name = row['Movie Name'].strip().lower()
        lang = row['Language'].strip().lower()
        if lang in ['english', 'malayalam','assamese','bengali','gujarati','hindi','kannada','konkani','marathi','odia','punjabi','tamil','telugu ']:
            movie_dataset[name] = lang.title()  # e.g., "English" or "Malayalam"

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        movie = request.form['movie'].strip().lower()
        language = movie_dataset.get(movie)
        if language:
            result = f"✅ It's a {language} movie."
        else:
            result = "❌ Movie not found in offline dataset."
    return render_template('index.html', result=result)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
