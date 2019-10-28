import random
import string
import writer
import general
#   An alphanumeric code generator


'''
Here we have info about three plans, with their names, prices, minutes, etc...
'''


def generate_plan():
    names = ["Essential", "Magneta", "Magneta Plus"]
    prices = [30, 50, 60]  # PLN
    minutes = [100, 120, -1]  # -1 means unlimited
    mbs = [15, 20, 25]  # in Gb
    launch_date = ["06.06.2016", "07.07.2017", "08.08.2018"]
    # TO-DO we need to add launched date just like the prices, minutes, etc...
    name = random.choice(names)
    price = None
    minute = None
    mb = None
    date = None
    if name == names[0]:
        price = prices[0]
        minute = minutes[0]
        mb = mbs[0]
        date = launch_date[0]
    elif name == names[1]:
        price = prices[1]
        minute = minutes[1]
        mb = mbs[1]
        date = launch_date[1]
    elif name == names[2]:
        price = prices[2]
        minute = minutes[2]
        mb = mbs[2]
        date = launch_date[2]

    return [name, price, minute, mb, date]


def generate_output():
    numeric_id = general.generate_id()
    plan = generate_plan()
    writer.export_data([numeric_id, plan[0], plan[1], plan[2], plan[3]])
