# -----------------------------------------------------------
# Rotate Matrix NxN Script
#
# (C) 2024 Ivan Gustavo Ortiz García
# GH Repository https://github.com/0zymandias-Courses/interview_challenges
# -----------------------------------------------------------

#Constants 
name = "Rotate a Matrix"; 
length = 3;
clockwiseFlag = False;
degrees = 360
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
];

def rotateMatrix(length = 0, matrix = [[]], degrees = 90, clockwiseFlag = True):  
    """
      function rotate Matrix works recursively 'till degrees got 0, decreasing 90 degrees per attempt
      Args:
        length :Integer:
        matrix :Array[Array[Integer]]:
        degrees :Integer:
        clockwiseFlag :Boolean:
      Returns:
        None
    """
    try:
        arrowCharDicrection = "Clockwise" if  clockwiseFlag else "Anticlockwise";
        newMatrix= rotateMatrix90Degrees(length, matrix, clockwiseFlag);
        printMatrix(newMatrix, f"Rotating the Matrix 90 degrees {arrowCharDicrection}");
        degrees -= 90
        if (degrees>0):
            rotateMatrix(length, newMatrix, degrees, clockwiseFlag)
    except Exception as e: 
        print(f"Error at rotateMatrix: {e}");

def rotateMatrix90Degrees(length = 0, matrix = [[]], clockwiseFlag = True):
    """
    function rotate Matrix 90 Degrees, it rotates clockwise or anticlockwise
      Args:
        length :Integer:
        matrix :Array[Array[Integer]]:
        clockwiseFlag :Boolean:
      Returns:
        matrix :Array[Array[Integer]]:
    """
    try:
        matrixRotated = [[0] * length for i in range(length)];
        for i in range(0, length):
            for j in range(0, length):
                if clockwiseFlag:
                    matrixRotated[j][length-1-i] = matrix[i][j];
                else:
                    matrixRotated[length-1-j][i] = matrix[i][j];
        return matrixRotated;
    except Exception as e: 
        print(f"Error at rotateMatrix90Degrees: {e}");
    
    
def printMatrix(matrix = [[]], message = ""):
    try:
        print(message)
        for subArray in matrix:
            print(str(subArray)+'\n');
    except Exception as e: 
        print(f"Error at printMatrix: {e}");
        
def main():
    try:
        print(f"Running the script: {name}");
        printMatrix(matrix, "Initial Matrix ....");
        rotateMatrix(length, matrix, degrees, clockwiseFlag);
    except Exception as e: 
        print(f"Error at Main: {e}");

if __name__ == "__main__":
    main();
