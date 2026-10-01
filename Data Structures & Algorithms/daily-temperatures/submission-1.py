class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Brute Stack 
        # n = len(temperatures)
        # res = []
        # for i in range (0, n):
        #     found = False
        #     for j in range(i+1, n):
        #         if  temperatures[j]>temperatures[i]:
        #             res.append(j-i)
        #             found = True
        #             break
        #     if not found:
        #         res.append(0)
        
        # print(res)

        # return res
    
    #stack solution
        stack = [] 
        res = [0]*(len(temperatures))
        for index,temp in enumerate(temperatures): 
            if len(stack)== 0:
                stack.append((temp,index))
            
            if stack[-1][0] > temp:
                stack.append((temp,index))
            else:
                while (len(stack) !=0  and  stack[-1][0] <temp ) :
                    print ("indexes" ,stack[-1][1] )
                    res[ stack[-1][1]] = index - stack[-1][1]
                    stack.pop()
                
                stack.append((temp,index))


        return res

                
        