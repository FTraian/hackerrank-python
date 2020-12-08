def minion_game(string):
    v_score = 0  # vowel score
    c_score = 0  # consonants score

    # for i in range(0, len(string)):
    #     for j in range(i + 1, len(string) + 1):
    #         if string[i] in 'AEIOU':
    #             v_score += 1
    #         else:
    #             c_score += 1
    for i in range(0, len(string)):
        if string[i] in 'AEIOU':
            v_score += len(string) - i
        else:
            c_score += len(string) - i
    if v_score > c_score:
        print('Kevin ' + str(v_score))
    elif c_score > v_score:
        print('Stuart ' + str(c_score))
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)
