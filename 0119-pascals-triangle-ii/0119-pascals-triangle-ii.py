class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        start = [1]
        cnt = 0
        while cnt < rowIndex:
            temp = [1] * (len(start)+1)
            for i in range(len(start) - 1):
                temp[i+1] = start[i] + start[i+1]

            start = temp
            cnt +=1

        return start
        
