import cv2 as cv
import numpy as np
import tkinter as tk
from tkinter import filedialog, Label, Frame, Canvas, Scrollbar
from tkinter import ttk
from PIL import Image, ImageTk

# Global variables
file_paths = ["", "", ""]
output_image = None
thumbnails = [None, None, None]


def load_image(index):
    """Open file dialog to select an image and update the corresponding path."""
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
    if file_path:
        file_paths[index] = file_path
        labels[index].config(text=file_path.split('/')[-1])
        # Load and display a thumbnail
        img = Image.open(file_path)
        img.thumbnail((250, 180))
        thumbnails[index] = ImageTk.PhotoImage(img)
        thumbnail_labels[index].config(image=thumbnails[index])
        thumbnail_labels[index].image = thumbnails[index]


def process_hdr():
    """Process the HDR image using the Mertens fusion algorithm."""
    global output_image
    img_list = [cv.imread(file) for file in file_paths if file]

    if len(img_list) != 3 or any(img is None for img in img_list):
        print("Please provide three valid images.")
        return

    try:
        # Merge using Mertens fusion
        merge_mertens = cv.createMergeMertens()
        hdr_mertens = merge_mertens.process(img_list)
        output_image = np.clip(hdr_mertens * 255, 0, 255).astype('uint8')
        display_output(output_image)
    except Exception as e:
        print(f"Error processing HDR image: {e}")


def display_output(img):
    """Display the processed image on a scrollable canvas."""
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb)

    # Resize the image to fit the available display space while preserving aspect ratio
    max_width, max_height = canvas.winfo_width(), canvas.winfo_height()
    img_width, img_height = img_pil.size
    if img_width > max_width or img_height > max_height:
        img_pil.thumbnail((max_width, max_height))

    img_tk = ImageTk.PhotoImage(img_pil)
    output_label.config(image=img_tk)
    output_label.image = img_tk

    # Adjust scroll region for the canvas to allow scrolling
    canvas.config(scrollregion=canvas.bbox("all"))


def on_resize(event):
    """Handle window resizing and adjust image size to stay centered."""
    if output_image is not None:  # Ensure the processed image exists
        display_output(output_image)


# Initialize Tkinter window
root = tk.Tk()
root.title("HDR Image Processor - Mertens Fusion")
root.geometry("1024x768")
root.config(bg="#f5f5f5")

# Styles
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 14, "bold"), padding=15, background="#007ACC", foreground="white")
style.map("TButton", background=[("active", "#005F8A")])
style.configure("TLabel", font=("Helvetica", 12), background="#f5f5f5")

# Header
header = Label(root, text="HDR Image Processor (Mertens Fusion)", font=("Helvetica", 28, "bold"), bg="#f5f5f5", fg="#007ACC")
header.grid(row=0, column=0, columnspan=5, pady=20)

# Frame for loading images
load_frame = Frame(root, bg="#f5f5f5")
load_frame.grid(row=1, column=0, columnspan=5, pady=10)

labels = []
thumbnail_labels = []

for i, label_text in enumerate(["Low Exposure", "Mid Exposure", "High Exposure"]):
    inner_frame = Frame(load_frame, bg="#f5f5f5")
    inner_frame.grid(row=0, column=i * 2, padx=20, sticky="nsew")

    lbl = ttk.Label(inner_frame, text=f"Select {label_text}", background="#f5f5f5")
    lbl.pack(pady=5)
    labels.append(lbl)

    btn = ttk.Button(inner_frame, text="Browse", command=lambda idx=i: load_image(idx))
    btn.pack(pady=10, ipadx=20)

    thumbnail_label = Label(inner_frame, bg="#f5f5f5")
    thumbnail_label.pack(pady=10)
    thumbnail_labels.append(thumbnail_label)

    if i < 2:
        plus_label = Label(load_frame, text="+", font=("Helvetica", 24, "bold"), bg="#f5f5f5", fg="#007ACC")
        plus_label.grid(row=0, column=(i * 2) + 1)

# Button to process HDR
process_button = ttk.Button(root, text="Process HDR", command=process_hdr)
process_button.grid(row=2, column=0, columnspan=5, pady=30, ipadx=30)

# Scrollable canvas for displaying output
output_canvas_frame = Frame(root, bg="#f5f5f5")
output_canvas_frame.grid(row=3, column=0, columnspan=5, sticky="nsew")

canvas = Canvas(output_canvas_frame, bg="#f5f5f5")
scrollbar = Scrollbar(output_canvas_frame, orient="vertical", command=canvas.yview)
canvas.config(yscrollcommand=scrollbar.set)

output_label = Label(canvas, bg="#f5f5f5")
canvas.create_window((500, 300), window=output_label, anchor='center')

canvas.grid(row=0, column=0, sticky='nsew')
scrollbar.grid(row=0, column=1, sticky='ns')

output_canvas_frame.columnconfigure(0, weight=1)
output_canvas_frame.rowconfigure(0, weight=1)

root.columnconfigure(0, weight=1)
root.rowconfigure(3, weight=10)

# Bind resizing event to adjust image display
root.bind("<Configure>", on_resize)

# Run the Tkinter main loop
root.mainloop()
