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
        
        # Call the summarizer function
        summary, original_text, len_original_text, len_summary, response_time, original_text_highlighted, summary_data = summerizer(rawtext)
        
        # Pass the summary and all intermediate data to the template
        return render_template('summary.html', 
                               summary=summary, 
                               original_text=original_text, 
                               len_original_text=len_original_text, 
                               len_summary=len_summary, 
                               response_time=response_time, 
                               original_text_highlighted=original_text_highlighted,
                               token=summary_data['token'], 
                               word_frequencies=summary_data['word_frequencies'], 
                               normalized_word_frequencies=summary_data['normalized_word_frequencies'], 
                               sentence_scores=summary_data['sentence_scores'])


if __name__ == "__main__":
    app.run(debug=True)