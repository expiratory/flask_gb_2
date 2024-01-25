from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/welcome', methods=['POST'])
def welcome():
    user_name = request.form.get('name')
    user_email = request.form.get('email')
    response = make_response(render_template('welcome.html', user_name=user_name))
    response.set_cookie('user_data', f'{user_name}|{user_email}')
    return response


@app.route('/logout')
def logout():
    response = make_response(redirect('/'))
    response.delete_cookie('user_data')
    return response


if __name__ == '__main__':
    app.run(debug=True)
