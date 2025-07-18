class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = set()
        visited = [False] * len(candidates)
        
        def dfs(temp: List[int], sumv: int, cur):
            if sumv == target:
                result.add(tuple(temp[:]))
                return
            elif sumv > target:
                return                
            prev = 0
            for i in range(cur, len(candidates)):
                if not visited[i] and sumv < target and candidates[i] != prev:
                    visited[i] = True
                    temp.append(candidates[i])
                    sumv += candidates[i]
                    prev = candidates[i]
                    dfs(temp,sumv, i + 1)

                    sumv -= candidates[i]
                    temp.remove(candidates[i])
                    visited[i] = False
        
        dfs([],0, 0)

        return list(result)