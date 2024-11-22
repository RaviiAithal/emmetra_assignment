

---

# **Assignment 2: Denoise and Sharpness Techniques**

This project implements various denoising and edge enhancement techniques to process a 12-bit Bayer RAW image and assess image quality using metrics like **Signal-to-Noise Ratio (SNR)** and **Edge Strength**.

---

## **Objective**

- Implement and compare different techniques for **denoising** and **sharpness enhancement**.
- Assess **image quality metrics** for each approach.

---

## **Tasks**

### **1. Denoising**
- **Traditional Methods**:
  - Median filter
  - Bilateral filter
  - Compare with Gaussian filter from Assignment 1
- **SNR Computation**:
  - Compute the spatial Signal-to-Noise Ratio (SNR) for **three gray tones** as specified by [Imatest Imaging Noise Guide](https://www.imatest.com/imaging/noise/).

### **2. Edge Enhancement**
- Implement **Laplacian filter-based enhancement**.
- Compare the results with other sharpness enhancement methods.
- Compute **Edge Strength** using gradient-based approaches for all implemented methods.

### **3. Processing Pipeline**
- Use the ISP pipeline from Assignment 1 for **Bayer RAW image processing**.
- Input: 12-bit Bayer RAW image.
- Output: RGB image with 24 bits per pixel (8 bits per channel).

### **4. Reporting**
- Generate a report comparing **SNR**, **Edge Strength**, and visual quality metrics for all methods.

---

## **Input Requirements**

- **Image Format**:
  - Bayer RAW format (`.raw`) with 12-bit pixel depth.
  - Resolution: **1920x1280**.
  - Bayer Pattern: **GRBG**.
- **Configuration**:
  - Ensure the appropriate tools are configured for viewing RAW and processed images.

---

## **Tools**

- **Image Viewers**:
  - **PixelViewer**
  - **Irfanview** (with RAW plugin)

---

## **Implementation Steps**

1. **Load Bayer RAW Image**:
   - Input a 12-bit Bayer RAW image file.
   - Convert the Bayer pattern to an RGB image using **demosaicing**.

2. **Denoising**:
   - Apply traditional filters: Median, Bilateral, and Gaussian.

3. **Edge Enhancement**:
   - Apply Laplacian filter-based sharpening.
   - Measure edge strength using gradient-based Sobel operators.

4. **Quality Metrics**:
   - Compute **SNR** for three different gray-tone regions in the image.
   - Compute **Edge Strength** to quantify sharpening performance.

5. **Save Outputs**:
   - Save denoised and sharpened images as PNG files for evaluation.

---

## **Example Output**

### **SNR Values**:
```plaintext
Gaussian: [35.90, 36.50, 34.78]
Median: [37.10, 36.98, 35.42]
Bilateral: [38.45, 37.12, 36.89]
```

### **Edge Strength**:
```plaintext
Gaussian: 50.12
Median: 51.45
Bilateral: 52.18
```

---

## **How to Run**

1. **Set Up Environment**:
   - Install required libraries:
     ```bash
     pip install numpy opencv-python
     ```

2. **Run the Script**:
   - Place the input RAW file (`task2image.raw`) in the project directory.
   - Execute the script:
     ```bash
     python main.py
     ```

3. **View Results**:
   - Processed images will be saved in the current directory:
     - `denoised_median.png`
     - `sharpened_laplacian.png`
   - Console output will display **SNR** and **Edge Strength** values.

---

