from flask import Flask, render_template, request
from text_summary import summerizer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        summary, original_text, len_original_text, len_summary, response_time, original_text_highlighted = summerizer(rawtext)
        
    return render_template('summary.html', summary=summary, 
                           original_text=original_text, 
                           len_original_text=len_original_text, 
                           len_summary=len_summary, 
                           response_time=response_time, 
                           original_text_highlighted=original_text_highlighted)

if __name__ == "__main__":
    app.run(debug=True)