class Solution(object):
    def isValid(self,trees):
        dict1 = {}
        for i in range(10):
            dict1[i]=0
        for i in (set(trees)):
            dict1[i] = 1
        return dict1.values().count(1) <= 2


    def totalFruit(self, tree):

        if not tree:
            return 0
        if len(set(tree)) <= 2:
            return len(tree)


        max_win_size = 0

        current_win_end = 0
        current_win_start = 0

        while current_win_start> -1 and current_win_end < len(tree):

            if self.isValid(tree[current_win_start:current_win_end+1]):
                current_win_end +=1
            else:
                current_win_end += 1
                while not self.isValid(tree[current_win_start:current_win_end+1]):
                    current_win_start +=1

            if max_win_size < current_win_end-current_win_start:
                max_win_size = current_win_end - current_win_start
                max_win_start = current_win_start
        return max_win_size

a = Solution()
print a.totalFruit([3,3,3,1,2,1,1,2,3,3,4])
