import timeit
import random


def generate_doclist(docs=2**11, words=2**10, word_range=(0, 2**20)):
    population = xrange(*word_range)
    return {docId: set(random.sample(population, words)) for docId in range(docs)}


if __name__ == "__main__":
    print("Octavian")
    print(timeit.repeat(
            "similarity(docs_list)",
            setup="""
from set_similarity_octavian import similarity;
from __main__ import generate_doclist;
docs_list = generate_doclist()
                """,
            number=1))

    print("Tido")
    print(timeit.repeat(
            "print_similar_docs(docs_list)",
            setup="""
from set_similarity_tido import print_similar_docs;
from __main__ import generate_doclist;
docs_list = generate_doclist()
                """,
            number=1))
