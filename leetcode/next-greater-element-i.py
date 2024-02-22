class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        nextGreater= [-1] * len(nums2)
        dict={}
        result=[]
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                nextGreater[stack.pop()] = nums2[i]
            stack.append(i)

        for i, num in enumerate(nums2):
            dict[num] = nextGreater[i]
        for num in nums1:
            result.append(dict[num])

        return result

                   


 


           





     

    




                     

                    


        