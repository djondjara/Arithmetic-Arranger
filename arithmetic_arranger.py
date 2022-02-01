
def arithmetic_arranger(problems, *opt_argument):

    number_of_problems = len(problems)

    if number_of_problems > 5:
        print("Error: Too many problems.")
        return

    arranged_problems = []
    first_row = []
    second_row = []
    third_row = []
    result = []

    # Loops through every string, splits them into elements and sorts them in different lists
    for x in problems:

        y = x.split()

        if y[1] == "+" or y[1] == "-":

            first_num = y[0]
            second_num = y[2]
            first_num_int = int(first_num)
            second_num_int = int(second_num)

            result_int = 0
            if y[1] == "+":
                result_int = first_num_int + second_num_int
            else:
                result_int = first_num_int - second_num_int

            result_str = str(result_int)
            lines = ""

            f_num_len = len(first_num)
            s_num_len = len(second_num)
            result_str_len = len(result_str)

            if f_num_len > s_num_len:
                dif = f_num_len - s_num_len
                second_num = y[1] + " " * dif + " " + y[2]

                # Looks for the bigger num to see how many lines to add
                lines += "-" * f_num_len + "--"
            else:
                second_num = y[1] + " " + y[2]
                lines += "-" * s_num_len + "--"

            first_row.append(first_num)
            second_row.append(second_num)
            third_row.append(lines)
            result.append(result_str)
        else:
            print("Error: Operator must be '+' or '-'.")
            return

    arranged_problems.append(first_row)
    arranged_problems.append(second_row)
    arranged_problems.append(third_row)
    if opt_argument:
        arranged_problems.append(result)

    n = max(len(x) for x in second_row)

    for row in arranged_problems:
        print("   ".join(x.rjust(n) for x in row))


numbers = ["32 - 698", "3801 - 2", "45 + 43", "123 + 49", "123 + 49"]

arithmetic_arranger(numbers, True)





