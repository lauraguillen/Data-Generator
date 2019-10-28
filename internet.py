import random
import string
import writer
import general

#   An alphanumeric code generator


'''
Here we have info about three plans, with their names, prices, minutes, etc...
'''


def generate_internet_plan():
    names = ["200Mb", "500Mb", "1000Mb"]
    # we can use other representative names for them...
    prices = [90, 150, 300]  # PLN
    minutes = [200, 400, -1]  # -1 means unlimited
    bandwidth = [200, 500, 1000]  # in Mb/s
    launch_date = ['06/06/2016', '07/07/2017', '08/08/2018']
    name = random.choice(names)
    price = None
    minute = None
    mb = None
    if name == names[0]:
        price = prices[0]
        minute = minutes[0]
        mb = mbs[0]
    elif name == names[1]:
        price = prices[1]
        minute = minutes[1]
        mb = mbs[1]
    elif name == names[2]:
        price = prices[2]
        minute = minutes[2]
        mb = mbs[2]

    return [name, price, minutes, bandwidth, launch_date]


def generate_output():
    numeric_id = general.generate_id()
    plan = generate_plan()
    writer.export_data([numeric_id, plan[0], plan[1], plan[2], plan[3]])
