class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        countof5=0
        countof10=0
        for i in bills:
            if i==5:
                countof5+=1
            elif i==10:
                if countof5==0:
                    return False
                countof10+=1
                countof5-=1
            else:
                if (countof5>=1 and countof10>=1):
                    countof5-=1
                    countof10-=1
                elif countof5>=3:
                    countof5-=3
                else:
                    return False
        return True

        