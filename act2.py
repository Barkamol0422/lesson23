test_dict={"Codingal": 2,"Coding":2,"classes":2,"others":1}
print("Original dictionary: "+str(test_dict))
k=2
res=0
for key in test_dict:
    if test_dict[key]==k:
        res+=1
print("Frequency of 2 is: "+str(res))
        
