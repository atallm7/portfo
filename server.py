from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/process_form', methods=['POST'])
def process_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        # Add your email sending logic here if needed

        # Redirect to thank_you.html
        return redirect('/thank_you')

    # Redirect to home page if not a POST request
    return redirect('/')

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')
