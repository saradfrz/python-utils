from .log_utils import debug_log
import csv
import json
from .datetime_utils import dt_now


def read_file(filepath):
    f = open(filepath, "r", encoding="utf-8")
    return f.read()


def save_file(filepath, data):
    try:
        f = open(filepath, "w", encoding="utf-8")
        response = f.write(data)
        f.close()
        return True
    except Exception as e:
        debug_log(str(e))
        return False


def read_json(filepath):
    f = open(filepath, 'r', encoding='utf-8')
    return json.load(f)


def save_json(filepath, data):
    try:
        f = open(filepath, 'w', encoding='utf-8')
        f.write(json.dumps(data, ensure_ascii=False, indent=4))
        f.close()
        return True
    except Exception as e:
        debug_log(str(e))
        return False


def read_csv(filepath, delimiter):
    # Returns csv contents as a list of lists
    csvfile = open(filepath, newline='')
    csv_reader = csv.reader(csvfile, delimiter=delimiter)
    csv_contents = list(csv_reader)
    csvfile.close()
    return csv_contents


def read_csv_as_dict(filepath, delimiter):
    # Returns csv contents as a list of dicts
    csvfile = open(filepath, newline='')
    csv_reader = csv.DictReader(csvfile, delimiter=delimiter)
    csv_contents = list(csv_reader)
    csvfile.close()
    return csv_contents


def save_csv(filepath, data):
    # = data: list[lists]
    f = open(filepath, 'w', encoding='utf-8', newline='')
    wr = csv.writer(f, dialect='excel')
    wr.writerows(data)
    f.close()


def save_csv_dict(filepath, data):
    # = data: list[dicts]
    keys = data[0].keys()
    f = open(filepath, 'w', encoding='utf-8', newline='')
    dict_writer = csv.DictWriter(f, keys)
    dict_writer.writeheader()
    dict_writer.writerows(data)
    f.close()
