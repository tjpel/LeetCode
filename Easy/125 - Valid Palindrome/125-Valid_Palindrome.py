class Solution:

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        cleaned = list(filter(lambda x: x.isalnum(), s))
        print(cleaned)

        for i in range(len(cleaned)):
            if cleaned[i] != cleaned[-i-1]:
                print(cleaned[i], i, cleaned[-i-1])
                return False
            
        return True     
