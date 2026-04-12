from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.secret_key = 'vantage-optimize-secret-2024'

# Email config
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME', 'info@vantagehealthusa.com')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD', '')
app.config['MAIL_DEFAULT_SENDER'] = 'info@vantagehealthusa.com'

mail = Mail(app)

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
        try:
            first_name = request.form.get('first_name', '')
            last_name = request.form.get('last_name', '')
            email = request.form.get('email', '')
            phone = request.form.get('phone', '')
            interest = request.form.get('interest', '')
            age_range = request.form.get('age_range', '')
            message = request.form.get('message', '')
            referral = request.form.get('referral', '')
            
            msg = Message(
                subject=f'New Lead: {first_name} {last_name} - {interest}',
                recipients=['info@vantagehealthusa.com'],
                body=f'''New contact form submission:

Name: {first_name} {last_name}
Email: {email}
Phone: {phone}
Interested In: {interest}
Age Range: {age_range}
Referral Source: {referral}

Message:
{message}
'''
            )
            mail.send(msg)
            flash('Message received! We\'ll be in touch within 24 hours.', 'success')
        except Exception as e:
            print(f'Email error: {e}')
            flash('Message received! We\'ll be in touch within 24 hours.', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html')

@app.route('/peptides')
def peptides():
    return render_template('peptides.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5056, debug=False)
