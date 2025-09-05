import io
from urllib import request

from flask import Flask, render_template, request, url_for, redirect, Response, render_template_string
from matplotlib import pyplot as plt

from ApplicationsManager import ApplicationsManager, data_table, pie_chart
from Status import Status

app = Flask(__name__)

applicationsMan = ApplicationsManager()
"""Initialise the ApplicationsManager"""

@app.route('/')
def main_menu():
    """
    The main menu page.

    Returns
    -------
    render_template("index.html")
    """
    return render_template("index.html")

@app.route('/applications', methods=['GET', 'POST'])
def applications():
    applicationsMan.load_data()
    applications_list = applicationsMan.return_entry_list()
    status_filter = 0
    if request.method == "POST":
        status_filter = int(request.form['status_filter'])

        if status_filter != 0:
            status_filter = Status(status_filter)
            applications_list = applicationsMan.Status_filter(status_filter)
    return render_template(
        "applications.html",
        applications_list = applications_list,
        status_list = Status,
        current_status = status_filter if status_filter else 0
    )

@app.route('/applications/new', methods=['GET', 'POST'])
def new_application():
    if request.method == "POST":
        applicationsMan.add_entry(
            request.form['job_title'],
            request.form['date'],
            request.form['company'],
            request.form['job_board'],
            Status(int(request.form['application_status']))
        )
        return redirect(url_for('applications'))
    return render_template("new_application.html", status_list = Status)

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
            job_board=request.form['job_board'],
            status=Status(int(request.form['application_status'])))
        return redirect(url_for('applications'))
    return render_template("update_application.html", application = application, status_list = Status)

@app.route('/applications/insight', methods=['GET'])
def insight():
    applicationsMan.load_data()
    return render_template(
        "insight.html",
        applications_list = applicationsMan.return_entry_list(),
        status_table = data_table(applicationsMan.status_insight(), ['No. Applications']),
        job_board_table = data_table(applicationsMan.job_board_insight(), ['Job Boards']),
        status_list = Status,
    )

@app.route('/applications/insight/status_pie_chart.svg')
def status_insight():
    fig = applicationsMan.status_pie_chart()
    output = io.BytesIO()
    fig.savefig(output, format='svg')
    plt.close(fig)
    output.seek(0)

    return Response(output.getvalue(), mimetype='image/svg+xml')

@app.route('/applications/insight/job_board_pie_chart.svg')
def job_board_insight():
    fig = applicationsMan.job_board_pie_chart()
    output = io.BytesIO()
    fig.savefig(output, format='svg')
    plt.close(fig)
    output.seek(0)

    return Response(output.getvalue(), mimetype='image/svg+xml')

@app.route('/applications/insight/<int:status>')
def job_board_status_split_pie_chart(status: int = Status.APPLIED.value):
    status = Status(status)
    accepted = applicationsMan.job_boards_status(status)
    fig = pie_chart(accepted.values(), accepted.keys(), f'{status.name.capitalize()} applications')
    output = io.BytesIO()
    fig.savefig(output, format='svg')
    plt.close(fig)
    output.seek(0)
    return Response(output.getvalue(), mimetype='image/svg+xml')

@app.route('/applications/insight/table/<int:status>')
def job_board_status_split_table(status: int = Status.APPLIED.value):
    status = Status(status)
    jobs = applicationsMan.job_boards_status(status)
    table = data_table(jobs, [f"{status.name.capitalize()} applications"])
    return render_template_string(table)

if __name__ == '__main__':
    app.run()
