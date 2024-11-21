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

**Assignment 1: Basic Image Signal Processing (ISP)**  

**Objective**  
- Implement a pipeline to process 12-bit Bayer raw images into visually enhanced 24-bit RGB images.  
- Develop a user-friendly GUI to allow real-time visualization and parameter tuning.  
- Demonstrate the effects of ISP techniques such as demosaicing, white balancing, denoising, gamma correction, and sharpening.  

**Features**  
- A `tkinter`-based GUI enables image loading, processing, and saving with adjustable sliders for parameters like gamma, blur radius, and sharpening strength.  
- The ISP pipeline includes demosaicing (edge-based interpolation, 5x5), white balancing (gray-world algorithm), denoising (Gaussian blur), gamma correction (sRGB mapping), and sharpening (unsharp masking).  
- Users can apply stages individually or in combination, with real-time feedback on the output.  

**Usage**  
- Input: A 12-bit Bayer raw image (GRBG, 1920x1280); Output: A 24-bit RGB image (8 bits per channel).  
- Users can load an image, select specific processing stages, adjust parameters using sliders, and save the processed result.  
- The workflow facilitates easy exploration of how different ISP techniques affect image quality.  

**Combinations to Test**  
- **Demosaic + Gamma Correction**: Evaluate the effects of converting raw data to a visually enhanced RGB image.  
- **Demosaic + White Balance + Gamma Correction**: Assess improvements in color accuracy and overall tonal mapping.  
- **Demosaic + White Balance + Denoise + Gamma Correction + Sharpening**: Observe cumulative effects of all stages on image quality.  

**Observations**  
- Each stage contributes uniquely, such as demosaicing for basic color formation and sharpening for detail enhancement.  
- The GUI simplifies the process, making it easy to experiment with combinations and observe their impact.  
- Documenting results highlights the importance of parameter tuning in optimizing image quality.  

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

---

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


