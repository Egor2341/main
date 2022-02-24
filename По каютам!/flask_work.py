from flask import request, url_for, Flask, render_template

app = Flask(__name__)

user_list = input().split()


@app.route('/distribution')
def distribution():
    param = {}
    param['title'] = 'Домашняя страница'
    param['user_list'] = user_list
    return render_template('index.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
