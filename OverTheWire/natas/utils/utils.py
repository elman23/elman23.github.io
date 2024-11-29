from typing import List


def common_prefix(s1: str, s2: str) -> str:
    common = ''
    n = min(len(s1), len(s2))
    for i in range(n):
        if s2[i] == s1[i]:
            common += s2[i]
        else:
            break
    return common

def common_suffix(s1: str, s2: str) -> str:
    s1_reversed = s1[::-1]
    s2_reversed = s2[::-1]
    reversed_suffix = common_prefix(s1_reversed, s2_reversed)
    return reversed_suffix[::-1]


def common_prefix_list(l: List) -> str:
    if len(l) == 0:
        return ""
    prefix = l[0]
    for s in l[1:]:
        prefix = common_prefix(prefix, s)
    return prefix


def common_suffix_list(l: List) -> str:
    if len(l) == 0:
        return ""
    suffix = l[0]
    for s in l[1:]:
        suffix = common_suffix(suffix, s)
    return suffix


def test1():
    s1 = "asdfghjkl"
    s2 = "asdwertyyyr"
    assert common_prefix(s1, s2) == "asd"


def test2():
    s1 = "qwertyhjklfgh"
    s2 = "qwertyuiop"
    assert common_prefix(s1, s2) == "qwerty"


def test3():
    s1 = "asdfghjkl"
    s2 = "qettrtyghjkl"
    assert common_suffix(s1, s2) == "ghjkl"


def test4():
    s1 = "erterterttre"
    s2 = "aaaerttre"
    assert common_suffix(s1, s2) == "erttre"


def test5():
    s1 = ""
    s2 = "asdasd"
    assert common_prefix(s1, s2) == ""


def test6():
    s1 = ""
    s2 = "asd"
    assert common_suffix(s1, s2) == ""


def test7():
    s1 = "asd"
    s2 = "qwerty"
    assert common_prefix(s1, s2) == ""


def test8():
    s1 = "asd"
    s2 = "qwerty"
    assert common_suffix(s1, s2) == ""


def test9():
    l = ["asdqwe", "asdiu", "asd"]
    assert common_prefix_list(l) == "asd"


def test10():
    l = ["sdadqwe", "aqwe", "qwe"]
    assert common_suffix_list(l) == "qwe"


def run_tests():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    test9()
    test10()


if __name__ == '__main__':
    run_tests()