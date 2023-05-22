if __name__ == "__main__":
    import numpy as np
    arr = np.array([[1,2],
                  [3,4]])
    eigvalues, eigvectors = np.linalg.eig(arr)

    determinant = np.linalg.det(arr)

    vec1 = np.array([1,2,3])
    vec2 = np.array([4,5,6])

    cross = np.cross(vec1,vec2)

    A = np.array([[1,2,-2],
                  [2,1,-5],
                  [1,-4,1]])

    b = np.array([-15., -21.,18.])

    x = np.linalg.solve(A,b)

    print("Eigenvalues: {0}".format(eigvalues),'\n')

    print("Eigenvectors: {0}".format(eigvectors), '\n')

    print("Determinant: {0:.0f}".format(determinant), '\n')

    print("Cross product: {0}".format(cross), '\n')

    print("Solution: {0}".format(x), '\n')
