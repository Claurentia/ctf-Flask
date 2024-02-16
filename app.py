from flask import Flask, render_template, send_from_directory
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/task1')
def task1():
    return render_template('task1.html')

@app.route('/task2')
def task2():
    return render_template('task2.html')

@app.route('/task3')
def task3():
    return render_template('task3.html')

@app.route('/task4')
def task4():
    return render_template('login.html')

@app.route('/task4/loginsuccess')
def login_success():
    return render_template('login_success.html')

@app.route('/task5')
def task5():
    return render_template('task5.html')

@app.route('/task6')
def task6():
    return render_template('task6.html')

@app.route('/task7')
def task7():
    return render_template('task7.html')

@app.route('/robots.txt')
def robots():
    return send_from_directory(app.static_folder, 'robots.txt')

@app.route('/hidden.html')
def hidden():
    return render_template('hidden.html')

@app.route('/task8')
def task8():
    return render_template('task8.html')

@app.route('/task9')
def task9():
    return render_template('task9.html')

@app.route('/task10')
def task10():
    return render_template('task10.html')

@app.route('/task11')
def task11():
    return render_template('task11.html')

@app.route('/task11/page10.html')
def page10():
    return render_template('pagesTask11/page10.html')

@app.route('/task11/page11.html')
def page11():
    return render_template('pagesTask11/page11.html')

@app.route('/task11/page14.html')
def page14():
    return render_template('pagesTask11/page14.html')

@app.route('/task11/page15.html')
def page15():
    return render_template('pagesTask11/page15.html')

@app.route('/task11/page16.html')
def page16():
    return render_template('pagesTask11/page16.html')

@app.route('/task11/page17.html')
def page17():
    return render_template('pagesTask11/page17.html')

@app.route('/task11/page18.html')
def page18():
    return render_template('pagesTask11/page18.html')

@app.route('/task11/page19.html')
def page19():
    return render_template('pagesTask11/page19.html')

@app.route('/task12')
def task12():
    return render_template('task12.html')

if __name__ == '__main__':
    app.run(debug=True)