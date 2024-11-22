import cv2
import numpy as np

# Load the denoised image
input_image_path = "denoised_output.jpg"  # Replace with your image path
denoised_image = cv2.imread(input_image_path)

# Step 1: Compute SNR for specified regions
regions = [
    denoised_image[240:260, 950:970],  # Region 1
    denoised_image[550:570, 850:870],  # Region 2
    denoised_image [700:720, 1000:1020]  # Region 3
]

def compute_snr(region):
    signal = np.mean(region)
    noise = np.std(region)
    return 20 * np.log10(signal / noise) if noise != 0 else float('inf')

snr_values = [compute_snr(region) for region in regions]

print("SNR values for the specified regions:")
for i, snr in enumerate(snr_values, 1):
    print(f"Region {i}: {snr:.2f} dB")

# Step 2: Apply gamma correction
def apply_gamma_correction(image, gamma=1.2):
    inv_gamma = 1.0 / gamma
    table = np.array([(i / 255.0) ** inv_gamma * 255 for i in range(256)]).astype("uint8")
    return cv2.LUT(image, table)

gamma_corrected_image = apply_gamma_correction(denoised_image)

# Step 3: Apply Laplacian sharpening
laplacian_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=np.float32)
sharpened_image = cv2.filter2D(gamma_corrected_image, -1, laplacian_kernel)

# Step 4: Compute edge strength
def compute_edge_strength(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grad_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    edge_strength = np.sqrt(grad_x**2 + grad_y**2)
    return np.mean(edge_strength)

edge_strength_value = compute_edge_strength(sharpened_image)
print(f"\nEdge strength after Laplacian sharpening: {edge_strength_value:.2f}")

# Save results
cv2.imwrite("gamma_corrected_image.jpg", gamma_corrected_image)
cv2.imwrite("sharpened_image.jpg", sharpened_image)
