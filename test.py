import numpy as np
def test_cholesky_verfahren(a):
    if a == np.transpose(a):
        return True
    else:
        return False