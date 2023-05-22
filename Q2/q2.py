def cosS(doci,query):
    return np.dot(doci,query)/(np.linalg.norm(doci)*np.linalg.norm(query))
    

if __name__ == '__main__':
    import numpy as np
    Docs = np.array([[1,1,0,1,0,1],
            [1,1,1,0,1,0],
            [1,1,0,1,0,0]])

    Query = [1,1,0,0,1,0]

    doc1 = cosS(Docs[0],Query)

    doc2 = cosS(Docs[1],Query)

    doc3 = cosS(Docs[2],Query)

    print("doc1 = {0:.2f}".format(doc1),'\n')

    print("doc2 = {0:.2f}".format(doc2),'\n')

    print("doc3 = {0:.2f}".format(doc3),'\n')
