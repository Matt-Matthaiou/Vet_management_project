
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from datetime import date

import repos.active_case_repo as active_case
import calendar

callendar_blueprint = Blueprint('callendar', __name__)

@callendar_blueprint.route('/dashboard/calendar')
def callendar():
    cal = calendar.HTMLCalendar(firstweekday = 0)
    month = date.today().month
    year = date.today().year
    months = {}
    counter = 1
    while counter < 4:
        inst = cal.formatmonth(year, month)
        months[inst] = month
        month += 1
        counter += 1

    return render_template('/dashboard/calendar.html', months = months)

@callendar_blueprint.route('/dashboard/month/<id>')
def show_month(id):
    month = int(id)
    cal = calendar.Calendar(0)
    cal_month = cal.itermonthdates(2022, month)
    cases = active_case.select_all()
    month_header = calendar.month_abbr[month]
    return render_template('/dashboard/month.html', cal=cal_month, cases=cases, month_header=f'{month_header} 2022')

