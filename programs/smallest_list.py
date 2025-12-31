
def ret_smaller(l):
    
    smallest_list = l[0]

    for sub_list in l:
        if(len(sub_list)<len(smallest_list)):
            smallest_list = sub_list   


     
    return smallest_list


    



