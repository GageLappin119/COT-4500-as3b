# COT-4500-as3b

Contains implementations of numerical algorithms related to linear systems.
Also includes test cases for verification and solution output.

Directory Structure

  src/main/: Contains the main implementation code.
  
  src/test/: Contains test cases for the algorithms.

How to Use

Install Dependencies

  Ensure you have Python installed (3.6 or higher).
  
  Install required dependencies by running the following command inside the root folder:
  
  pip3 install -r requirements.txt
  
  (Use pip instead of pip3 if the command does not work.)

Running Tests

  To execute the test cases, navigate to the test folder and run:
  
  python3 test_assignments_2.py
  
  (Default values are provided in the test cases.)

Implemented Algorithms

1. Gaussian Elimination

  Solves a system of linear equations using the Gaussian elimination method.
  
  Test Case: Solves Ax = B for a given coefficient matrix A and constant vector B.
    
2. LU Factorization

  Decomposes a square matrix A into a lower triangular matrix L and an upper triangular matrix U.
  
  Test Case: Computes LU decomposition and determinant for a given matrix.

3. Diagonal Dominance Check

  Determines whether a given square matrix is diagonally dominant.
  
  Test Case: Checks a sample matrix and returns True or False.

4. Positive Definiteness Check

  Verifies if a matrix is symmetric and positive definite using the Cholesky decomposition method.
  
  Test Case: Tests a given matrix for positive definiteness.

