def solution(id_list, report, k):
    
    from collections import defaultdict

    # 신고 내용 중복 제거하기
    report = list(set(report))

    # 신고 당한 사람 : [신고한 사람들]
    reported_users = defaultdict(list)

    # 신고 목록을 순회하면서
    for content in report:

        user, reported_user = content.split()

        # 신고 당한 사람과 신고한 사람 정보를 담는다
        reported_users[reported_user].append(user)
    
    # 신고 처리 결과 메일을 받을 횟수를 담을 리스트
    answer = [0] * len(id_list)

    # 각각 몇 명이 신고했는지 순회하면서
    for report_list in reported_users.values():

        # 신고한 사람들의 수가 k보다 크거나 같으면
        if len(report_list) >= k:

            # id_list의 인덱스와 원소를 뽑아서
            for idx, user in enumerate(id_list):
            
                # user가 신고한 사람 목록에 없으면 넘어가고
                if user not in report_list:
                    continue
                
                # 있으면 answer의 같은 인덱스에 1을 더해준다
                answer[idx] += 1

    return answer