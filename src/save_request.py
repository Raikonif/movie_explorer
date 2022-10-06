import uuid
from datetime import datetime as dt
import csv
RELATIVE_PATH_TO_SAVE_REQUESTS = 'saved_requests/requests.csv'

def save_request(request_args):
    unique_identifier = uuid.uuid4()
    time_stamp = dt.strftime(dt.now(), '%Y-%m-%d %H:%M:%S')
    request_args = valid_input_arg = [(key, value) for key,value in request_args.items() if value is not None]
    request_args_to_plain_text = [' '.join(item) for item in request_args]

    with open(RELATIVE_PATH_TO_SAVE_REQUESTS, 'a', encoding='UTF-8', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow([unique_identifier, request_args_to_plain_text, time_stamp])