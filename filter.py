def filter(input_str,criteria):
    answer_list=[]
    for string in input_str:
        if(criteria(string)):
            answer_list.append(string)
    return answer_list
    
def length_five(string):
    if(len(string)==5):
        return True
    else:
        return False
        
def print_result(input_str):
    for string in input_str:
        print(string)
    
lst_sample=['apple','grapes','mango']
result=filter(lst_sample,length_five)
print_result(result)

