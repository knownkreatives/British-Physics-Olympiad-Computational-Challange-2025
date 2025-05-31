from Utilities.Transformations import *

import matplotlib.pyplot as plt
import numpy as np
import requests
from tkinter import Tk, filedialog
from PIL import Image

class GeometricImage:
    def __init__(self, image: Image):
        self.image = image
        self.rot = create_2d_rotation_matrix(0)
        self.pos = create_2d_translation_matrix(0, 0)
        self.scale = create_2d_scaling_matrix(image.width, image.height)

    def plot(self, ax: plt.Axes):
        # Resize image
        resizedImage = self.image.resize(self.scale)
        # Convert to array
        img_array = np.array(resizedImage)
        # Get image center
        center = (img_array.shape[1] / 2, img_array.shape[0] / 2)
        # Create rotation matrix
        angle_deg = np.degrees(np.arccos(self.rot[0, 0]))  # Assuming rotation matrix is 2x2
        # Rotate image using PIL
        rotated_img = Image.fromarray(img_array).rotate(angle_deg, resample=Image.BICUBIC, expand=True, center=center)
        # Show image
        ax.imshow(rotated_img, extent=(self.pos[0], self.pos[0] + rotated_img.width, self.pos[1], self.pos[1] + rotated_img.height))

def upload_local_image(filePath: str = None) -> Image.Image:
    """
    Opens a file dialog to upload an image and optionally displays it.
    
    Parameters:
        filePath (str): Optional path to an image file. If not provided, a file dialog will open.

    Returns:
        PIL.Image.Image: The loaded image object.
    """
    # Hide the root Tk window
    root = Tk()
    root.withdraw()

    # File dialog for image selection
    if not filePath:
        filePath = filedialog.askopenfilename(
            title="Select an image",
            filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
        )

    if not filePath:
        print("No file selected.")
        return None
    else:
        print(f"Selected file: {filePath}")
        img = Image.open(filePath)
        return img

def upload_image_from_url(url: str) -> Image.Image:
    """
    Downloads an image from a given URL and returns it as a PIL Image.
    
    Parameters:
        url (str): The URL of the image to download.
        
    Returns:
        PIL.Image.Image: The downloaded image object.
    """
    try:
        img = Image.open(requests.get(url, stream=True).raw)
        print(f"Image downloaded from {url}")
        return img
    
    except Exception as e:
        print(f"Error downloading image: {e}")
        return None

def convert_image_to_array(image: Image.Image) -> np.ndarray:
    """
    Converts a PIL image to a NumPy array.
    
    Parameters:
        image (PIL.Image.Image): The image to convert.
        
    Returns:
        np.ndarray: The converted image as a NumPy array.
    """
    return np.array(image)
