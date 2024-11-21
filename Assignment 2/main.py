import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

# Step 1: Load the Bayer raw image
file_path = 'task2image.raw'  # Replace with actual file path
bayer_image = np.fromfile(file_path, dtype=np.uint16).reshape((1280, 1920))
bayer_image = bayer_image >> 4  # Scale to 12-bit range (0-4095)

# Step 2: Normalize to 8-bit range for processing
bayer_image_normalized = cv2.normalize(bayer_image, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

# Step 3: Demosaicing
rgb_image = cv2.cvtColor(bayer_image_normalized, cv2.COLOR_BAYER_GR2BGR)

# Step 4: White balance
b, g, r = cv2.split(rgb_image)
b_mean, g_mean, r_mean = np.mean(b), np.mean(g), np.mean(r)
k = (b_mean + g_mean + r_mean) / 3
b_gain, g_gain, r_gain = k / b_mean, k / g_mean, k / r_mean
b = cv2.multiply(b, b_gain)
g = cv2.multiply(g, g_gain)
r = cv2.multiply(r, r_gain)
white_balanced_image = cv2.merge((b, g, r))

# Step 5: Implement denoising filters
denoised_median = cv2.medianBlur(white_balanced_image, 5)
denoised_bilateral = cv2.bilateralFilter(white_balanced_image, 9, 75, 75)
denoised_gaussian = cv2.GaussianBlur(white_balanced_image, (5, 5), 0)

# Step 6: Compute SNR for black-bordered regions
regions = [
    bayer_image_normalized[240:260, 950:970],  # Region 1
    bayer_image_normalized[550:570, 850:870],  # Region 2
    bayer_image_normalized[1050:1070, 950:970]  # Region 3
]

def compute_snr(region):
    signal = np.mean(region)
    noise = np.std(region)
    return 20 * np.log10(signal / noise) if noise != 0 else float('inf')

snr_values = {"Median": [], "Bilateral": [], "Gaussian": []}

for region in regions:
    snr_values["Median"].append(compute_snr(cv2.medianBlur(region, 5)))
    snr_values["Bilateral"].append(compute_snr(cv2.bilateralFilter(region, 9, 75, 75)))
    snr_values["Gaussian"].append(compute_snr(cv2.GaussianBlur(region, (5, 5), 0)))

# Step 7: Apply gamma correction and Laplacian sharpening
def apply_gamma_correction(image, gamma=1.2):
    inv_gamma = 1.0 / gamma
    table = np.array([(i / 255.0) ** inv_gamma * 255 for i in range(256)]).astype("uint8")
    return cv2.LUT(image, table)

gamma_corrected_images = {
    "Median": apply_gamma_correction(denoised_median),
    "Bilateral": apply_gamma_correction(denoised_bilateral),
    "Gaussian": apply_gamma_correction(denoised_gaussian)
}

laplacian_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=np.float32)
sharpened_images = {
    method: cv2.filter2D(img, -1, laplacian_kernel)
    for method, img in gamma_corrected_images.items()
}

# Compute edge strength as a single normalized scalar
def compute_edge_strength(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grad_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    edge_strength = np.sqrt(grad_x**2 + grad_y**2)
    return np.mean(edge_strength)

edge_strength_values = {
    method: compute_edge_strength(img)
    for method, img in sharpened_images.items()
}

# Save and display results
cv2.imwrite('denoised_median.png', denoised_median)
cv2.imwrite('denoised_bilateral.png', denoised_bilateral)
cv2.imwrite('denoised_gaussian.png', denoised_gaussian)

for method, img in sharpened_images.items():
    cv2.imwrite(f'sharpened_{method.lower()}.png', img)

print("SNR values for different methods:")
for method, values in snr_values.items():
    print(f"{method}: {values}")

print("\nEdge strength values for sharpened images:")
for method, value in edge_strength_values.items():
    print(f"{method}: {value}")
