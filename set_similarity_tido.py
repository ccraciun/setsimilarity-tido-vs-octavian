from itertools import combinations
from collections import defaultdict

docs_list = {
    13: {14, 15, 100, 9, 3},
    16: {32, 1, 9, 3, 5},
    19: {15, 29, 2, 6, 8, 7},
    24: {7, 10}
}


def similarity(word_list_1, word_list_2):
    return 1.0 * len(word_list_1 & word_list_2) / len(word_list_1 | word_list_2)


def print_similar_docs(docs_list):
    # create dict of word id -> set of docs with that word
    word_dict = defaultdict(set)
    for doc_id, words in docs_list.iteritems():
        for word_id in words:
            word_dict[word_id].add(doc_id)

    # assemble set of doc pairs with nonzero similarity
    candidate_pairs = set()
    for similar_doc_ids in word_dict.values():
        for candidate in combinations(similar_doc_ids, 2):
            candidate_pairs.add(candidate)

    for (doc1, doc2) in candidate_pairs:
        _ = doc1, doc2, similarity(docs_list[doc1], docs_list[doc2])

print_similar_docs(docs_list)
