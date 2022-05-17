def equal(str1, str2):
    arr1 = list(str1.lower())
    arr2 = list(str2.lower())
    arr1 = sorted(arr1, key=str)
    arr2 = sorted(arr2, key=str)
    if len(arr1) != len(arr2):
        return False
    else:
        for i in range(0,len(arr2)):
            if arr1[i] != arr2[i]:
                return False
    return True


str1= "bilent"
str2 = "listen"
print(equal(str1,str2))