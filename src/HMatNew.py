import numpy as np
from scipy.linalg import eigh_tridiagonal

class Hamiltonian:
    def __init__(self, potential, x):
        """
        Initialise the Hamiltonian matrix.
        """
        self.potential = potential
        self.V = potential.GetPotential(x)
        self.EMax = potential.GroundStateEnergy()
        self.x = x

    def solve(self):
        """
        Solve for eigenvalues and eigenvectors.
        """
        deltaX = self.x[1] - self.x[0]
        alpha = 1 / (2 * deltaX**2)

        # Define the upper, lower, and main diagonal array in the matrix
        self.upperDiag = np.full(len(self.x)-1, - alpha)
        self.mainDiag = 2*alpha + self.V
        self.lowerDiag = np.full(len(self.x)-1, -alpha)

        # Solve eigenvalue problem
        eigenvalues, eigenvectors = eigh_tridiagonal(self.mainDiag, self.upperDiag)
        return eigenvalues, eigenvectors

class RadialHamiltonian:
    def __init__(self, potential, r, l=0):
        assert l >= 0, "Orbital Angular Momentum, l, must be greater than or equal to zero."
        self.potential = potential
        self.l = l
        self.r = r
        
        if np.isclose(r[0], 0.0):
            self.r = r[1:]
        else:
            self.r = r

        self.V = potential.GetPotential(r) + l*(l+1)/(2*self.r**2)

    def solve(self):
        deltaR = self.r[1] - self.r[0]
        alpha = 1/(2*(deltaR**2))

        N = len(self.r)
        
        self.upperDiag = np.full(len(self.r)-1, -alpha)
        self.mainDiag = 2*alpha + self.V
        self.lowerDiag = np.full(len(self.r)-1, -alpha)

        # Solve eigenvalue problem
        eigenvalues, eigenvectors = eigh_tridiagonal(self.mainDiag, self.upperDiag)
        return eigenvalues, eigenvectors
    
    
    
    