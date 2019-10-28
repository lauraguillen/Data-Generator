import random
import client
import datetime
import general
import writer
from faker import Faker

fake = Faker()


def generate_call(launch_date):  # This isn't finished, the problem is, that we need to store the date when was call
    satisfaction = random.randint(1, 9)
    response_time = random.randint(3, 120)
    call_date = fake.date_between(start_date=launch_date, end_date="now")
    operator_phone = client.generate_phone('pl')
    call = [satisfaction, response_time, operator_phone, call_date]
    return call


def generate_output():
    call_id = general.generate_id()
    writer.export_data([general.generate_id(),  ])  #  ..............


