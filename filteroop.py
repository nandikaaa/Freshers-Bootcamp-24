class StringFilter:
    def __init__(self, input_str):
        self.input_str = input_str

    def filter(self, criteria_func):
        answer_list = []
        for string in self.input_str:
            if criteria_func(string):
                answer_list.append(string)
        return answer_list

class StringCriteria:
    def __init__(self, length_of_string):
        self.length_of_string = length_of_string

    def check_string_length(self, string_item):
        return len(string_item) == self.length_of_string

class StringPrinter:
    def __init__(self, input_str):
        self.input_str = input_str

    def print_to_terminal(self):
        for string in self.input_str:
            print(string)


lst_sample = ['apple', 'grapes', 'mango']
string_filter = StringFilter(lst_sample)
criteria = StringCriteria(length_of_string=6)
result = string_filter.filter(criteria.check_string_length)
printer = StringPrinter(result)
printer.print_to_terminal()
