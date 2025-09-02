import numpy as np

class Potential:
    """
    Base class for different quantum systems.
    Provides common physical constants and storage for parameters
    like mass, width, centre, and xmin that subclasses can utilise.
    """
    
    # Physical Constants
    h = 6.62607015e-34       # Planck's constant, J*s
    hbar = h / (2.0 * np.pi) 
    e = 1.602176634e-19      # Elementary charge, C
    eps0 = 8.8541878128e-12  # Vacuum permittivity, F/m
    
    def __init__(self, mass=None, width=None, center=None, xmin=None):
        """
        Parameters
        ----------
        -mass 
            
        -width 
            
        -center 
            
        xmin 
        """
        self.mass = mass
        self.width = width
        self.center = center
        self.xmin = xmin

    def GetPotential(self, x):
        """Calculate the potential V(x). Must be implemented by subclasses."""
        

    def GroundStateEnergy(self):
        """Return the ground state energy. Must be implemented by subclasses."""
        

class PotentialBarrier(Potential):
    def __init__(self, mass, width, xmin=0, v0=15):
        super().__init__(mass=mass,width=width,center=0,xmin=xmin)
        self.v0 = v0

    def GetPotential(self, x):
        xmax = self.xmin + self.width
        return np.where((x >= self.xmin) & (x <= xmax), self.v0, 0)

    def GroundStateEnergy(self):
        return self.h**2 / (8 * self.mass * self.width**2)
    
    
    
class HarmonicOscillator(Potential):
    def __init__(self, mass, width, omega, center):
        """
        1D Harmonic Oscillator.
        
        Parameters
        ---------
        -mass 
            
        -width 
            
       -omega 
            
        -center 
            
        """
        super().__init__(mass=mass, width=width, center=center, xmin=None)
        self.omega = omega
    
    def GetPotential(self, x):
        # Use self.center from the base class
        return 0.5 * self.mass * self.omega**2 * (x - self.center)**2
    
    def GroundStateEnergy(self):
        return 0.5 * self.hbar * self.omega


class FreeParticle(Potential):
    def __init__(self, mass, momentum):
        """
        Free Particle (Zero Potential).
        
        Parameters
        ----------
        -mass 
        
        -momentum 
            
        """
       
        super().__init__(mass=mass, width=None, center=None, xmin=None)
        self.momentum = momentum
    
    def GetPotential(self, x):
        return np.zeros_like(x)
    
    def GroundStateEnergy(self):
        return (self.momentum**2) / (2.0 * self.mass)


class InfinitePotentialWell(Potential):
    def __init__(self, mass, width, xmin=0):
        """
        1D Infinite Potential Well.
        
        Parameters
        ----------
        -mass 
            
        -width 
            
        -xmin 
          
        """
        super().__init__(mass=mass, width=width, center=None, xmin=xmin)
    
    def GetPotential(self, x):
       
        xmax = self.xmin + self.width
        return np.where((x < self.xmin) | (x > xmax), 1e5, 0)
    
        #Large finite value (1e5) used to approximate infinite potential, 
        #for numerical stability
    
    def GroundStateEnergy(self):
        return (self.h**2) / (8.0 * self.mass * self.width**2)


class FinitePotentialWell(Potential):
    def __init__(self, mass, width, xmin=0, v0=1e-18):
        """
        1D Finite Potential Well.
        
        Parameters
        ----------
        -mass 
            
        -width 
           
        -xmin 
            
        -v0 
           
        """
        super().__init__(mass=mass, width=width, center=None, xmin=xmin)
        self.v0 = v0
    
    def GetPotential(self, x):
        
        xmax = self.xmin + self.width
        return np.where((x < self.xmin) | (x > xmax), self.v0, 0)
    
    def GroundStateEnergy(self):
        return (self.h**2) / (8.0 * self.mass * self.width**2)


class CoulombPotential(Potential):
    def __init__(self):
        """
        1/r Coulomb Potential 
        
        No need for mass, width, center, xmin in a pure Coulomb potential.
        """
        super().__init__(mass=None, width=None, center=None, xmin=None)
    
    def GetPotential(self, r):
       
        return -1/r
    
    def GroundStateEnergy(self):
       
        return -13.6 * self.e


class DoublePotentialWell(Potential):
    def __init__(self, mass, width, xmin1, xmin2, v0):
        """
        Double Potential Well with two separate wells.
        
        Parameters
        ----------
        -mass 
            
        -width 
           
        -xmin1 
            
        -xmin2 

        -v0 
        """
       
        super().__init__(mass=mass, width=width, center=None, xmin=xmin1)
        self.xmin2 = xmin2
        self.v0 = v0
    
    def GetPotential(self, x):
       
        xmax1 = self.xmin  + self.width
        xmax2 = self.xmin2 + self.width
        
        return np.where(
            ((x >= self.xmin)  & (x <= xmax1)) |
            ((x >= self.xmin2) & (x <= xmax2)),
            0,   # Inside either well
            self.v0  # Outside
        )
    
    def GroundStateEnergy(self):
        
        return (self.h**2) / (8.0 * self.mass * (2.0 * self.width)**2)

class DoubleSmoothPotential(Potential):
    def __init__(self,mass):
        super().__init__(mass=mass,width=None,center=None,xmin=None)  
        
    def GetPotential(self, x):
        E_0 = 5.1
        C = 0.085
        D = 15
        return E_0 * (C * x**4 - x**2) + D
   


#Changes made are as follows:

#-Potentials are now subclasses of the class Potential to allow for inheritance and overall code hygiene. This allows for common properties present in each class (system) to be shared from the base class.
#Example: mass was defined separately everytime, causing duplicates. More properties can be inherited this way for example xmins and widths but this can be implemented later

#rather than calling x as a paremeter in the class, its now called in GetPotential() to avoid calling and storing unneccessary data in each class

#constants defined in the Potential base class allowing for easy access when defining the functions of each potential.

# Cold changes - Jake

#More parameters are now inherited from the base class, BEWARE OF THESE CHANGES
