class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")
       
# Runtime: 40 ms
# Memory Usage: 13.7 MB
