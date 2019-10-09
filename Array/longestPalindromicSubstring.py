def longestPal(str1):

    arr=[[0 for i in range(len(str1))] for j in range(len(str1))]

    maxlen = 1

    for i in range(len(str1)):
        arr[i][i] = 1

    start = 0
    i = 0
    while i < len(str1) - 1:
        if (str1[i] == str1[i + 1]):
            arr[i][i + 1] = 1
            start = i
            maxlen = 2
        i = i + 1



    pallen = 3
    print(arr)
    while pallen <= len(str1):
        print(pallen)

        i = 0

        while i < (len(str1) - pallen + 1):

            j = i + pallen - 1

            if(arr[i+1][j-1] == 1 and str1[i] == str1[j]):
                arr[i][j] = 1


                if(pallen > maxlen):
                    start = i
                    maxlen = pallen

            i += 1

        pallen += 1

    return maxlen


print(longestPal("forgeeksskeegfor"))