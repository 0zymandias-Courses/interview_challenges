# -----------------------------------------------------------
# String Rotation Script
#
# (C) 2024 Ivan Gustavo Ortiz García
# GH Repository https://github.com/0zymandias-Courses/interview_challenges
# -----------------------------------------------------------

#Constants 
name = "String Rotation"; 
word = "waterbottle";
wordRotated = "erbottlewat";

def isARotatedString(word = "", wordRotated = "", wordIndex = 0, previousWordIndex=0):  
    """
      function isARotatedString works recursively 'till ensure found the world on the rotated world.
      Args:
      Returns:
        None
    """
    try:
        indexFromWordRotated = findSubString(word[:wordIndex],wordRotated);
        if(indexFromWordRotated >- 1):
            isARotatedString(word, wordRotated, wordIndex + 1, indexFromWordRotated)
        else:
            exRotatedWord = wordRotated[indexFromWordRotated-2:] + wordRotated[:indexFromWordRotated-2]
            if(exRotatedWord == word):
                print(f"Original Word {word}");
                print(f"Ex Rotated Word {exRotatedWord}");
                print(f"Is {wordRotated} a Rotated Word of {word} ? True");
            else:
                print(f"Is {wordRotated} a Rotated Word of {word} ? False");
    except Exception as e: 
        print(f"Error at isARotatedString: {e}");

def findSubString(subString2lookUp = "", wordRotated = ""):
    try:
        print(f"Evaluating {subString2lookUp} on {wordRotated}")
        return wordRotated.find(subString2lookUp)
    except Exception as e :
        print(f"Error at findSubString: {e}");

def main():
    try:
        print(f"Running the script: {name}");
        isARotatedString(word, wordRotated, 1, 1);
    except Exception as e: 
        print(f"Error at Main: {e}");

if __name__ == "__main__":
    main();
