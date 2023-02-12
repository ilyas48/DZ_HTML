from flask import Flask, render_template
import utils

app = Flask(__name__)

"""Функция загружает и выводит весь список кандидатов"""

@app.route("/")
def index():
    candidates = utils.get_candidates_all()
    return render_template('list.html', candidates=candidates)

    """
    Загружает кандидата по запросу его (pk)
    если кандидат не был найден то выводит: Кандидат не найден!
    """

@app.route("/candidate/<int:pk>")
def get_candidate(pk):
    candidate = get_candidate_by_pk(pk)
    if not candidate:
        return 'None'

    result = '<br>'
    result += candidate['name'] + '<br>'
    result += candidate['position'] + '<br>'
    result += candidate['skills'] + '<br>'
    result += '<br>'

    return 'None'

"""Функция перебирает и выводит список кандитдатов по их навыкам"""

@app.route("/candidate/<skill>")
def get_candidate_by_skills(skill):
    candidates = get_candidate_by_skill(skill)
    result = '<br>'
    for candidate in candidates:
        result += candidate['name'] + '<br>'
        result += candidate['position'] + '<br>'
        result += candidate['skills'] + '<br>'
        result += '<br>'

    return 'None'


if __name__ == '__main__':
    app.run(debug=True)
