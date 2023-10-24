from flask import Flask, render_template, url_for, request, redirect
import csv


app = Flask(__name__)
print(__name__)



@app.route("/")
def my_home():
    return render_template('./index.html')


@app.route("/thankyou.html")
def html_page():
    return render_template('./thankyou.html')

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        Subject = data['name']
        message = data['message']
        file = database.write(f'\n{email},{Subject},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        Subject = data['name']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, Subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong'

