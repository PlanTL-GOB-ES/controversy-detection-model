import json
from collections import defaultdict
import nltk.tokenize
from stop_words import get_stop_words
from nltk.corpus import stopwords
from tqdm import tqdm


def tokenize_remove_stop_words(text, stop_words):
    tokenized = [tok.lower() for tok in nltk.tokenize.word_tokenize(text, language='spanish')]
    return [token for token in tokenized if token not in stop_words and token.isalpha()]


def add_to_dict(words, dictionary):
    for word in words:
        dictionary[word] = dictionary[word] + 1


def print_top(d):
    print(sorted(d.items(), key=lambda x: x[1], reverse=True)[:10])


def save(d, name):
    with open(f'../output/{name}.json', 'w', encoding='utf-8') as fout:
        json.dump(d, fout)


def relative(a, b):
    ret = {k: v/(v+b[k])for k, v in a.items() if a[k] > 1 and b[k] > 1}
    return ret


def stats():
    word_positive_counts_title = defaultdict(int, json.load(open('../output/positive_title.json')))
    word_negative_counts_title = defaultdict(int, json.load(open('../output/negative_title.json')))
    word_positive_counts_summary = defaultdict(int, json.load(open('../output/positive_summary.json')))
    word_negative_counts_summary = defaultdict(int, json.load(open('../output/negative_summary.json')))
    print_top(word_positive_counts_title)
    print_top(word_negative_counts_title)
    print_top(word_positive_counts_summary)
    print_top(word_negative_counts_summary)
    print_top(relative(word_positive_counts_title, word_negative_counts_title))
    print_top(relative(word_negative_counts_title, word_positive_counts_title))
    print_top(relative(word_positive_counts_summary, word_negative_counts_summary))
    print_top(relative(word_negative_counts_summary, word_positive_counts_summary))


def compute_all():
    stop_words = list(get_stop_words('es'))  # About 900 stopwords
    nltk_words = list(stopwords.words('spanish'))  # About 150 stopwords
    stop_words.extend(nltk_words)

    word_positive_counts_title = defaultdict(int)
    word_negative_counts_title = defaultdict(int)
    word_positive_counts_summary = defaultdict(int)
    word_negative_counts_summary = defaultdict(int)
    with open('../data/meneame_controversy.json', 'r', encoding='utf-8') as fin:
        for element in tqdm(fin):
            try:
                element = json.loads(element)
                d = word_positive_counts_title if element['controversy'] else word_negative_counts_title
                add_to_dict(tokenize_remove_stop_words(element['title'], stop_words), d)
                d = word_positive_counts_summary if element['controversy'] else word_negative_counts_summary
                add_to_dict(tokenize_remove_stop_words(element['summary'], stop_words), d)
            except:
                print("Error")

    save(word_positive_counts_title, 'positive_title')
    save(word_negative_counts_title, 'negative_title')
    save(word_positive_counts_summary, 'positive_summary')
    save(word_negative_counts_summary, 'negative_summary')

    stats()


if __name__ == '__main__':
    # compute_all()
    stats()
