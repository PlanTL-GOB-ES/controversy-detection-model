import json
import dateutil.parser
from datetime import datetime

#INPUT_PATH = './meneame.sample.json'
INPUT_PATH = '/gpfs/projects/bsc88/corpora/meneame/v1/s1/meneame_fix_controversy.json'
if __name__ == '__main__':
    smallest = datetime.now()
    counter = 0
    with open(INPUT_PATH, 'r', encoding='utf-8') as fin:
        line = fin.readline()
        i = 1
        while line:
            try:
                data = json.loads(line)
                if data['controversy']:
                    date = data['creationIsoDate']
                    date = dateutil.parser.isoparse(date)
                    date = date.replace(tzinfo=None)
                    counter = counter + 1
                    if smallest > date:
                        smallest = date
            except:
                print("Error parsing", i)
            line = fin.readline()
            i = i + 1
    print(smallest)
    print(counter)
