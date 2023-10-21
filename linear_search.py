# Linear Search Algorithme
def linear_search(arr,var):
    isInsideList = False
    for i in list(arr):
        if (i == var):
           isInsideList = True
           break
    return isInsideList
    
var = int(input("\n\nEnter The variable that You Searching for>>: "))
our_list = [8 , 99 , 9 , 2 , 0 , 12 , 15 , 16 , 20 , 22 , 1 , 7 , 8 , 999, 532 , 21]
if linear_search(our_list,var):
    print(f"\nYes {var} is Inside the list\n")
else: 
    print(f"\nSorry {var} is not Inside the list\n")