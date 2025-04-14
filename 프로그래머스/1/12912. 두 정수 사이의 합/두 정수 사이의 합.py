def solution(a, b):
    start = min(a, b)
    end = max(a, b)
    answer = 0
    
    for i in range(start, end + 1):
        answer += i
    
    return answer