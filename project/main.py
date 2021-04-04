from project import trie
from matplotlib import pyplot as plt


lines = open("routes.pfx2as", "r").readlines()
# route_lengths = [100, 1000, 10000, 100000, 1000000]
# route_lengths = range(100, 10100, 100)
route_lengths = range(10000, 110000, 10000)
generate_time = []
test_time = []
legal_count = []
for length in route_lengths:
    (ip_trie, end, legal, generate) = trie.generate_trie(lines, length)
    generate_time.append(generate)

    legal_count.append(len(legal))

    test = trie.ip_test(length, ip_trie, end, legal)
    test_time.append(test)

print(route_lengths)
print(generate_time)
print(test_time)
# print(legal_count)

plt.plot(route_lengths, generate_time, 'r', label="Generating time")
plt.plot(route_lengths, test_time, 'b', label="Testing time")
plt.xlabel('Routes count')
plt.ylabel('nanoseconds')
plt.legend()
plt.show()

