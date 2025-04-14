def solution(n):
    
    word = str(n)
    word = word[::-1]

    answer = list(word)

    for i in range(len(answer)):
        answer[i] = int(answer[i])
    
    return answer