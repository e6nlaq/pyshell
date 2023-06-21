def csplit(s: str) -> list:
    flag: bool = False
    tmp: str = ""
    ret: list = []
    for i in range(len(s)):
        if s[i] == '"':
            flag = not flag
        elif s[i] == " ":
            if flag:
                tmp += s[i]
            else:
                ret.append(tmp)
                tmp = ""
        else:
            tmp += s[i]

    if tmp != "":
        ret.append(tmp)

    return ret


if __name__ == "__main__":
    print(csplit('A "a b" b'))
