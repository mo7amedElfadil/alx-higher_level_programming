#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i is not j and i < j:
            print("{:d}{:d}".format(i, j),
                  end=(", ", "\n")[i > 7])
