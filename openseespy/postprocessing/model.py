import openseespy.opensees as ops
import matplotlib.pyplot as plt


def drawModel():
    plt.figure()

    etags = ops.getEleTags()
    if etags is None:
        return
    if isinstance(etags, int):
        etags = [etags]

    for e in etags:
        elenodes = ops.eleNodes(e)
        for i in range(0, len(elenodes)):

            [xi, yi] = ops.nodeCoord(elenodes[i-1])
            [xj, yj] = ops.nodeCoord(elenodes[i])
            plt.plot([xi, xj], [yi, yj], 'k')

    plt.show()
