class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        org0 = [ None for _ in derived ]
        org0[0] = 0
        for k in range(len(derived) - 1):
            org0[k+1] = derived[k] ^ org0[k]
        if org0[-1] ^ org0[0] == derived[-1]:
            return True
        
        org1 = [ None for _ in derived ]
        org1[0] = 1
        for k in range(len(derived) - 1):
            org1[k+1] = derived[k] ^ org1[k]
        if org1[-1] ^ org1[0] == derived[-1]:
            return True
        
        return False