# -----------------------------------------------------------
# Palindrome Script
#
# (C) 2024 Ivan Gustavo Ortiz García
# GH Repository https://github.com/0zymandias-Courses/interview_challenges
# -----------------------------------------------------------

#Constants 
name="It is a palindrome?"; 
words=["hello", "MOM", "Radar", "Rotator"];

print(f"Running the sctipt: {name}");

def isItAPalindrome(word2Verify=""):
    """
        function isItAPalindrome checks if the word is a palindrome, 
        return true in success/ False in failure
        
        @params word -> String 
        @returns -> Boolean 
    """
    try:
        #Ensure upperCase the word
        word2Verify=word2Verify.upper()
        #locate the index from the very end of the string for initial comparation  
        indexTop2Bottom=len(word2Verify)-1
        for indexBottom2Top in range(0, len(word2Verify)):
            #if the characters are no equal the execution got interrupted 
            if(word2Verify[indexBottom2Top]!=word2Verify[indexTop2Bottom]):
                return False;
            else:
                indexTop2Bottom-=1
        #In case there wasn't any return executed, the word is a palindrome
        return True;
    except Exception as e: 
        print(f"Error at isItAPalindrome: {e}");

def main():
    try:
        print(f"Running the sctipt: {name}");
        for word in words:
            print(f"is {word} a palindrome? {str(isItAPalindrome(word))}");
    except Exception as e: 
        print(f"Error at Main: {e}");

if __name__ == "__main__":
    main()
