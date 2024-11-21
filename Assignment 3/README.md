---

# HDR Image Processor

A Python-based application for generating High Dynamic Range (HDR) images using the **Mertens Fusion** algorithm. This tool allows users to merge three images with different exposures (low, mid, and high) into a single HDR image. The application features a graphical user interface (GUI) built with Tkinter for ease of use.

---

## Features

- **Mertens Fusion Algorithm**: Create HDR images using exposure fusion.
- **User-Friendly Interface**: Simple GUI for selecting images and processing.
- **Image Previews**: Displays thumbnails of the selected images and the final HDR output.
- **Resizable Output Display**: The processed image adjusts to the window size.

---

## Prerequisites

Ensure you have Python 3.8 or later installed. 

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repository/hdr-image-processor.git
   cd hdr-image-processor
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

---

## Usage

1. Launch the application by running `app.py`.
2. Select three images (low, mid, and high exposure) using the **Browse** buttons.
3. Click the **Process HDR** button to merge the images using the Mertens Fusion algorithm.
4. View the HDR result displayed in the output section.

---

## File Structure

- `app.py`: Main Python script containing the application logic.
- `requirements.txt`: Dependencies required to run the application.
- `README.md`: Documentation for the project.

---

## Dependencies

The application uses the following libraries:

- [OpenCV](https://opencv.org/) for image processing.
- [NumPy](https://numpy.org/) for numerical operations.
- [Pillow](https://python-pillow.org/) for handling image thumbnails.
- [Tkinter](https://wiki.python.org/moin/TkInter) for the graphical interface.

---

## Screenshots

### 1. Main Interface
*Show a screenshot of the application interface here.*

### 2. HDR Output
*Show a screenshot of the HDR result display here.*

---

## Future Enhancements

- Add support for saving the processed HDR image directly.
- Enhance the GUI for a more modern look.
- Support for other HDR algorithms (e.g., Debevec, Robertson).

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For questions or feedback, feel free to reach out:

- **Name**: [Your Name]
- **Email**: [your.email@example.com]
- **GitHub**: [Your GitHub Profile](https://github.com/your-profile)

--- 

Replace placeholder sections with your specific details (e.g., repository URL, screenshots, and contact information).
