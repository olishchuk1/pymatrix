# Pymatrix

## General description:
Learning library for working with matrices and systems of linear equations (SOLE) implemented on Python programing language.

## List of Contents
**Using Pymatrix labrary you can:**
- multiply matrices;
- add matrices;
- multiply matrix by a number;
- find the determinant of a matrix (NxN);
- find the inverted matrix of a matrix (NxN);
- find the determinant of a matrix (NxN) using a Gaussian method;
- find the inverted matrix of a matrix (NxN) using a Gaussian method with a gradual selection of the principal element;
- find the SOLE solution using a Gaussian method;
- find the SOLE solution by the LU-decomposition (L with ones on the main diagonal);
- find the SOLE solution by the LU-decomposition (U with ones on the main diagonal);
- arrangement of symmetric matrices ((U^T)U-decomposition)

## How to download

## How to use

```python
import Pymatrix as px

obj = px([[1, 2], [2, 1])
# finding the determinant of the obj
det_obj = obj.mdeterminant()
```

## Methods
Method | Description
------------ | -------------
obj.mmultiply(other_obj) | Multiplies object matrix on another matrix
obj.madd(other_obj) | Adds the appropriate matrix elements (matrices must be the same size!)
obj.mtranpose() | Tranposes object matrix
obj.triangle_matrix() | Reduces object matrix to a triangular matrix
obj.square_check() | Checks if matrix is a square matrix
obj.mdeterminant() | Finds the determinant of the object matrix
obj.matrix_sort() | Sorts in descending order by rows
