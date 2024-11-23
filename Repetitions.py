string=input()
count=1
lst=[]
for i in range(len(string)-1):
    if string[i]==string[i+1]:
        count+=1
    elif string[i]!=string[i+1]:
        lst.append(count)
        count=1
lst.append(count)
print(max(lst))  

#     # if i not in dic:
#     #     dic[i]=1
#     # else:
#     #     dic[i]+=1
# a=list(dic.values())
# print(max(a))

