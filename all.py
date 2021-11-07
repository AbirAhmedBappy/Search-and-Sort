# linear Search
position = 0
def linear_search (list,search_number):
    for i in range(0,len(list)):
        if list[i] == search_number :
            globals() ["position"] = i
            return True
    else :
        return False

list = [10,78,9,87,65,25,12,15,35,98]
search_number = int(input("Enter the number :"))
if linear_search(list,search_number) :
    print(search_number, "found at " , position+1)
else :
    print(search_number,"Not Found in List")
# binary search
position = 0
def binary_search(list,search_number) :
    lower = 0
    upper = len(list)

    for i in range(lower,upper):
        mid = (lower + upper) // 2
        if list[mid] == search_number :
            globals()['position']= mid
            return True
        else :
            if list[mid] > search_number :
                upper = mid
            else:
                lower = mid


list = [10,20,30,40,50,60,70,80,90,100]

search_number = 60
if binary_search(list,search_number) :
    print(search_number," Found at : " , position+1)
else :
    print(search_number, " Not Found in List")
# Bubble sort
def bubble_sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
list = [21,78,96,85,45,36,125,87,32,91,105]
bubble_sort(list)
print(list)
# selection sort
def selection_sort(list):
    for i in range(0,len(list)-1):
        minimum_value = i
        for j in range(i,len(list)):
            if list[j] < list[minimum_value] :
                minimum_value = j
        list[i],list[minimum_value] = list[minimum_value],list[i]
list = [21,78,96,85,45,36,125,87,32,91,105]
selection_sort(list)
print(list)
