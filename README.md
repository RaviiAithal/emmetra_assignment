# Emmetra Assignments Repository

Welcome to the **Emmetra Assignments Repository**. This repository contains three assignments completed as part of the task provided by Emmetra. Each assignment includes its source code, outputs, and any relevant documentation.

## Table of Contents

- [Overview](#overview)  
- [Structure](#structure)  
- [Assignment Details](#assignment-details)  
- [Setup Instructions](#setup-instructions)  
- [How to Run](#how-to-run)  
- [Outputs](#outputs)  
- [License](#license)  

---

## Overview

This repository contains three assignments that demonstrate various coding and problem-solving skills. Each assignment folder includes:

- Source code for the task  
- Documentation or README specific to the task  
- Outputs (if applicable)  

The assignments are implemented in **Python**, ensuring clean and efficient code.

---

## Structure

The repository is structured as follows:

```plaintext
emmetra-assignments/
│
├── Assignment1/
│   ├── source/             # Source code files for Assignment 1
│   ├── outputs/            # Outputs generated for Assignment 1
│   └── README.md           # Specific details about Assignment 1
│
├── Assignment2/
│   ├── source/             # Source code files for Assignment 2
│   ├── outputs/            # Outputs generated for Assignment 2
│   └── README.md           # Specific details about Assignment 2
│
├── Assignment3/
│   ├── source/             # Source code files for Assignment 3
│   ├── outputs/            # Outputs generated for Assignment 3
│   └── README.md           # Specific details about Assignment 3
│
└── README.md               # Main repository README file

---
## Assignment Details

### **Assignment 1: Basic Image Signal Processing (ISP)**  
This assignment involves implementing essential image signal processing routines for sensor raw images. The tasks include:  
- **Demosaicing:** Edge-based interpolation (5x5) to compute missing channels.  
- **White Balancing:** Using a simple gray-world algorithm to remove color casts.  
- **Denoising:** Applying a Gaussian filter (5x5).  
- **Gamma Correction:** Using sRGB gamma for converting 12-bit input to 8-bit output.  
- **Sharpening:** Applying an unsharp masking filter.  

#### Additional Features:  
- A UI tool to control the parameters of each algorithm block for visualization and comparison.  

#### Input and Output:  
- **Input:** 12-bit Bayer raw image (GRBG, 1920x1280).  
- **Output:** 24-bit RGB image (8 bits per channel).  

#### Combinations to Test:  
Generate outputs with the following combinations and document observations in a report:  
1. Demosaic + Gamma  
2. Demosaic + White Balance + Gamma  
3. Demosaic + White Balance + Denoise + Gamma  
4. Demosaic + White Balance + Denoise + Gamma + Sharpen  

---

### **Assignment 2: Denoise and Sharpness Techniques**  
This assignment explores and compares denoising and sharpness techniques.

#### Denoising Techniques:  
1. Implement Median filter.  
2. Implement Bilateral filter.  
3. Compare both with the Gaussian filter from Assignment 1.  
4. Use an AI-based model (e.g., U-Net, FFDNet) for image denoising.  
5. Compute spatial signal-to-noise ratio (SSNR) for three gray tones to compare the methods.  

#### Edge Enhancement Techniques:  
1. Implement Laplacian filter-based enhancement.  
2. Compare with unsharp masking from Assignment 1.  
3. Compute edge strength using gradient-based approaches.  

#### Input and Output:  
- **Input:** Same Bayer raw image as Assignment 1.  
- **Output:** Processed 24-bit RGB image.

#### Tools:  
Use **PixelViewer** or **IrfanView** (with RAW plugin) for visualizing input and output images.

---

### **Assignment 3: HDR Imaging**  
This assignment focuses on implementing an HDR imaging algorithm using three differently exposed LDR images of a high-contrast scene.

#### Steps to Complete:  
1. Capture three differently exposed LDR images manually (daylight or indoor scenes with bright and shadow regions).  
2. Merge the three images into an HDR image.  
3. Apply tone mapping to create an 8-bit image for display.  

#### Input and Output:  
- **Input:** 3 LDR images captured manually.  
- **Output:** Tone-mapped HDR image.

#### Deliverables:  
A detailed report documenting:  
1. The HDR merging algorithm.  
2. The tone mapping process.  
3. Observations and results.


