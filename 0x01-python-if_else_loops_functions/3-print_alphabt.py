#!/usr/bin/python3
for a in range(97, 123):
    print((f"{a:c}", "")[a == ord('q') or a == ord('e')], end="")
