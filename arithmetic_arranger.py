# Create a function that receives a list of strings that are arithmetic problems
# and returns the problems arranged vertically and side-by-side.
# The function should optionally take a second argument.
# When the second argument is set to True, the answers should be displayed.


def arithmetic_arranger(problems, flag=False):

    num_of_problems = len(problems)

    # Checks if the number of problems is no more than 5
    if num_of_problems > 5:

        # Error message for too many problems
        print("Error: Too many problems.")
        return
    valid_operator = False

    # Different list for every row
    arranged_problems = []
    first_row = []
    second_row = []
    third_row = []
    result = []

    # Loops through every string, splits them into numbers and operators and sorts them in different lists
    for problemStr in problems:

        elem_in_str = problemStr.split()

        # Checks if the operator is + or - in the string
        if elem_in_str[1] == "+" or elem_in_str[1] == "-":

            # Converts strings nums to integers to calc the result
            first_num = elem_in_str[0]
            second_num = elem_in_str[2]

            if len(first_num) > 4 or len(second_num) > 4:
                print("Error: Numbers cannot be more than four digits.")
                break

            try:
                a = int(first_num)
                b = int(second_num)

            except ValueError:
                return print("Error: Numbers must only contain digits.")

            first_num_int = int(first_num)
            second_num_int = int(second_num)

            # Performs addition or subtraction
            result_int = 0
            if elem_in_str[1] == "+":
                result_int = first_num_int + second_num_int
            else:
                result_int = first_num_int - second_num_int

            result_str = str(result_int)
            lines = ""

            # Checks which number is bigger
            f_num_len = len(first_num)
            s_num_len = len(second_num)
            result_str_len = len(result_str)
            if f_num_len > s_num_len:
                dif = f_num_len - s_num_len
                second_num = elem_in_str[1] + " " * dif + " " + elem_in_str[2]

                # Looks for the bigger num to see how many lines to add
                lines += "-" * f_num_len + "--"
            else:
                second_num = elem_in_str[1] + " " + elem_in_str[2]
                lines += "-" * s_num_len + "--"

            first_row.append(first_num)
            second_row.append(second_num)
            third_row.append(lines)
            result.append(result_str)

        # Error message when operator is different from + or -
        else:
            print("Error: Operator must be '+' or '-'.")
            return

    arranged_problems.append(first_row)
    arranged_problems.append(second_row)
    arranged_problems.append(third_row)
    arranged_problems.append(result)

    for x, i in enumerate(second_row):
        num_len2 = len(i)
        len1_new = first_row[x].rjust(num_len2)
        len2_new = result[x].rjust(num_len2)
        first_row[x] = len1_new
        result[x] = len2_new

    final_result = []
    final_result.append("    ".join(x.rjust(len(x)) for x in first_row))
    final_result.append("    ".join(x.rjust(len(x)) for x in second_row))
    final_result.append("    ".join(x.rjust(len(x)) for x in third_row))
    if flag is True:
        final_result.append("    ".join(x.rjust(len(x)) for x in result))

    for i in final_result:
        print(i)



