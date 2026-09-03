class Solution:
    #Understand: We want to encode a list of strings and return them combined and then decode them to get back to the original
    #Input: a list of strings
    #Output: A list of strings

    #Plan: Get the length of each string and put it at the front of that string and append the string after 
    #Then for decode go through the String if we run into a number add the next number of characters to the Array

    def encode(self, strs: List[str]) -> str:
        new_string = ""

        for word in strs:
            new_string += str(len(word)) + "#" 
            new_string += word
        return new_string 

    def decode(self, s: str) -> List[str]:
        #Go through the string and when we run into a number followed by a hashtag then we know that after that is a string from the original
        ans = []

        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            
            length = int(s[i:j])

            word = s[j + 1: j + length + 1]

            ans.append(word)

            i = j + length + 1
        return ans