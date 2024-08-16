# -----------------------------------------------------------
# Anagram Script
#
# (C) 2024 Ivan Gustavo Ortiz García
# GH Repository https://github.com/0zymandias-Courses/interview_challenges
# -----------------------------------------------------------

#Constants 
name="It is an Anagram?"; 

def itIsAnAnagram(word1="", word2=""):
    """
        function itIsAnAnagram checks if 2 words are an Anagram
        
        @params word1 -> String 
        @params word2 -> String 
        @returns -> Dict 
    """
    try:
        # Dictionary which stores the counting results
        results = {}
        # sort procesing to ensure the comparation
        word1Sorted = ''.join(sorted(word1));
        word2Sorted = ''.join(sorted(word2));
        #Verify if those are equals with a simply string comparation
        if(word1Sorted==word2Sorted):
            #then, iterate on to get the counting result
            for char in word1Sorted:
                results[char] = 1 if (char is not results) else results[char] + 1
            return({"status":True,"results":results});
        #else, just return false
        else:
            return({"status":False,"results": results});
    except Exception as e: 
        print(f"Error at wordsComparation: {e}");

def main():
    try:
        print(f"Running the script: {name}");
        dictResponse = itIsAnAnagram("elbow","below");
        print(f"the words are an Anagram: {dictResponse['status']}");
        print(dictResponse["results"])
        
    except Exception as e: 
        print(f"Error at Main: {e}");

if __name__ == "__main__":
    main()
