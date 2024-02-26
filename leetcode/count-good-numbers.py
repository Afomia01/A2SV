MOD=10**9+7
class Solution:
    def power(self, base,pow):     
        if pow==1:
            return base
        if pow<=0:
            return 1
        if pow%2==0:
            return (self.power(base,pow//2)**2)%MOD 
        else:
            return (base* self.power(base,(pow-1)//2)**2)%MOD

    def countGoodNumbers(self, n: int) -> int:
     
        #return  (pow(5, (ceil(n/2)))) * pow(4,(n//2)) %MOD
        x= ceil(n/2)
        y=n//2
        return (self.power(5,x)*self.power(4,y))%MOD


           
        
        