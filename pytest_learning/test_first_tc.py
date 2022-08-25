import pytest

def test_1():
    print('Its me')


def test_2():
    s  = 'aaabbbbbccddeffaaab'
    d ={}
    for i in s:
        if i in d:
            d[i]+= 1
        else:
            d[i]= 1

    print(d)
    for k,v in d.items():
        print(k,v)