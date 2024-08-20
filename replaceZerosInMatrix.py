# -----------------------------------------------------------
# Fill Matrix MxN with Zeros Script
#
# (C) 2024 Ivan Gustavo Ortiz García
# GH Repository https://github.com/0zymandias-Courses/interview_challenges
# -----------------------------------------------------------

#Constants 
name = "replace Zero values in a Matrix"; 
coordenates = {
    "col":[],
    "row":[]
}
matrix = [
    [1,2,3,4],
    [0,5,6,10],
    [7,8,0,9],
    [7,2,1,9],
    [7,7,2,0]
];

def searchZerosInMatrix(matrix = [[]]):  
    """
      function searchZerosInMatrix lookUp for all Zeros values in a Matrix N x M
      Args:
        matrix :Array[Array[Integer]]:
      Returns:
        None
    """
    try:
        for indexRow in range(0,len(matrix)):
            for indexColumn in range(0,len(matrix[indexRow])):
                if(matrix[indexRow][indexColumn]==0):
                    coordenates["row"].append(indexRow)
                    coordenates["col"].append(indexColumn)
    except Exception as e: 
        print(f"Error at searchZerosInMatrix: {e}");
        
def replaceWithZerosMatrix(matrix = [[]]):
    """
      function replaceWithZerosMatrix Replace Zero values in all Columns and Rows 
      where zeros values were found in a Matrix N x M 
      Args:
        matrix :Array[Array[Integer]]:
      Returns:
        None
    """
    try:
        for indexRow in range(0,len(matrix)):
            if indexRow in coordenates['row']:
                matrix[indexRow] = [0] * len(matrix[indexRow]);
            else:
                for indexColumn in range(0,len(matrix[indexRow])):
                    if indexColumn in coordenates['col']:
                        matrix[indexRow][indexColumn] = 0;
        printMatrix(matrix, "Final Matrix ....")
    except Exception as e: 
        print(f"Error at replaceWithZerosMatrix: {e}");
        
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
        searchZerosInMatrix(matrix);
        replaceWithZerosMatrix(matrix);
    except Exception as e: 
        print(f"Error at Main: {e}");

if __name__ == "__main__":
    main();
