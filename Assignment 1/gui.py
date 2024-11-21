import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np
import threading


class ImageProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Signal Processing Pipeline -  Emmetra")
        self.root.geometry("1200x800")
        self.root.configure(bg="#2E2E2E")

        # Initialize variables
        self.original_image = None
        self.processed_image = None
        self.current_stage = "Demosaic"  # Default to demosaic after loading
        self.demosaic_button = None  # We'll reference this button for highlighting

        # Top buttons for processing stages
        self.buttons_frame = tk.Frame(root, bg="#2E2E2E")
        self.buttons_frame.pack(side=tk.TOP, pady=10)

        self.buttons = {
            "Original": self.display_original,
            "Demosaic": self.demosaic_image,
            "White Balance": self.white_balance,
            "Denoise": self.denoise_image,
            "Gamma Correct": self.gamma_correct,
            "Sharpen": self.sharpen_image,
        }

        for stage, command in self.buttons.items():
            btn = tk.Button(
                self.buttons_frame,
                text=stage,
                command=lambda cmd=command, stage=stage: self.process_and_display(cmd, stage),
                bg="#4CAF50",
                fg="white",
                font=("Arial", 12, "bold"),
                activebackground="#45a049",
                width=15,
                relief="ridge",
            )
            btn.pack(side=tk.LEFT, padx=5)

            # Save reference to the Demosaic button
            if stage == "Demosaic":
                self.demosaic_button = btn

        # Image display area
        self.image_panel = tk.Label(
            root, text="Load an image to begin.", bg="#2E2E2E", fg="white", font=("Arial", 14)
        )
        self.image_panel.pack(expand=True)

        # Bottom control buttons
        self.controls_frame = tk.Frame(root, bg="#2E2E2E")
        self.controls_frame.pack(side=tk.BOTTOM, pady=10)

        load_btn = tk.Button(
            self.controls_frame,
            text="Load Image",
            command=self.load_image,
            bg="#3b5998",
            fg="white",
            font=("Arial", 12, "bold"),
            activebackground="#3b5998",
            width=15,
        )
        load_btn.pack(side=tk.LEFT, padx=5)

        save_btn = tk.Button(
            self.controls_frame,
            text="Save Image",
            command=self.save_image,
            bg="#ff5722",
            fg="white",
            font=("Arial", 12, "bold"),
            activebackground="#ff5722",
            width=15,
        )
        save_btn.pack(side=tk.LEFT, padx=5)

    def load_image(self):
        file_path = filedialog.askopenfilename(
            title="Select a Raw Image", filetypes=[("Raw Files", "*.raw")]
        )
        if not file_path:
            return

        # Loading animation
        self.image_panel.config(text="Loading...", image="")
        self.root.update()

        # Load and process the Bayer image
        try:
            bayer_image = np.fromfile(file_path, dtype=np.uint16).reshape((1280, 1920))
            bayer_image = (bayer_image >> 4)  # Shift to 12-bit
            bayer_image = cv2.normalize(
                bayer_image, None, 0, 255, cv2.NORM_MINMAX
            ).astype(np.uint8)

            # Demosaic the Bayer image to RGB
            self.original_image = cv2.cvtColor(bayer_image, cv2.COLOR_BAYER_GR2BGR)
            self.processed_image = self.original_image.copy()

            # Always demosaic immediately after loading the image
            self.process_and_display(self.demosaic_image, "Demosaic")
            self.image_panel.config(text="Original Image Loaded")
        except Exception as e:
            print("")

    def save_image(self):
        if self.processed_image is None:
            messagebox.showwarning("Warning", "No image to save.")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".png", filetypes=[("PNG Files", "*.png")]
        )
        if file_path:
            try:
                cv2.imwrite(file_path, cv2.cvtColor(self.processed_image, cv2.COLOR_RGB2BGR))
                messagebox.showinfo("Success", f"Image saved to {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save image: {e}")

    def process_and_display(self, process_function, stage_name):
        if self.original_image is None:
            messagebox.showwarning("Warning", "No image loaded.")
            return

        # Display loading animation
        self.image_panel.config(text="Processing...", image="")
        self.root.update()

        # Process image in a thread to avoid blocking GUI
        def process():
            try:
                self.processed_image = process_function()
                self.display_image(self.processed_image)
                self.image_panel.config(text=f"{stage_name} Image")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to process image: {e}")

        threading.Thread(target=process).start()

        # Highlight the active button
        #self.highlight_active_button(stage_name)

    def display_image(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
        image = Image.fromarray(image)
        image = image.resize((960, 640), Image.LANCZOS)
        image = ImageTk.PhotoImage(image)

        self.image_panel.config(image=image, text="")
        self.image_panel.image = image

    def display_original(self):
        self.current_stage = "Original"
        return self.original_image

    def demosaic_image(self):
        self.current_stage = "Demosaic"
        return self.original_image

    def white_balance(self):
        self.current_stage = "White Balance"
        return self.apply_gray_world(self.processed_image)

    def denoise_image(self):
        self.current_stage = "Denoise"
        return cv2.GaussianBlur(self.processed_image, (5, 5), 0)

    def gamma_correct(self):
        self.current_stage = "Gamma Correct"
        return self.apply_srgb_gamma(self.processed_image, gamma=1.1)

    def sharpen_image(self):
        self.current_stage = "Sharpen"
        return self.apply_unsharp_mask(self.processed_image, blur_radius=5, strength=3.8)

    # def highlight_active_button(self, stage_name):
    #     # Reset all buttons to default color
    #     for btn in self.buttons.values():
    #         btn.config(bg="#4CAF50")

        # Highlight the active stage's button
        if stage_name == "Demosaic":
            self.demosaic_button.config(bg="#45a049")  # Darker green for active stage

    @staticmethod
    def apply_gray_world(image):
        b, g, r = cv2.split(image)
        b_gain, g_gain, r_gain = (np.mean(g) / np.mean(c) for c in (b, g, r))
        return cv2.merge((cv2.multiply(b, b_gain), g, cv2.multiply(r, r_gain)))

    @staticmethod
    def apply_srgb_gamma(image, gamma=2.2):
        image = image / 255.0
        corrected = np.where(image <= 0.0031308, 12.92 * image, 1.055 * (image ** (1 / gamma)) - 0.055)
        return (corrected * 255).clip(0, 255).astype(np.uint8)

    @staticmethod
    def apply_unsharp_mask(image, blur_radius, strength):
        blurred = cv2.GaussianBlur(image, (blur_radius, blur_radius), 0)
        return cv2.addWeighted(image, 1 + strength, blurred, -strength, 0)


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessorApp(root)
    root.mainloop()