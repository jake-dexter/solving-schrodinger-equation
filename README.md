# Schrödinger Equation Solver ⚛️  
*Numerical solutions of the time-dependent and time-independent Schrödinger equation using finite difference and Crank–Nicolson methods.*  

## Overview  
This project implements numerical methods to solve the Schrödinger equation in **1D and 3D** for a variety of quantum systems.  
- In **1D**, both **finite difference** and **Crank–Nicolson** methods are used, allowing simulation of wave packet dynamics, tunnelling, and stationary states.  
- In **3D**, the hydrogen atom is modelled via the radial Schrödinger equation in spherical coordinates, recovering correct bound state energies and orbitals.  

The code is split into:  
- `PotentialsNew.py`: definitions of common 1D quantum potentials (infinite/finite wells, harmonic oscillator, Coulomb, double wells, barriers, etc.).  
- `HMatNew.py`: construction of the Hamiltonian matrix and eigensystem solvers.  
- `main.ipynb`: Jupyter notebook demonstrating 1D and 3D simulations.  

This work was carried out as part of a group project on computational quantum mechanics, with an accompanying [project report](docs/Numerically_Solving_the_Schrodinger_Equation.pdf).  

## Features  
- Solve the 1D Schrödinger equation using **finite difference methods**.  
- Simulate 1D time evolution via the **Crank–Nicolson scheme** (stable implicit integration).  
- Built-in support for multiple 1D potentials:  
  - Free particle  
  - Infinite/finite square wells  
  - Potential barriers  
  - Harmonic oscillator  
  - Coulomb potential  
  - Double wells  
- Extendable to **3D hydrogen atom** solutions:  
  - Radial Schrödinger equation solved numerically  
  - Correct bound state energies recovered  
  - Demonstration of quantum orbital structures  
- Visualisation of real part, imaginary part, and probability density of the wavefunction.  
- Demonstrations of tunnelling, bound states, and hydrogen-like orbitals.  

## Example Outputs  

### Free Particle  
![Free Particle](media/Free%20Particle.gif)  

### Potential Barrier (Tunnelling)  
![Potential Barrier](media/Potential%20Barrier.gif)  

### Harmonic Oscillator  
![Harmonic Oscillator](media/Harmonic%20Oscillator.gif)  

## Physics Background  
- **1D systems**: Stationary solutions obtained via finite difference Hamiltonian diagonalisation. Time-dependent propagation uses the **Crank–Nicolson method** to maintain norm conservation.  
- **3D systems**: Radial Schrödinger equation for hydrogen solved numerically, producing quantised bound states consistent with analytic hydrogen spectra.  
- Demonstrates central principles of quantum mechanics:  
  - Wave packet dispersion  
  - Quantum tunnelling  
  - Energy quantisation  
  - Bound vs unbound states  
  - Hydrogen orbital structure  

## Tech Stack  
- **Language:** Python 3.10  
- **Libraries:** NumPy, SciPy, Matplotlib  
- **Environment:** Jupyter Notebook for demonstrations  

## Installation  

Clone the repository and install dependencies:  
```bash
git clone https://github.com/jake-dexter/schrodinger-equation-solver
cd schrodinger-equation-solver
pip install -r requirements.txt
```

Run the Jupyter Notebook:  
```bash
jupyter notebook main.ipynb
```

Note: To export animations, you will also need [FFmpeg](https://ffmpeg.org/download.html) installed and available in your PATH.

## Documentation  
The full report is provided in `/docs/Numerically_Solving_the_Schrodinger_Equation.pdf`, covering methods, theory, and results in detail.  

## Status  
Educational visualisation project (completed as part of a group).  
Future improvements could include 2D solvers, more complex potentials, or GPU acceleration.  

---
