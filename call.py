import random
import client
import datetime
import general
import writer


def generate_call(launch_date):  # This isn't finished, the problem is, that we need to store the date when was call
    satisfaction = random.randint(1, 9)
    response_time = random.randint(3, 120)
    #  TO-DO if that's a first launch, random date starting from launch date, we write it, and only then generate others
    year = random.randint(launch_date.year, datetime.date.today().year)
    month = random.randint(launch_date.month, datetime.date.today().month)
    day = random.randint(launch_date.day, datetime.date.today().day)
    f = open("date.txt", "r")
    f_read = f.read()
    if len(f_read) < 1:
        f = open("date.txt", "w")
        f.write(launch_date)
    else:
        call_date = f_read
    operator_phone = client.generate_phone('pl')
    call = [satisfaction, response_time, operator_phone]
    return call


def generate_date(plan_name, launch_date):
    f = open(plan_name+".txt", "r")
    date = datetime.date(f.read())
    f.close()
    if date > launch_date:
        date = datetime.date(date.year, date.month, date.day+1)
        f = open(launch_date, " ")
        calls_number = random.randint(1, 30)


def generate_output():
    call_id = general.generate_id()
    writer.export_data([general.generate_id(),  ])  #  ..............


