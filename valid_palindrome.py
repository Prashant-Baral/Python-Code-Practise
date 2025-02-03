class Solution:
    def uniqueoccur(self,s: str)->bool:
        new_str = ''.join(s.lower() for c in s if c.isalnum())
        left,right = 0,len(s)-1
        
        while(left<right):
            if (new_str[left] != new_str[right]):
                return False
            left+=1
            right-=1

        return True
       

if __name__ == "__main__":
    str = " "
    soln = Solution()
    print(soln.uniqueoccur(str))  