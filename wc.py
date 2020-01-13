import sys, json

def get_words(path):
    words = []
    f = open(path, encoding="utf-8")
    for line in f:
        for w in line.strip().split(" "):
            words.append(w.upper())
    f.close()
    return words


def count_words(path, search):
    count = 0
    for w in get_words(path):
        if w == search:
            count += 1
    return count


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 wc.py <file.txt> (ALL|<word>)")
        sys.exit(1)

    path = sys.argv[1]
    search = sys.argv[2].upper()

    if search.upper() == "ALL":
        counts = {}
        for word in get_words(path):
            counts[word] = count_words(path, word)
        print(json.dumps(counts, sort_keys=True, indent=2))
    else:
        print(count_words(path, search))


if __name__ == '__main__':
     main()
