def solution(clothes):
    clothes_dict = dict()

    for cloth in clothes:

        cloth_name = cloth[0]
        cloth_type = cloth[1]

        if cloth_type in clothes_dict:
            clothes_dict[cloth_type].append(cloth_name)
        else:
            clothes_dict[cloth_type] = [cloth_name]

    cloth_cnt = 1

    for cloth_names in clothes_dict.values():

        cloth_cnt *= len(cloth_names) + 1

    return cloth_cnt - 1
