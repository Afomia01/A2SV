class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        hashmap = {}
        ans = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                key = i+j
                if key in hashmap:
                    hashmap[key].append(mat[i][j])
                else:
                   hashmap[key]=[mat[i][j]]
   
        for key in hashmap:
           
            if key%2!=0:
                ans.extend(hashmap[key])
            else:
                ans.extend(hashmap[key][::-1])
              
        return ans




        