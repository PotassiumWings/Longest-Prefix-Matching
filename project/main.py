from project import trie

lines = open("routes.pfx2as", "r").readlines()
route_lengths = [100, 1000, 10000, 100000, 1000000]
for length in route_lengths:
    (ip_trie, end, legal) = trie.generate_trie(lines, length)
    print(len(legal))
    trie.ip_test(length, ip_trie, end, legal)

