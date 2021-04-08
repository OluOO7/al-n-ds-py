def isanagram(str1, str2):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    match_found = 0
    if len(str1) == len(str2):
        for i in str1:
            if i in alphabets:
                if i in str2:
                    match_found += 1
                    #print(match_found)
                else:
                    match_found
                    #print(match_found)
            else:
                raise RuntimeError(f"{i} is not in the alphabets.")
        if match_found == len(str1):
            #print(match_found)
            return print(True)
        else:
            return print(False)
    else:
        raise RuntimeError("{} is {} characters long and {} is {} characters long and cannot be anagrams.".format(str1,len(str1),str2,len(str2)))
isanagram("abcd", "dcda")