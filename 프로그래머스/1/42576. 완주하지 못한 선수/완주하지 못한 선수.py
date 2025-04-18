def solution(participant, completion):
    completion_dict = dict()

    for person in completion:

        if person in completion_dict:
            completion_dict[person] += 1
        else:
            completion_dict[person] = 1

    for person in participant:

        if person in completion_dict:

            if completion_dict[person] > 1:
                completion_dict[person] -= 1
                continue

            completion_dict.pop(person)
        else:
            return person