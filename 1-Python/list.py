#-------------------------------- List Assignment---------------------------

#list sum
#write python program to add all the items in a list
def sum_list(item):
    sum=0
    for x in item:
        sum=sum+x
    return sum

list=[2,3,5,-6,7,8]
print(sum_list(list))


#write python program to multiply all the items in a list
def mul_list(item):
    mul=1
    for x in item:
        mul=mul*x
    return mul

list=[2,3,4,5]
print(mul_list(list))

##write python program to substraction all the items in a list
def sub_list(item):
    sub=0
    for x in item:
        sub=sub-x
    return sub

list=[2,3,4,5]
print(sub_list(list))


#Write python program to get the largest number from a list.

def largest_no(list):
    a=max(list)
    return a
list=[2,3,4,5]
print(largest_no(list))

#Write python program to get the smallest number from a list.

def smallest_no(list):
    a=min(list)
    return a
list=[2,3,4,5]
print(smallest_no(list))

###Write a python program to count the no of strings which satisfies
##the condition that the string length is 2 or more and the first and last char
#should be same
['abc' , 'xyz', 'aba', '1221']


def match_words(words):
    ctr=0
    for word in words:
        if len(word)>2 and word[0]==word[-1]:
            ctr+=1
    return ctr

print(match_words(['abc' , 'xyz', 'aba', '1221']))


"""
write a python program to get a list sorted in increasing 
order by the last element in each touple from a given list 
of non-empty tuples.

sample_list : [(2,5),(1,2),(4,4),(2,3),(2,1)]
Expected_Result : [(2,1),(1,2),(2,3),(4,4),(2,5)]
"""
def last(n):
    return n[-1]

def sort_list_last(tuples):
    result=sorted(tuples, key=last)
    return result

print(sort_list_last([(2,5),(1,2),(4,4),(2,3),(2,1)]))

#another method to sort using lambda method

def sort_tuples_by_last_element(tuples):
    return sorted(tuples, key=lambda x: x[-1])

tuples=[(2,5),(1,2),(4,4),(2,3),(2,1)]
print(sort_tuples_by_last_element(tuples))

#Write a program to remove duplicates from a list
#given the list a= [10,20,30,20,10,50,60,40,80,50,40]
# set remove all duplicates items


a= [10,20,30,20,10,50,60,40,80,50,40]
dup_items=set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)
        
print(dup_items)
print(uniq_items)

#another method

lst1= [10,20,30,20,10,50,60,40,80,50,40]
st1=set(lst1)
print(st1)
lst2=list(st1)
print(lst2)

#write a python program to clone or copy a list
original_list=[10,22,44,23,4]
new_list=list(original_list)
print(original_list)
print(new_list)

#Write a python program to find a list of word that are longer than 
# n from a given list of words

def long_words(n,str):
    word_len=[]
    txt=str.split(" ")
    #print(txt)
    for x in txt:
        if len(x)>n:
            word_len.append(x)
    return word_len
print(long_words(3,"The quick brown fox jumps over the lazy dog"))



#write a python function that takes two list and return
#True if they have at least one common member

def common_data(list1,list2):
    result= False
    for x in list1:
        for y in list2:
            if x==y:
                result=True
                return result
print(common_data([1,2,3,4,5],[5,6,7,8,9]))
print(common_data([1,2,3,4,5],[6,7,8,9]))


#write a python program to find the difference between two lists

list1=[1,3,5,7,9]
list2=[1,2,4,6,8]
diff1=list(set(list1)-set(list2))
diff2=list(set(list2)-set(list1))
print(diff1)
print(diff2)
total_diff = diff1 + diff2
print(total_diff)

#Write python program to convert list of character into a string 
#used in nlp

s=['a','b','c','d']
str1=''.join(s)
print(str1)

#Write a python program to find the index of an item in a specificed list.
num=[10,30,3,-6]
print(num.index(30))

#Write a python program to append a list to the second list.
list1=[1,2,3,0]
list2=['Red','Green','Black']
final_list =list1 + list2
print(final_list)