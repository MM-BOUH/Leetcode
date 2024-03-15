def calculateFN(n):
    dictionary = {
                    0:0,
                    1:1
                }
    for i in range(n+1):
        if i>1:
            dictionary[i] = dictionary[i-1] + dictionary[i-2]
    print(dictionary[n])
    # Or we can also do it for them 
    
calculateFN(8181)    