import re


def arithmetic_arranger(problems, show_result = False):

    error = check_for_errors(problems)

    if error:
        print(error)
        return error
    else:
        components = componentize(problems, show_result)

        lines = make_lines_from(components)

        print_grid_from(lines)

        return lines


def componentize(problems, show_result):
    spacer = " "
    dash = "-"
    line_break = "\n"
    message = ""
    operator = ""
    operator_spacing = 1
    components_list = []
    for problem in problems:
        splited_problem = problem.split(spacer)

        check_for_errors(problem)

        operator = splited_problem[1]
        operator_spacing = len(operator)
        first = len(splited_problem[0])
        second = len(splited_problem[2])
        spacing = (first if first > second else second) + operator_spacing

        first_spacing = (spacing - first) + operator_spacing
        second_spacing = spacing - second
        calc = str(eval(problem))
        result_spacing = (spacing - len(calc)) + operator_spacing

        first_line = f"{spacer * first_spacing}{splited_problem[0]}"
        second_line = f"{splited_problem[1]}{spacer * second_spacing}{splited_problem[2]}"
        dashes = f"{dash * (spacing + operator_spacing)}"
        
        result = ((result_spacing * spacer) + calc) if show_result else ""
        
        components = [first_line, second_line, dashes, result]
        components_list.append(components)
    return components_list


def make_lines_from(components):
    lines = []
    proxy_list = []
    number_of_lines = 4
    space_between = " " * 4

    for i in range(number_of_lines):
        for component in components:
            proxy_list.append(component[i])
        lines.append(space_between.join(proxy_list))
        proxy_list = []
    
    return lines


def print_grid_from(lines):
    line_break = "\n"
    print(line_break.join(lines))


def check_for_errors(problems):
    pattern = r"\D"

    if len(problems) > 5:
        return error(1)  

    for problem in problems:
        split_problem = problem.split(" ")
        if "+" not in problem and "-" not in problem:
            return error(2)

        if re.search(pattern, split_problem[0]) or re.search(pattern, split_problem[2]):
            return error(3)

        if len(split_problem[0]) > 4 or len(split_problem[2]) > 4:
            return error(4)


def error(number):
    error_message = "no error"
    match number:
        case 1:
            error_message = "Error: Too many problems."
        case 2:
            error_message = "Error: Operator must be '+' or '-'."
        case 3:
            error_message = "Error: Numbers must only contain digits."
        case 4:
            error_message = "Error: Numbers cannot be more than four digits."
        case _default:
            error_message = f"uncaught error number {number}"

    return error_message


test =  ["1001 + 11", "22 + 22", "33 + 3003"]

arithmetic_arranger(test, True)
