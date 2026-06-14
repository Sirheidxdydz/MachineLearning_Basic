def div_sum(*values, action):

    if not values:
        result = None
    else:
        result = values[0]

        for val in values[1:]:
            if action == "+":
                result += val
            elif action == "*":
                result *= val

    return result

func_call = div_sum(3, 2, 5, 11, 12, action = "+")
print(func_call)