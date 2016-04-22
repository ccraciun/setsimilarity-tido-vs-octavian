import timeit
import random


def generate_doclist(docs=2**11, words=2**10, word_range=2**20):
    population = xrange(word_range)
    return {docId: set(random.sample(population, words)) for docId in xrange(docs)}


NUMBER = 5
REPEAT = 3

logfile = open('runbench{}.{}.csv'.format(NUMBER, REPEAT), 'w')


def run_case(docs, words, word_range):
    SETUP = (
        'import random;'
        'from {module} import {func} as func;'
        'from __main__ import generate_doclist;'
        'random.seed("tidovsoctavian");'
        'docs_list = generate_doclist({docs}, {words}, {word_range})'
    )

    octavian = timeit.repeat(
            "func(docs_list)",
            setup=SETUP.format(
                module='set_similarity_octavian',
                func='similarity',
                docs=docs, words=words, word_range=word_range),
            number=NUMBER, repeat=REPEAT)
    tido = timeit.repeat(
            "func(docs_list)",
            setup=SETUP.format(
                module='set_similarity_tido',
                func='print_similar_docs',
                docs=docs, words=words, word_range=word_range),
            number=NUMBER, repeat=REPEAT)

    return {'octavian': octavian, 'tido': tido}


def main():
    import json

    data = []
    print('NUMBER: {}, REPEAT: {}'.format(NUMBER, REPEAT))
    logfile.write('name, docs, words, word_range, result\n')
    for docs in (2**i for i in range(5, 12)):
        for words in (2**i for i in range(5, 11)):
                for word_range in (2**i for i in range(30, 19, -2)):
                    print('Running testcase docs: {} words: {} word_range: {}'.format(
                        docs, words, word_range))
                    for name, result in run_case(docs, words, word_range).items():
                        print('\t\t{}: {}'.format(name, result))
                        logfile.write('{}, {}, {}, {}, {}\n'.format(name, docs, words, word_range, result))
                        logfile.flush()
                        data.append({
                            'name': name,
                            'docs': docs,
                            'words': words,
                            'word_range': word_range,
                            'result': result})

    print(data)
    with open('data.json', 'w') as f:
        json.dump({'number': NUMBER, 'repeat': REPEAT, 'data': data}, f)
    logfile.close()


if __name__ == "__main__":
    main()
