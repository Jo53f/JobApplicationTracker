from urllib import request

from flask import Flask, render_template, request, url_for, redirect

from ApplicationsManager import ApplicationsManager

app = Flask(__name__)

applicationsMan = ApplicationsManager()

@app.route('/')
def main_menu():  # put application's code here
    return render_template("index.html")

@app.route('/applications')
def applications():
    applicationsMan.load_data()
    return render_template("applications.html", applications_list = applicationsMan.return_entry_list())

@app.route('/applications/new', methods=['GET', 'POST'])
def new_application():
    if request.method == "POST":
        applicationsMan.add_entry(request.form['job_title'], request.form['date'], request.form['company'], request.form['job_board'])
        return redirect(url_for('applications'))
    return render_template("new_application.html")

@app.post('/applications/delete')
def delete_application():
    application_id = int(request.form['application_id'])
    application = applicationsMan.return_entry(application_id)
    applicationsMan.remove_entry(application)
    return redirect(url_for('applications'))

@app.route('/applications/update', methods=['GET', 'POST'])
def update_application():
    application_id = request.args.get('application_id', type=int)
    application = applicationsMan.return_entry(application_id)
    if request.method == "POST":
        applicationsMan.update_entry(
            application,
            job_title=request.form['job_title'],
            company=request.form['company'],
            date=request.form['date'],
            job_board=request.form['job_board'])
        return redirect(url_for('applications'))
    return render_template("update_application.html", application = application)

if __name__ == '__main__':
    app.run()
