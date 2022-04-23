class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        l = 0
        h = n-1
        while l<=h:
            m = l + (h-l)//2
            if ord(target) >= ord(letters[m]):
                l = m+1
            else:
                h = m-1
        return letters[l%n]