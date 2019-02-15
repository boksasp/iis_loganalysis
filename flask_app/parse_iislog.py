
import pandas as pd
import uuid
import sys
import os
from datetime import datetime


def run_parse():

    number_of_bars = 20
    logfile_name = "u_ex190122.log"

    startTime = datetime.now()

    def sanitise_log_file(file_name):
        print("Sanitising log file - removing comments and extra header rows...")
        added_header = False
        sanitised_log_file_name = str(uuid.uuid4())
        with open(file_name, 'r+') as f:
            with open(sanitised_log_file_name, 'w') as output:
                i = 1
                for line in f:
                    if line.startswith("#"):
                        if line.startswith("#Fields:") and not added_header:
                            line = line.replace("#Fields: ", "")
                            added_header = True
                        elif line.startswith("#Fields:") and added_header:
                            continue
                        elif line.startswith("#"):
                            continue
                        
                    output.write(line)
                    i += 1
        
        return sanitised_log_file_name


    sanitised_log_file_name = sanitise_log_file(logfile_name)

    columns = [
        'time',
        'c-ip',
    ]
    data = pd.read_csv(sanitised_log_file_name, delim_whitespace=True, header=0, usecols=columns)
    os.remove(sanitised_log_file_name)


    plot_values = data['c-ip'].value_counts()[:number_of_bars]

    plot_data = {}

    for pair in plot_values.items():
        plot_data[pair[0]] = pair[1]

    return plot_data
