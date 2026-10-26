print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def calculate_bmi(height, weight):
    print('value of height is: ', height)
    print('value of weight is: ', weight)

    bmi = weight / (height * height)
    print('value of bmi is: ', bmi)

    if bmi < 18.5:
        print('BMI is underweight')
    elif bmi >= 18.5 and bmi < 24.9:
        print('BMI is normal')
    else:
        print('BMI is overweight')

    return bmi

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    user_input = input()
    str_list = user_input.split(",")

    float_list = []
    for item in str_list:
        float_list.append(float(item))
    return float_list

def calc_average_temperature(user_input):
    avg = sum(user_input) / len(user_input)
    return float(avg)

def calc_min_max_temperature(user_input):
    min_temp = min(user_input)
    max_temp = max(user_input)
    return [float(min_temp), float(max_temp)]

def main():
    display_main_menu()
    num_list = get_user_input()

    average = calc_average_temperature(num_list)
    min_max = calc_min_max_temperature(num_list)

    print("Average temperature:", average)
    print("Minimum temperature:", min_max[0])
    print("Maximum temperature:", min_max[1])

if __name__ == "__main__":
    main()