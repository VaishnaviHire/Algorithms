class Solution:


    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        result=[]
        def count(word):
            dict1 ={}
            for i in word:
                if i in dict1.keys():
                    dict1[i] +=1
                else:
                    dict1[i] = 1
            return dict1

        global_dict = {}
        for i in range(len(B)):
            curr_dict = count(B[i])
            for j in range(len(B[i])):
                if B[i][j] in global_dict.keys():
                    global_dict[B[i][j]] = max(curr_dict[B[i][j]], global_dict[B[i][j]])
                else:
                    global_dict[B[i][j]] = curr_dict[B[i][j]]


        for i in range(len(A)):
            word_dict = count(A[i])
            flag = 1
            print word_dict, global_dict
            for j in global_dict.keys():
                if j not in word_dict.keys():
                    flag =0
                    break
                elif j in word_dict.keys() and word_dict[j] < global_dict[j]:
                    flag = 0
                    break
            if flag == 1:
                result.append(A[i])


        return result


a = Solution()
print a.wordSubsets(["bcedecccdb","daeeddecbc","ecceededdc","edadadccea","ebacdedcea","eddabdacec","cddbecbeca","eeababedcc","bcaddcdbad","aeeeeabeea"],["cb","aae","ccc","ab","adc"])


