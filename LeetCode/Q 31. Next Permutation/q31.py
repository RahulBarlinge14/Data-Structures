class Solution(object):
    def nextPermutation(self,nums):
        x=-1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i]<nums[i+1]:
                x=i
                break
        badanumber=-1
        if(x!=-1):
            for i in range(len(nums) - 1, x, -1):
                if(nums[i]>nums[x]):
                    badanumber=i
                    break
            self.swap(x,badanumber,nums)
        self.reversee(x+1,nums)    
        print(nums)    

    def swap(self,x,badanumber,nums):
        temp = nums[x]
        nums[x]=nums[badanumber]
        nums[badanumber]=temp

    def reversee(self,x,nums):
        s=x
        e=len(nums)-1
        while s<e:
            temp=nums[s]
            nums[s]=nums[e]
            nums[e]=temp 
            s+=1
            e-=1   
        