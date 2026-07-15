class Solution(object):
    def rearrangeArray(self, nums):
        n=len(nums)
        p=[]
        n=[]
        for num in nums :
            if num>0:
               p.append(num)
            else:
                n.append(num)   
        k=len(p)
        ans=[]
        for i in range(k):
            ans.append(p[i])
            ans.append(n[i])
        return ans     

