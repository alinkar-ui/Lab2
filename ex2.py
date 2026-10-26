def find_min_max(temperatures):
    min_temp = min(temperatures)
    max_temp = max(temperatures)
    return [float(min_temp), float(max_temp)]

print(find_min_max([25.5, 30.2, 18.6, 27.0]))


def average(num1, num2):
    avg = float((num1 + num2) / 2)
    return [float(avg)]

print(average(11.2, 2.5))