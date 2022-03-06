


# from array import array


# l1=[0]
# l2=[0]
# lt = []

# numeroString1=""
# numeroString2=""
# numeroStringTotal=""

# for n1 in range(len(l1)):
#     numeroString1 += str(l1[len(l1)-n1-1])

# for n2 in range(len(l2)):
#     numeroString2 += str(l2[len(l2)-n2-1])

# numeroStringTotal = str(int(numeroString1) + int(numeroString2))
# #print(numeroStringTotal)

# for n3 in range(len(numeroStringTotal)):
#     lt.append(int(numeroStringTotal[len(numeroStringTotal)-1-n3]))




class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

l1 = ListNode(2,ListNode(4,ListNode(3,None)))
l2 = ListNode(5,ListNode(6,ListNode(4,None)))

lt = []
numeroString1=""
numeroString2=""
numeroStringTotal=""
it1=0
it2=0
i=0
lista = ListNode(0,None)
lista2 = lista

while l1 != None:
    numeroString1 += str(l1.val)
    l1 = l1.next
    it1+=1

while l2 != None:
    numeroString2 += str(l2.val)
    l2 = l2.next
    it2+=1

numeroStringTotal = str(int(numeroString1[::-1]) + int(numeroString2[::-1]))
print(numeroStringTotal)

for n3 in range(len(numeroStringTotal)):
    lt.append(ListNode(int(numeroStringTotal[len(numeroStringTotal)-1-n3]),None))

i=0     
for node in range(len(lt)):
    lista.val = lt[i].val
    if node < len(lt)-1:
        lista.next = lt[i+1]
        lista = lt[i+1]
        i+=1

print(lista2.val,lista2.next.val,lista2.next.next.val)

# for l in range(len(lt)):
#     print(""+str(lt[l].val)+" -> "+str(lt[l].next.val))