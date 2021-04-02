import random
import time


def generate_trie(ip_lines, router_size):
    print("Total routes: " + str(router_size))
    ip_trie_tot = 1
    ip_trie = [[0 for j in range(0, 2)] for i in range(0, 32 * router_size + 10)]
    end = ["" for i in range(0, 32 * router_size + 10)]
    legal = set()

    print("generating")
    generate_time = time.time()

    for index in range(0, len(ip_lines), len(ip_lines) // router_size + 1):
        ip_line = ip_lines[index]
        cmd = ip_line.strip("\n").split("\t")
        (ips, ip, count, ip_cur) = (list(map(int, cmd[0].split("."))), 0, int(cmd[1]), 1)
        mask = 0
        for x in ips:
            ip = ip * 256 + x

        for i in range(0, count):
            mask = mask << 1 | 1
            c = ip >> (31 - i) & 1
            if ip_trie[ip_cur][c] == 0:
                ip_trie_tot += 1
                ip_trie[ip_cur][c] = ip_trie_tot
            ip_cur = ip_trie[ip_cur][c]
        for i in range(count, 32):
            mask <<= 1
        end[ip_cur] = ip_line

        legal_start = ip & mask
        legal_end = legal_start + (1 << (32 - count))
        for i in range(legal_start, min(legal_end, legal_start + 10)):
            legal.add(i)
    print("! generate time: " + str(time.time() - generate_time))
    return ip_trie, end, legal


def ip_test(length, trie, end, legal):
    list_legal = list(legal)
    test_time = time.time()
    for j in range(0, length):
        ip_index = random.randint(0, len(list_legal))
        ip = list_legal[ip_index]
        (cur, ans) = (1, 0)
        for i in range(0, 32):
            c = ip >> (31 - i) & 1
            if trie[cur][c] == 0:
                break
            cur = trie[cur][c]
            if end[cur] != "":
                ans = cur
        # print(end[ans], end="")
    print("! test time: " + str(time.time() - test_time))

