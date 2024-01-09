def filter(input_str,criteriaFunc):
    answer_list=[]
    for string in input_str:
        if(criteriaFunc(string)):
            answer_list.append(string)
    return answer_list
    
def checkStringOfLength(length_of_string):
    predicate=lambda string_item:len(string_item)==length_of_string
    return predicate
        
def printToTerminal(input_str):
    for string in input_str:
        print(string)
    
lst_sample=['apple','grapes','mango']
result=filter(lst_sample,checkStringOfLength(5))
printToTerminal(result)

