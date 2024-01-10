class stringFilter:
    def __init__(self, input_str):
        self.input_str = input_str

    def filter(self, criteria_func):
        answer_list = []
        for string in self.input_str:
            if criteria_func(string):
                answer_list.append(string)
        return answer_list

class stringCriteria:
    def check_string_length(length_of_string):
        predicate = lambda string_item: len(string_item) == length_of_string
        return predicate

class stringPrinter:
    def print_to_terminal(input_str):
        for string in input_str:
            print(string)

lst_sample = ['apple', 'grapes', 'mango']
string_filter = stringFilter(lst_sample)
criteria_func = stringCriteria.check_string_length(6)
result = string_filter.filter(criteria_func)
stringPrinter.print_to_terminal(result)
