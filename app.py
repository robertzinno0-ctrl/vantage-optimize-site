from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'vantage-optimize-secret-2024'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mens')
def mens():
    return render_template('mens.html')

@app.route('/womens')
def womens():
    return render_template('womens.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        flash('Message received! We\'ll be in touch within 24 hours.', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5056, debug=False)

@app.route('/peptides')
def peptides():
    return render_template('peptides.html')
