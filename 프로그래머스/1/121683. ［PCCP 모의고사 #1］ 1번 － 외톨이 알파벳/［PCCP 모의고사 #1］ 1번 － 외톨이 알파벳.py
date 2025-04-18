def solution(input_string):

    from collections import Counter

    existed_alphabet = dict()

    for idx, alphabet in enumerate(input_string):

        if alphabet in existed_alphabet:
            existed_alphabet[alphabet].append(idx)
        else:
            existed_alphabet[alphabet] = [idx]

    loner = set()

    for alphabet, index_list in existed_alphabet.items():

        if len(index_list) == 1:
            continue

        for idx, index in enumerate(index_list):

            if idx > len(index_list) - 2:
                continue

            if index + 1 != index_list[idx + 1]:
                loner.add(alphabet)

    loner = list(loner)
    loner.sort()
    loner_string = ""

    for idx, alphabet in enumerate(loner):
        
        loner_string += alphabet

        if (idx == len(loner) -1):
            return loner_string

    else:
        return "N"