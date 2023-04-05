import math
######################################################
##############       -TASK I -      ##################
######################################################

# TODO: Complete the function magnitude 
# use a for loop
def magnitude(vector):
    """ This function computes the magnitude of a vector
    
    Args:
        vector (list): The input vector
    
    Returns:
        float: The magnitude of the input vector
    """
    ...

# TODO: Complete the function dot
# use iteration using list indexes
def dot(a,b):
    """ This function computes the dot product 
    of 2 vectors of same length
    
    Args:
        a (list): The input vector 1
        b (list): The input vector 2
    
    Returns:
        float: the dot product between vectors
    """
    ...

# TODO: Complete the cosine distance fct
# use acos from the module "math"
def cos_distance(a,b):
    """ This function computes the angle between 2 vectors
    of aritrary dimension from 2 vectors of same length
    
    Args:
        a (list): The input vector 1
        b (list): The input vector 2
    
    Returns:
        float: the angle (cosine distance) btw the vectors
    """
    ...


######################################################
##############      -TASK II -      ##################
######################################################

# TODO: Complete the matrix_average fct
# use range index to access matrix elements
def matrix_average(matrix, n, m):
    """ This function computes the average of the input
    matrix of size nxm
    
    Args:
        matrix (list): The input 2D matrix
        n (int): number of row of matrix
        m (int): number of column of matrix
    
    Returns:
        float: the average value of the matrix
    """
    ...


# TODO: Complete the normalize_matrix fct
# use the average previously computed
# and pass it as an argument of your fct
# Copy matrix into a new "averaged_matrix"
# or initialize a new nxm matrix filled with zeros
def normalize_matrix(matrix, n, m, average):
    """ This function average a matrix using its
    size and average value
    
    Args:
        matrix (list): The input 2D matrix
        n (int): number of row of matrix
        m (int): number of column of matrix
        average (float): average of the matrix
    
    Returns:
        list: the averaged matrix
    """
    ...


######################################################
###############      - MAIN -      ###################
######################################################
def main():

    # Task 1: Cosine distance
    vector_1 = [10, 5, 5]
    vector_2 = [-2, 4, 8]
    angle = math.degrees(cos_distance(vector_1, vector_2))
    print("the angle between the two vectors is " + str(angle))

    # Task 2: Matrix averaging
    matrix = [[ 10, 3, 5 ], 
            [  2, 4, 1 ], 
            [  3, 2, 0 ]]
    n = len(matrix)
    m = len(matrix[0])
    average = matrix_average(matrix, n, m)
    print("the normalized matrix is: ", normalize_matrix(matrix, n, m, average))

main()

