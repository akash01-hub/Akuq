from flask import Flask, render_template, request, redirect

app = Flask(__name__)

questions = []  # Simple in-memory storage

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        question = request.form['question']
        if question:
            questions.append(question)
        return redirect('/')
    return render_template('index.html', questions=questions)

if __name__ == '__main__':
    app.run(debug=True)


