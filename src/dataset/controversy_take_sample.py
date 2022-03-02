import json
import random



INPUT_PATH = './meneame_controversy.json'
OUTPUT_PATH = './meneame_controversy_sampled.json'
SAMPLE_RATE = 0.0652
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
                    writable_data = data
                    controversy_counter = controversy_counter + 1
                elif random.random() <= SAMPLE_RATE:
                    writable_data = data
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
