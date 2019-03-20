###problem B2
def reverse_list(lst):
    rev_lst=[]
    i = len(lst)
    for x in range(1,i+1):
        rev_lst.append(lst[-x])
    return rev_lst

