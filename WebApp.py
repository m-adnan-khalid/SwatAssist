from flask import Flask, request, render_template
from SwatAssistModel import find_most_similar_question
from main import postReplyToZendesk

app = Flask(__name__)

messages = {};
result = "";


@app.route('/')
def index():
    return render_template('index.html', messages=messages)


@app.route('/', methods=['POST'])
def get_answer():
    question = request.form['query']
    answer = find_most_similar_question(question)
    messages[question] = answer;
    return render_template('index.html', answer=answer, messages=messages)


@app.route('/zendesk-comments', methods=['GET'])
def zendesk():
    return render_template('zendesk.html', result=result)


@app.route('/zendesk', methods=['POST'])
def post_answer():
    result = "Answer is Posted";
    postReplyToZendesk();
    return render_template('zendesk.html', result=result)


if __name__ == '__main__':
    app.run()
