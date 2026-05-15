# PINN vs FEM Example

This example compares a classical Finite Element Method (FEM) structural dynamics solution using OpenSeesPy against a Physics-Informed Neural Network (PINN) approximation implemented in PyTorch.

## Features

- **SDOF dynamic system**: Modeling a single-degree-of-freedom oscillator.
- **Harmonic excitation**: Application of sinusoidal force to observe frequency response.
- **FEM transient response**: Numerical integration using the OpenSeesPy framework.
- **PINN approximation**: Neural network training constrained by the governing differential equations.
- **Response comparison plots**: Visual validation of the neural network's accuracy against the FEM baseline.

## Requirements

The following libraries are required to run the comparison:

- `openseespy`
- `torch` (PyTorch)
- `numpy`
- `matplotlib`

## Project Structure

- `main.py`: Primary script to run both simulations and generate plots.
- `models/`: Contains the PINN architecture and training logic.
- `fem/`: OpenSeesPy model definitions and solver settings.
