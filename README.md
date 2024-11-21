# Emmetra Assignments

This repository contains three assignments completed as part of the task provided by Emmetra. Each assignment includes its source code, outputs, and any relevant documentation.

## Table of Contents

- [Overview](#overview)  
- [Structure](#structure)  
- [Assignment Details](#assignment-details)  


---

## Overview

This repository contains three assignments that is given by **Emmetra**. Each assignment folder includes:

- Source code
- README 
- Output
- Input

The assignments are implemented in **Python**.

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


``` 
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

### Assignment 2: Denoise and Sharpness Techniques

#### **Objective**  
Implement and compare denoising and edge enhancement techniques for Bayer raw images.

#### **Features**

1. **Denoising**:
   - **Median Filter**, **Bilateral Filter**, **Gaussian Filter** for noise reduction.
   - **SSNR Calculation**: Computes signal-to-noise ratio for method comparison.

2. **Edge Enhancement**:
   - **Laplacian Filter** for sharpening edges.
   - **Gamma Correction**: Adjusts image contrast before sharpening.
   - **Edge Strength**: Measures edge clarity after processing.

3. **Comparison**:
   - Denoising methods and edge enhancement techniques evaluated based on SSNR and edge strength.

#### **Usage**

1. **Input**: Bayer raw image (`task2image.raw`).
2. **Run Script**:  
   - Demosaic Bayer image to RGB.
   - Apply denoising filters (Median, Bilateral, Gaussian) and sharpen with Laplacian.
   - Save processed images: `denoised_<method>.png`, `sharpened_<method>.png`.

#### **Requirements**

- **Dependencies**: `opencv-python-headless`, `numpy`.
- **Tools**: Use PixelViewer or IrfanView to view results.
- **Resolution**: Ensure consistent resolution for input images.

#### **Observations**

1. **Denoising**:
   - **Median Filter**: Balanced noise reduction and edge preservation.
   - **Bilateral Filter**: Best for edge retention, moderate noise reduction.
   - **Gaussian Filter**: Smooths effectively but loses detail.

2. **Edge Enhancement**:
   - **Laplacian Filter**: Enhances sharpness.
   - Compared with unsharp masking from Assignment 1 for edge clarity.

3. **Metrics**: SSNR and edge strength quantify denoising and sharpening effectiveness.

### Assignment 3: HDR Imaging

#### Objective  
Implement HDR imaging to merge and tone-map three differently exposed LDR images using the Mertens fusion algorithm.

#### Features  
1. **GUI Tool**: Built with Tkinter for interactive image selection, processing, and saving.  
2. **HDR Processing**: Uses OpenCV’s Mertens fusion to merge low, medium, and high-exposure images.  
3. **Output Management**: Displays processed HDR image on a scrollable canvas and allows saving the result.  

#### Usage  
1. **Input**: Three LDR images (low, medium, high exposure) of the same scene.  
2. **Run Script**: Use the "Browse" buttons to select images, then click "Process HDR" to merge and tone-map.  
3. **Save**: Use the "Save Output" button to store the HDR result.  

#### Requirements  
- **Dependencies**: Install `opencv-python-headless`, `numpy`, and `pillow` via `pip install`.  
- **Images**: Consistent resolution for input LDR images.

#### Observations  
- Mertens fusion creates a balanced HDR image with improved shadow and highlight details.  
- GUI simplifies workflow, making HDR processing intuitive and user-friendly.  


