import unittest
import numpy as np
import volestipy
from volestipy import HPolytope

class TestVolumeMethods(unittest.TestCase):
    def setUp(self):
        dim = 2
        A = np.zeros((2*dim, dim), dtype=np.double)
        A[0:dim] = np.eye(dim)
        A[dim:] -=  np.eye(dim,dim, dtype=np.double)
        b = np.ones(2*dim, dtype=np.double)/2

        self.p = HPolytope(A,b)
        print("*** This is a test for the compute_volume() function of the volestipy library *** \n")
        print("The polytope:")
        print("Dimensions: {}".format(self.p.dimension()))
        print("A matrix:")
        print(self.p.A())
        print("b vector:")
        print(self.p.b())

    # Run tests for the compute_volume() function and its different methods
    def test_seq_of_balls(self):
        volume_SoB = self.p.compute_volume(vol_method = "sequence_of_balls", walk_method = "uniform_ball", walk_len = 5, epsilon = 0.05, seed = volestipy.get_time_seed())
        print("Volume (sequence of balls): {}\n".format(volume_SoB))
        # self.assertAlmostEqual

    def test_gaussian(self):
        volume_GA  = self.p.compute_volume(vol_method = "cooling_gaussian", walk_method = "gaussian_CDHR", walk_len = 5, epsilon = 0.05, seed = 42)
        print("Volume (gaussian annealing): {} \n".format(volume_GA))

    def test_cooling_balls(self):
        test_volume = self.p.compute_volume(vol_method = "cooling_balls", walk_method = "uniform_ball", walk_len = 5, epsilon = 0.05, seed = 42)
        print("Volume (test_volume): {}\n".format(test_volume)) 

# Run tests for the compute_volume() function and its different methods
if __name__ == "__main__":
    print("\n>> Here are the outcomes of the different methods for computing volume <<\n")
    unittest.main()
