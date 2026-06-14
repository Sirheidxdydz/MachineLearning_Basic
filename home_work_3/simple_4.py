import copy

def create_obj_dict(obj_list):

    new_obj_list = copy.deepcopy(obj_list)

    obj_dict = dict()

    for obj in new_obj_list:
        obj_dict[type(obj).__name__] = obj_dict.get(type(obj).__name__, []) + [obj]

    return obj_dict

input_list = ["A", 1, [1,2], "Sergei", 1, True, (1,2,3,5), False, None]
return_dict = create_obj_dict(input_list)
print(return_dict)


