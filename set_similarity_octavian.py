
from collections import defaultdict


docs_list = {
    13: {14, 15, 100, 9, 3},
    16: {32, 1, 9, 3, 5},
    19: {15, 29, 2, 6, 8, 7},
    24: {7, 10}
}


def similarity(docs_list):
    # map: word -> list of containing docIds
    word_map = defaultdict(list)

    # map[docId1][docId2] -> length of intersection
    len_intersect = defaultdict(lambda: defaultdict(int))

    flat_list = docs_list.items()
    for sId, doc in flat_list:
        for word in doc:
            for docIdMatching in word_map[word]:
                len_intersect[sId][docIdMatching] += 1
            word_map[word].append(sId)

    # Note that here we only loop over docIds that are known to intersect.
    for docId in len_intersect.keys():
        for doc2Id in len_intersect[docId].keys():
            inter_len = len_intersect[docId][doc2Id]
            union_len = len(docs_list[docId]) + len(docs_list[doc2Id]) - inter_len
            _ = (docId, doc2Id, float(inter_len) / union_len)

similarity(docs_list)
