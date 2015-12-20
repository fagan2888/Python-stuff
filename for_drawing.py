def rat(values, ratio):
    index = 0
    print(values)
    for value in values:

        value = list(str(value))
        dot = value.index('.')
        end = float(''.join(value[dot+1:]))
        new_value = 0
        for v in value[:dot]:
            new_value += float(v)
        values[index] = round((new_value + end/16)*ratio, 1)

        index += 1

    return values


print(rat([5.4, 4.1, .4, .8, .15], 10.0/5.25))
