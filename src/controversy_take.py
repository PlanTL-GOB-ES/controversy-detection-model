import json
import dateutil.parser
from datetime import datetime


def int_attempt(data, key):
    value = None
    try:
        value = int(data[key])
    except:
        pass
        #print("int transform error")
    return value


def get_writable(data):
    writable_data = {
        'title': data['title'],
        'content': data['summary'],
        'controversy': data['controversy'],
        'date': data['creationIsoDate'],
        "positive_votes": int_attempt(data, 'positive_votes'),
        "negative_votes": int_attempt(data, 'negative_votes'),
        "number_comments": int_attempt(data, 'number_comments'),
        "karma": int_attempt(data, 'karma'),
        "clicks": int_attempt(data, 'clics'),
        "meneos": int_attempt(data, 'meneos'),
        'url_meneo': data['url'],
        'url_website': data['articleUrl'],
        'tags': data['tags'],
        'category': data['category']
    }
    return writable_data

#INPUT_PATH = './meneame_controversy.example.json'
SELECTED_DATE = dateutil.parser.parse('2006-01-17 15:39:45')
INPUT_PATH = '/gpfs/projects/bsc88/corpora/meneame/v1/s1/meneame_fix_controversy.json'
OUTPUT_PATH = './meneame_controversy.json'
if __name__ == '__main__':
    controversy_counter = 0
    controversy_not_counter = 0
    with open(INPUT_PATH, 'r', encoding='utf-8') as fin, \
            open(OUTPUT_PATH, 'w', encoding='utf-8') as fout:
        line = fin.readline()
        i = 1
        while line:
            try:
                data = json.loads(line)
                if data['controversy']:
                    writable_data = get_writable(data)
                    controversy_counter = controversy_counter + 1
                else:
                    date = data['creationIsoDate']
                    date = dateutil.parser.isoparse(date)
                    date = date.replace(tzinfo=None)
                    if SELECTED_DATE <= date:
                        writable_data = get_writable(data)
                        controversy_not_counter = controversy_not_counter + 1

                if writable_data:
                    fout.write(json.dumps(writable_data))
                    fout.write('\n')
                    writable_data = None
            except:
                print("Error parsing", i)
            line = fin.readline()
            i = i + 1
    print("Total", i)
    print("Not controversy", controversy_not_counter)
    print("Controversy", controversy_counter)