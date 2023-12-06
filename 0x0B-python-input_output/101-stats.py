#!/usr/bin/python3
"""defining 101-stats module
takes input format:
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> \
            <file size>
Each 10 lines and after a keyboard interruption (CTRL + C),
    prints those statistics since the beginning:

    Total file size: File size: <total size>
    where is the sum of all previous (see input format above)
    Number of lines by status code:
        possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
        if a status code doesn’t appear, don’t print anything for this status code
        format: <status code>: <number>
        status codes should be printed in ascending order
"""


def print_stats():
    """print the stats from stdin according to fmt
    """
    from sys import stdin
    count = 0
    lst = []
    stat = [200, 301, 400, 401, 403, 404, 405, 500]
    size = 0
    df = {}
    df = df.fromkeys(stat, 0)
    for line in stdin:
        lst = line.split()
        size += int(lst[-1])
        if int(lst[-2]) in df:
            df[int(lst[-2])] += 1
            count += 1
        if count % 10 == 0:
            print(f"File size: {size}")
            for k, v in df.items():
                if v:
                    print(f"{k}: {v}")

if __name__ == "__main__":
    print_stats()
