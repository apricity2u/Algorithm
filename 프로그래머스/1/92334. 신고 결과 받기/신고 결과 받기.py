def solution(id_list, report, k):
    
    from collections import defaultdict
    
    #중복값 제거
    report = set(report)
    
    #신고 정보 담기
    reported_info = defaultdict(list)
    
    #신고당한 횟수 정보 담기
    reported_count = defaultdict(int)
    
    for content in report:
        user, reported_user = content.split()
        
        # 신고당한 사람 : 1 식으로 딕셔너리 만들기
        reported_count[reported_user] += 1
        # 신고한 사람 : [신고 당한 사람] 형태로 만들기
        reported_info[user].append(reported_user)
        
    
    answer = [0]*len(id_list)
    
    # id_list의 원소와 인덱스 뽑기
    for idx, user_id in enumerate(id_list):
        
        # 신고당한 사람과 신고당한 횟수 출력
        for reported_user, reported_sum in reported_count.items():
            
            # k번 이상 신고 당한 사람이 신고한 사람 목록에 있으면, answer에 추가
            if reported_sum >= k and reported_user in reported_info[user_id]:
                answer[idx] += 1
        
    return answer