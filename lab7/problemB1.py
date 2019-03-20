###problem B1
def collect_those_less_than_x (x,num_list):
    new_list=[]
    for y in range(0,len(num_list)):
        if x > num_list[y]:
            new_list.append(num_list[y])
    return new_list


