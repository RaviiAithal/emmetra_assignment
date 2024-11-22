
# **Assignment 2: Denoise and Sharpness Techniques**

This project implements various denoising and edge enhancement techniques to process a 12-bit Bayer RAW image and assess image quality using metrics like **Signal-to-Noise Ratio (SNR)** and **Edge Strength**.

---

## **Objective**

- Implement and compare different techniques for **denoising** and **sharpness enhancement**.
- Assess **image quality metrics** for each approach.

---

## Implementation Workflow

## Step 1: Load Bayer Raw Image
- Load the `.raw` file using `np.fromfile()`.
- Reshape the data to match the image resolution (e.g., `1280x1920`).
- Scale the image to a 12-bit range (0–4095) using bit-shifting.

---

## Step 2: Normalize to 8-bit Range
- Use `cv2.normalize()` to map the 12-bit values to the 8-bit range (0–255).
- Convert the normalized data to `uint8`.

---

## Step 3: Demosaicing
- Convert the Bayer raw image to an RGB image using `cv2.cvtColor()` with the `cv2.COLOR_BAYER_GR2BGR` flag.

---

## Step 4: White Balancing
- Split the RGB image into Blue, Green, and Red channels.
- Compute the mean intensity of each channel.
- Calculate gains to equalize channel intensities using the formula:
<!DOCTYPE html>
<html>
<head>
</head>
<body>
<p>Calculate gains using:</p>
<p>
  $$k = \frac{b_{\text{mean}} + g_{\text{mean}} + r_{\text{mean}}}{3}$$
</p>
<p>
  $$b_{\text{gain}} = \frac{k}{b_{\text{mean}}}, \quad g_{\text{gain}} = \frac{k}{g_{\text{mean}}}, \quad r_{\text{gain}} = \frac{k}{r_{\text{mean}}}$$
</p>
</body>
</html>
- Scale each channel using the calculated gains.
- Merge the adjusted channels back into an RGB image.

---

## Step 5: Denoising
1. Apply **Median Blur** using `cv2.medianBlur()`.
2. Apply **Bilateral Filter** using `cv2.bilateralFilter()`.
3. Apply **Gaussian Blur** using `cv2.GaussianBlur()`.

---

## Step 6: Signal-to-Noise Ratio (SNR) Computation
- Define regions for noise analysis in the image.
- Compute SNR for each region using the formula:
 <!DOCTYPE html>
<html>
<body>
<p>The SNR is computed using the formula:</p>
<p>
  $$\text{SNR} = 20 \cdot \log_{10}\left(\frac{\text{Signal}}{\text{Noise}}\right)$$
</p>
</body>
</html>
  where:
  - Signal = Mean intensity of the region.
  - Noise = Standard deviation of intensity values.
- Repeat for all denoising methods.

---

<!DOCTYPE html>
<html>
<body>
<h2>Step 7: Gamma Correction and Sharpening</h2>

<h3>Gamma Correction</h3>
<p>Adjust pixel intensity values using a lookup table based on the gamma value. The formula for intensity transformation is:</p>
<p>
  $$I_{\text{out}} = \left( \frac{I_{\text{in}}}{255} \right)^\gamma \cdot 255$$
</p>

<h3>Laplacian Sharpening</h3>
<p>Apply sharpening with a Laplacian kernel. The kernel is defined as:</p>
<p>
  $$\text{Laplacian Kernel} = 
  \begin{bmatrix}
  0 & -1 & 0 \\
  -1 & 5 & -1 \\
  0 & -1 & 0
  \end{bmatrix}$$
</p>
</body>
</html>

---

<!DOCTYPE html>
<html>
<body>
<h2>Step 8: Edge Strength Computation</h2>

<p>To compute edge strength, first convert the image to grayscale. Then calculate Sobel gradients in the x and y directions. The formula for edge strength is:</p>
<p>
  $$\text{Edge Strength} = \sqrt{\text{grad}_x^2 + \text{grad}_y^2}$$
</p>
<p>Normalize the computed edge strength and calculate the mean value to obtain a scalar metric.</p>
</body>
</html>


---
### **FFD_NET**
- We also used `ffd_net` to denoise the images for comparision. The pretrained models are used to denoise. Follow the ffd_net implementation to run the code. Changes are made to `utils.py` and `test_ffdnet_ipol.py` due the change in functions of `scikit-image` and other libraries. To vary the noise change `noise-sigma`. The values are ranged between 0 to 255. which is later mapped between 0 to 1.   
---

## **Input Requirements**

- **Image Format**:
  - Bayer RAW format (`.raw`) with 12-bit pixel depth.
  - Resolution: **1920x1280**.
  - Bayer Pattern: **GRBG**.
- **Configuration**:
  - Ensure the appropriate tools are configured for viewing RAW and processed images.

---

### **Output**
![Denoised and Sharpened output of all three methods](https://github.com/user-attachments/assets/7de1de8a-67eb-4fd8-92e1-b6fefa0898a7)
### SNR Values (in dB)

| Method       | Region 1 (dB) | Region 2 (dB) | Region 3 (dB) |
|--------------|---------------|---------------|---------------|
| Gaussian     | 35.90         | 36.50         | 34.78         |
| Median       | 37.10         | 36.98         | 35.42         |
| Bilateral    | 38.45         | 37.12         | 36.89         |
| FFDNet       | 36.72         | 20.91         | 22.57         |

---

### Edge Strength (Average Magnitude in Pixel Units)

| Method       | Edge Strength (pixels) |
|--------------|-------------------------|
| Gaussian     | 50.12                   |
| Median       | 51.45                   |
| Bilateral    | 52.18                   |
| FFDNet       | 27.07                   |
---
## **Conclusion**
### **Best Denoising Method**
The Bilateral Filter achieved the highest Signal-to-Noise Ratio (SNR) across all evaluations, indicating its superior performance in noise reduction while preserving image details.

### **Best Sharpening Method**
The Bilateral Filter also demonstrated the highest edge strength, making it the most effective in enhancing image edges without over-smoothing.

---
## **How to Run**

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
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
     - `denoised_gaussian.png`
     - `denoised_billateral.png`
     - `sharpened_median.png`
     - `sharpened_gaussian.png`
     - `sharpened_billateral.png`
   - Console output will display **SNR** and **Edge Strength** values.

---


