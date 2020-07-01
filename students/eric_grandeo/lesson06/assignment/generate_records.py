#5df44a54-8cca-4928-bc53-caabb23cf329,1,2,3,4,05/26/2015,
#bc337622-119c-445d-9282-e4b980201c03,2,3,4,5,08/02/2011,ao

#generate one million records

import uuid
from datetime import datetime, timedelta
from csv import writer
import random

def random_date():
    start_date = datetime(2010, 1, 1)
    end_date = datetime(2020, 6, 15)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    
    return random_date.strftime("%x")
    

def create_record(num_list):
    #up to a million
    with open('exercise.csv', 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        for i in range(100):
            del num_list[0]
            num_list.append(num_list[2] + 1)
            guid = str(uuid.uuid4())
            ao_choice = ['ao', '', '', '']
            #need to write to csv file
            #print([guid] + num_list + [random_date()] + [random.choice(ao_choice)])
            new_row = [guid] + num_list + [random_date()] + [random.choice(ao_choice)]
            csv_writer.writerow(new_row)

if __name__ == "__main__":
    create_record([10, 11, 12, 13])