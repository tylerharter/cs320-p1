import sys

def main():
    assert len(sys.argv) == 3 # TODO: give friendly warning instead
    path = sys.argv[1]
    search = sys.argv[2] # TODO: support wildcards

    count = 0
    f = open(path, encoding="utf-8")
    for line in f:
        words = line.split(" ")
        for word in words:
            if word == search:
                count += 1
    f.close()

    print(count)


if __name__ == '__main__':
     main()
