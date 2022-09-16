import json
from collections import Counter

if __name__ == '__main__':
    # COMPARE BALANCED VS UNBALANCED, BECAUSE TITLE VS TITLE+SUMMARY TÉ MASSA POCA DIFERÈNCIA
    with open('models/t_s_bal/test_results_cont.txt', 'r') as file1:
        bal = file1.readlines()
        bal_results = [t.split('\t')[1].replace('\n', '') for t in bal][1:]
    with open('models/t_s_unbal/test_results_cont.txt', 'r') as file2:
        unbal = file2.readlines()
        unbal_results = [t.split('\t')[1].replace('\n', '') for t in unbal][1:]
    with open('data/split_20k/test.json', 'r') as fin:
        new_json = []
        for i,line in enumerate(fin.readlines()):
            d = json.loads(line)
            if bal_results[i] == 'CONTROVERSY':
                d['answer_bal'] = True
            else:
                d['answer_bal'] = False
            if unbal_results[i] == 'CONTROVERSY':
                d['answer_unbal'] = True
            else:
                d['answer_unbal'] = False

            new_json.append(d)
    print('Balanced:',Counter(bal_results))
    print('Unbalanced:',Counter(unbal_results))

    # compara resultats: matrix showing write results for balanced/positive, balanced/negative, unbalanced/postive, Unbalanced/negative

    # Hipòtesis: el unbalanced ho fa millor perquè tendeix a predir més negatius, i el test té més negatius

    with open('src/statistics/comparison_bal_unbal.json', 'w') as outfile:
        for item in new_json:
            outfile.write(json.dumps(item) + "\n")