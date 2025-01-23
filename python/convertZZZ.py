class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if (numRows == 1):
            return s
        result = ""
        s_len = s.__len__()#给定字符串的长度
        num = numRows * 2 - 2#一个循环的长度
        for row in range(numRows):#以行数建立循环，行数为给定的
            col=0
            while row + col < s_len:
                result += s[row + col]
                if (row!=0 and row!=numRows-1 and col+num-row<s_len):
                    result+=s[col+num-row]
                # if (row != 0 and row != numRows - 1 and col + num - row < s_len):
                #     result += s[col + num - row]
                col += num
        return result
    

s = "0123456789"
numRows=4
xx=Solution()
res=xx.convert(s,numRows)
print(res)

#%%
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):return s
        r,j,k=[""]*numRows,0,1
        for i in s:
            r[j]+=i
            j+=k
            if j==0 or j==numRows-1:k=-k
        return "".join(r)
    
    
#%%
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        newlist = ['' for _ in range(numRows)]
        flag = -1
        start = 0
        for i in s:
            newlist[start] += i
            if start == 0 or start == numRows - 1:
                flag  = -flag
            start += flag
        return ''.join(newlist)
    
#%% ***比较好的***

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows<2:
            return s
        res = ['' for i in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i==0 or i == numRows -1:
                flag = -flag # flag 代表行索引变化的方向 即 是减小还是增加
            i += flag
        return ''.join(res)