# :(
g = [[12,34,45],[1,3,5], [23, 67,78]]
da = []
for i in g:
    h={}
    for k in i:
        h['i']=k
        da.append(h)
print(da)
# output 
[{'i': 45}, {'i': 45}, {'i': 45}, {'i': 5}, {'i': 5}, {'i': 5}, {'i': 78}, {'i': 78}, {'i': 78}]
# solved
# for i in g:
#     for k in i:
#         h={}
#         h['i']=k
#         da.append(h)