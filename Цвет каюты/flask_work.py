from flask import request, url_for, Flask, render_template

app = Flask(__name__)


@app.route('/distribution/<sex>/<int:age>')
def distribution(sex, age):
    param = {}
    param['title'] = 'Цвет каюты'
    print(sex, age)
    if sex == "female":
        if age < 21:
            param["image"] = "http://127.0.0.1:8080/static/img/kid.png"
            param['color'] = '#EDA06E'
        else:
            param["image"] = "http://127.0.0.1:8080/static/img/adult.png"
            param['color'] = "#E96916"
    elif sex == "male":
        if age < 21:
            param["image"] = "http://127.0.0.1:8080/static/img/kid.png"
            param["color"] = "#3578ED"
        else:
            param["image"] = "http://127.0.0.1:8080/static/img/adult.png"
            param["color"] = "#0F3475"
    return render_template('index.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
