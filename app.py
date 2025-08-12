from urllib import request

from flask import Flask, render_template, request, url_for, redirect

from ApplicationsManager import ApplicationsManager

app = Flask(__name__)

applicationsMan = ApplicationsManager()
applicationsMan.add_entry(job_title="Junior Software Engineer", company="XiaTech", date=None)

print(applicationsMan.return_entry_list()[0].get_job_title())

@app.route('/')
def main_menu():  # put application's code here
    return render_template("index.html")

@app.route('/applications')
def applications():
    return render_template("applications.html", applications_list = applicationsMan.return_entry_list())

@app.route('/applications/new', methods=['GET', 'POST'])
def new_application():
    if request.method == "POST":
        applicationsMan.add_entry(request.form['job_title'], request.form['date'], request.form['company'])
        return redirect(url_for('applications'))
    return render_template("new_application.html")

if __name__ == '__main__':
    app.run()
