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
- Apply and compare denoising and edge enhancement techniques to Bayer raw images.
- Use different filters (Median, Bilateral, and Gaussian) for denoising and assess their performance.
- Evaluate the effectiveness of each technique through SSNR and edge strength metrics.

#### **Features**
- **Denoising**: Implement Median, Bilateral, and Gaussian filters to reduce noise with varying approaches, maintaining image quality.
- **Edge Enhancement**: Apply Laplacian Filter for sharpening edges and use Gamma Correction to adjust image contrast before sharpening.
- **Evaluation**: Use SSNR for comparing denoising methods and edge strength metrics to quantify the sharpness of the processed images.

#### **Usage**
- The script processes Bayer raw images by first demosaicing them to RGB format.
- Denoising techniques are applied, followed by Laplacian sharpening with gamma correction.
- Results are saved as 24-bit RGB images, ready for further analysis or visualization.

  #### **Requirements**
- **Dependencies**: Requires `opencv-python-headless` and `numpy` libraries for image processing tasks.
- **Visualization Tools**: Use PixelViewer or IrfanView for viewing raw images and processed outputs.
- **Image Consistency**: Ensure input images have a consistent resolution for accurate processing across different techniques.

#### **Observations**
- **Denoising Results**: Median Filter balances noise reduction and edge preservation, while Bilateral Filter offers the best edge retention with moderate noise reduction. Gaussian Filter, though efficient, can blur finer details.
- **Edge Enhancement**: The Laplacian Filter sharpens edges effectively, and when combined with gamma correction, it enhances contrast before sharpening. Edge strength measurements help quantify how much detail is preserved in the sharpened images.

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


