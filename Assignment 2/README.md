# Image Signal Processing Pipeline - Emmetra

This project demonstrates an **Image Signal Processing (ISP) Pipeline** to process Bayer RAW image files. The pipeline includes various stages, such as **demosaicing**, **white balancing**, **denoising**, **gamma correction**, and **sharpening**, with options to evaluate **Signal-to-Noise Ratio (SNR)** and **edge strength** metrics. 

---

## **Features**

- **Load and View RAW Images**: Handles 12-bit Bayer RAW images and reshapes them into a 2D array for processing.
- **Demosaicing**: Converts Bayer patterns (GRBG) to full-color RGB using OpenCV interpolation.
- **White Balance**: Corrects color casts with a simple gray-world algorithm.
- **Denoising**: Applies various filters such as Median, Bilateral, and Gaussian Blur to reduce noise.
- **Gamma Correction**: Adjusts brightness and contrast using sRGB gamma correction (default gamma = 1.2).
- **Sharpening**: Enhances edge details using Laplacian-based sharpening.
- **Metrics Evaluation**: Computes **SNR** and **edge strength** to assess quality.
- **Save Processed Images**: Saves the processed images in **PNG format**.
- **GUI Control**: Toggle between various ISP stages via intuitive buttons.

---

## **How It Works**

### **Load Image**  
The user loads a **12-bit Bayer RAW image** (e.g., GRBG pattern) using the **Load Image** button.  

### **Process Image**  
The pipeline processes the image through the following stages:  

- **Demosaic**: Converts the Bayer pattern to RGB immediately after loading.  
- **White Balance**: Balances color channels to remove unwanted tints.  
- **Denoise**: Reduces noise using Median, Bilateral, or Gaussian Blur filters.  
- **Gamma Correct**: Enhances brightness and contrast.  
- **Sharpen**: Refines edge details with Laplacian-based sharpening.  

### **Save Image**  
The processed image can be saved in **PNG format** via the **Save Image** button.

---

## **Installation**

### **Prerequisites**
- Ensure you have Python 3.8 or higher installed.

### **Install Dependencies**
Run the following command to install required libraries:
```bash
pip install opencv-python numpy tensorflow
```

---

## **File Format Requirements**

- **Input**: 12-bit Bayer RAW image (e.g., `.raw`) with GRBG configuration and dimensions **1920x1280**.  
- **Output**: RGB image with **8 bits per channel** saved as a **PNG file**.  

---

## **Metrics Evaluation**

- **Signal-to-Noise Ratio (SNR)**:  
  Evaluates denoising performance by measuring the SNR for predefined regions.  

- **Edge Strength**:  
  Assesses sharpening performance by analyzing edge gradients and computing mean gradient magnitude.  

---

## **Usage**

### **1. Clone the Repository**  
Clone the repository or copy the script file into your working directory.  

### **2. Run the Script**  
Execute the GUI script:  
```bash
python main_GUI.py
```

### **3. Process and Save**  
Use the GUI to load, process, and save images.

---

## **Example Console Output**

```plaintext
SNR values for different methods:
Median: [36.45, 35.78, 34.95]
Bilateral: [37.12, 36.45, 35.90]
Gaussian: [35.89, 35.10, 34.56]

Edge strength values for sharpened images:
Median: 52.34
Bilateral: 50.78
Gaussian: 49.56
```

---
