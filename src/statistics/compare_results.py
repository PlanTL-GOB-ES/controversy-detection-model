import json
from collections import Counter
from sklearn.metrics import confusion_matrix, classification_report, f1_score

if __name__ == '__main__':
    # COMPARE BALANCED VS UNBALANCED, BECAUSE TITLE VS TITLE+SUMMARY TÉ MASSA POCA DIFERÈNCIA
    matrix  =[]
    with open('models/t_s_bal/test_results_cont.txt', 'r') as file1:
        bal = file1.readlines()
        bal_results = [t.split('\t')[1].replace('\n', '') for t in bal][1:]
    with open('models/t_s_unbal/test_results_cont.txt', 'r') as file2:
        unbal = file2.readlines()
        unbal_results = [t.split('\t')[1].replace('\n', '') for t in unbal][1:]
    with open('data/split_20k/test.json', 'r') as fin:
        new_json = []
        true_labels = []
        for i,line in enumerate(fin.readlines()):
            d = json.loads(line)
            result = []
            if d['controversy']:
                true_labels.append('CONTROVERSY')
            else:
                true_labels.append('NO_CONTROVERSY')

            if bal_results[i] == 'CONTROVERSY':
                d['answer_bal'] = True
                if d['controversy']:
                    result = ['BAL-RIGHT-TRUE']
                else:
                    result = ['BAL-WRONG-FALSE']
            else:
                d['answer_bal'] = False
                if d['controversy']:
                    result = ['BAL-WRONG-TRUE']
                else:
                    result = ['BAL-RIGHT-FALSE']

            if unbal_results[i] == 'CONTROVERSY':
                d['answer_unbal'] = True
                if d['controversy']:
                    result.append('UNBAL-RIGHT-TRUE')
                else:
                    result.append('UNBAL-WRONG-FALSE')
            else:
                d['answer_unbal'] = False
                if d['controversy']:
                    result.append('UNBAL-WRONG-TRUE')
                else:
                    result.append('UNBAL-RIGHT-FALSE')

            matrix.append(tuple(result))

            new_json.append(d)
    print('Balanced:',Counter(bal_results))
    print('Unbalanced:',Counter(unbal_results))
    matrix_counter = Counter(matrix)
    for line in matrix_counter.keys():
        #if line[0][-11:] != line[1][-11:]:
        print(line, matrix_counter[line])

    print(classification_report(true_labels, bal_results))
    print(classification_report(true_labels, unbal_results))

    #print(f1_score(true_labels, bal_results))
    #print(f1_score(true_labels, unbal_results))


    # compara resultats: matrix showing write results for balanced/positive, balanced/negative, unbalanced/postive, Unbalanced/negative

    # Hipòtesis: el unbalanced ho fa millor perquè tendeix a predir més negatius, i el test té més negatius

    with open('src/statistics/comparison_bal_unbal.json', 'w') as outfile:
        for item in new_json:
            outfile.write(json.dumps(item) + "\n")