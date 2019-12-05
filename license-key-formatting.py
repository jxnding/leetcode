class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace('-','').upper()
        leftover = len(S)%K
        if S=='': return ''
        
        ans = []
        for i in range(leftover):
            ans.append(S[i])
        if leftover>0:
            ans.append('-')
        for i in range(leftover,len(S),K):
            for j in range(i,i+K):
                ans.append(S[j])
            ans.append('-')
        del ans[-1]
        return ''.join(ans)