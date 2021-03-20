"""
Adjacency list:

    - Initialize a dict: keys = all nodes
    - Iterate on all edges:
        - Get their start/fin nodes (ignore 'blobs')
        - dict(start).append(fin)
        - dict(fin).append(start)

Adjacency matrix
    - Outcome should be a list of lists: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    - Iterate on all nodes:
        - Initialize shell of matrix with 0's or None's for values.
        -



"""
