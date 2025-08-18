class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fac = [1]
        for i in range(1,n+1):
            fac.append(fac[i-1]*i)

        visited = [False] * (n+1)
        s = ""
        for i in range(n-1,-1,-1):

            cnt = 1
            while fac[i] < k:
                cnt +=1
                k -=fac[i]
            

            c = 0
            for j in range(1,n+1):
                if visited[j] == False:
                    c +=1
                    if c == cnt:
                        visited[j] = True
                        s+=  str(j)
        return s






                