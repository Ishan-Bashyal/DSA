A=[1,2,3]
print(A)

#Modifying using indexing: O(1)
A[0]=5 

#Accessing using index: O(1)
print(A[0])

#Add in end: O(1)
A.append(4) 
print(A)

#Remove from end: O(1)
A.pop 
print(A)

#Insert: O(N)
A.insert(1, 0) #Inserting 0 on 1 index
print(A)

#Checking if array contains an element: O(N)
if 5 in A:
    print(True)








