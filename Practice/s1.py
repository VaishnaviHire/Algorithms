def minimalOperations(words):
    result = []
    for i in range(len(words)):
        result.append(0)
        char_list = list(words[i])
        for j in range(len(words[i])):

            if (j < len(words[i]) - 1 and char_list[j]==char_list[j+1]):
                char_list[j+1] =  "0"
                print(char_list)
                result[i] += 1

    return result

print(minimalOperations(["abdd","baaaab"]))