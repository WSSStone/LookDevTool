import os

def handle_spaced_dir(argv:list) -> str:
    res = ''
    n = len(argv)
    for i in range(1, n):
        res += argv[i]
        if i != n - 1:
            res += ' '
    return f'{res}'