# <u>**Sound-Localization**
## Overview
This project implements a sound-based image reconstruction system using the **Delay-and-Sum (DAS)** algorithm — a method commonly used in **ultrasound imaging** to localize obstacles or reflectors based on received acoustic signals.

The system simulates an **ultrasound transmit–receive setup** with a microphone array, a sound source, and a reflective obstacle. It reconstructs an image of the environment by summing delayed microphone signals to identify the obstacle’s location.

---

## Core Concepts

### Problem Setup
- **Sound Source:** A single source at (0, 0) emitting a circular sound wave.
- **Microphones:** An array of `Nmics` microphones placed vertically along the Y-axis (`x=0`) with spacing `pitch`.
- **Obstacle:** A single point scatterer located at `(x > 0, y)` that reflects the sound wave back to the microphones.

### Signal Model
Each microphone records a **reflected wave** that is a delayed version of the source signal.  
The **delay** depends on the total path length:  
`Source → Obstacle → Microphone`.

A **sinc pulse** represents the emitted sound wave. The narrowness of this pulse (controlled by parameter `SincP`) affects image sharpness.

---

## Procedure

### Step 1: Generate Microphone Signals
- Compute the distance from source → obstacle → each microphone.
- Use this to calculate time delays.
- Generate delayed reflected signals for all microphones.
- Visualize signals as time-series plots and heatmaps.

### Step 2: Implement Delay-and-Sum (DAS) Reconstruction
- Create a grid of possible obstacle locations (X, Y).
- For each grid point, calculate expected delays for all microphones.
- Align (delay) the received mic signals accordingly.
- Sum them to estimate the intensity at each grid point.
- The point of **maximum summed amplitude** corresponds to the obstacle position.

---

## Key Questions / Analysis
- Why does the reconstructed maximum correspond to the true obstacle position?  
- Effect of varying parameters:
  - **Speed of sound (C)** — affects sharpness.
  - **Number of microphones (Nmics)** and **samples (Nsamp)** — affect resolution and accuracy.
- How changing `SincP` modifies the pulse width and image clarity.
- What happens when reconstruction limits or array sizes are varied.

---

## Input Data
- Two `.txt` files containing simulated microphone data (`64 mics × 200 samples`).
- Load data using:
  ```python
  data = np.loadtxt("filename.txt")
  ```

---

## Repository contents
1. **Python Notebook / Script** implementing:
   - Microphone simulation
   - DAS reconstruction
   - Plots for mic outputs and reconstructed images
   - Answers to provided questions
2. **PDF Report** including:
   - Generated figures
   - Parameter analysis
   - Observations and conclusions
---

## Outputs
- Time-domain plots of received mic signals  
- Heatmap of reflections  
- Reconstructed image showing obstacle location  
- Parameter comparison across `Nmics = [8, 32, 64]` and `Nsamp = [50, 100, 200]`
---

## Notes
- The simulation ignores aperture effects and windowing techniques for simplicity.
- The DAS model assumes uniform sound propagation and perfect reflection.
- Only a single reflection obstacle is considered.

---

## Technologies Used
- **Python**
- **NumPy**
- **Matplotlib**
- **Jupyter Notebook** for visualization

---


Developed as part of *Assignment 7 – Sound Localization* for ultrasound imaging reconstruction using the **Delay-and-Sum algorithm**.





