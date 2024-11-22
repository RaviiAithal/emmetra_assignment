import cv2
import numpy as np

# Path to the raw Bayer image file
file_path = '12.raw'  # Replace with your actual file path

# Step 1: Load the Bayer image (16-bit unsigned, GRBG pattern) with 1920x1280 resolution
bayer_image = np.fromfile(file_path, dtype=np.uint16).reshape((1280, 1920))

# Step 2: Right-shift to account for the 12-bit effective bit depth in a 16-bit container
bayer_image = bayer_image >> 4  # Shift to scale to 12-bit range (0-4095)

# Step 3: Normalize the image data to 8-bit range for display (0-255)
# This ensures the image is bright enough to be viewed properly
bayer_image_normalized = cv2.normalize(bayer_image, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
# Step 3: Separate the Bayer pattern into individual channels
red = np.zeros_like(bayer_image)
green = np.zeros_like(bayer_image)
blue = np.zeros_like(bayer_image)

# Red at (1,1), (1,3), ...
red[1::2, 1::2] = bayer_image[1::2, 1::2]

# Green at (0,1), (1,0), ...
green[0::2, 1::2] = bayer_image[0::2, 1::2]
green[1::2, 0::2] = bayer_image[1::2, 0::2]

# Blue at (0,0), (0,2), ...
blue[0::2, 0::2] = bayer_image[0::2, 0::2]

# Step 4: Edge-aware interpolation for missing pixels
kernel = np.array([[-1, -1, 0, 1, 1],
                   [-1, 0, 1, 1, 1],
                   [0, 1, 1, 1, 0],
                   [1, 1, 1, 0, -1],
                   [1, 1, 0, -1, -1]], dtype=np.float32)

# Interpolate Red channel
interpolated_red = cv2.filter2D(red.astype(np.float32), -1, kernel)
interpolated_red = np.clip(interpolated_red, 0, 4095)

# Interpolate Green channel
interpolated_green = cv2.filter2D(green.astype(np.float32), -1, kernel)
interpolated_green = np.clip(interpolated_green, 0, 4095)

# Interpolate Blue channel
interpolated_blue = cv2.filter2D(blue.astype(np.float32), -1, kernel)
interpolated_blue = np.clip(interpolated_blue, 0, 4095)

# Step 5: Combine interpolated channels into a single image
bgr_image = np.zeros((bayer_image.shape[0], bayer_image.shape[1], 3), dtype=np.uint16)
bgr_image[:, :, 0] = interpolated_blue
bgr_image[:, :, 1] = interpolated_green
bgr_image[:, :, 2] = interpolated_red

# Normalize to 8-bit for saving
demosaiced_image = (bgr_image / 16).astype(np.uint8)

# Step 5: Custom white balancing by scaling each channel
def gray_world(image):
    """
    White balance image using Gray-world algorithm
    Parameters
    ----------
    image : numpy array
            Image to white balance
    
    Returns
    -------
    image_wb : numpy array   
               White-balanced image
    """
    # Compute the mean of each channel (B, G, R)
    b, g, r = cv2.split(image)
    b_mean, g_mean, r_mean = np.mean(b), np.mean(g), np.mean(r)

    # Calculate the overall mean of the image
    k = (b_mean + g_mean + r_mean) / 3

    # Calculate the gain factors for each channel
    b_gain = k / b_mean
    g_gain = k / g_mean
    r_gain = k / r_mean

    # Apply gains to each channel
    b = cv2.multiply(b, b_gain)
    g = cv2.multiply(g, g_gain)
    r = cv2.multiply(r, r_gain)

    # Merge the channels back into a single image
    image_wb = cv2.merge((b, g, r))

    return image_wb

# Step 6: Apply the gray_world function to the demosaiced image
white_balanced_image = gray_world(demosaiced_image)

# Step 7: Denoise the white-balanced image using Gaussian filter (5x5)
# Apply Gaussian blur with a 5x5 kernel size
denoised_image = cv2.GaussianBlur(white_balanced_image, (5, 5), 0)

# Step 7: Apply Gamma correction using sRGB gamma approximation with adjustable parameters

def apply_srgb_gamma(image, gamma=2.2, threshold=0.0031308):
    # Scale the image to the range [0, 1] for gamma correction
    image = image / 255.0
    # Apply sRGB gamma correction with an adjustable gamma parameter
    gamma_corrected = np.where(image <= threshold, 
                               12.92 * image, 
                               1.055 * (image ** (1 / gamma)) - 0.055)
    # Scale back to 8-bit range [0, 255]
    gamma_corrected = np.clip(gamma_corrected * 255, 0, 255).astype(np.uint8)
    return gamma_corrected

# Apply gamma correction with a custom gamma value
gamma_corrected_image = apply_srgb_gamma(denoised_image, gamma=2.2)  # Adjust gamma to 1.8 for less brightness

# Step 8: Apply Unsharp Mask filter
def unsharp_mask(image, blur_radius=5, strength=1.5):
    # Step 1: Blur the image (Gaussian Blur)
    blurred_image = cv2.GaussianBlur(image, (blur_radius, blur_radius), 0)
    
    # Step 2: Subtract the blurred image from the original
    sharpened_image = cv2.addWeighted(image, 1 + strength, blurred_image, -strength, 0)
    
    return sharpened_image

# Apply Unsharp Masking to the gamma-corrected image
sharpened_image = unsharp_mask(gamma_corrected_image, blur_radius=5, strength=3.8)

# Step 9: Convert to RGB for correct color format before saving
sharpened_image_rgb = cv2.cvtColor(sharpened_image, cv2.COLOR_BGR2RGB)

# Optional: Save the final output as an image file
output_path = 'testing\\test.png'
cv2.imwrite(output_path, sharpened_image_rgb)
print(f"Sharpened unsharp-masked image saved to {output_path}")
