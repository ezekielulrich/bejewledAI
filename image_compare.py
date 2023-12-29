import numpy as np
from numpy.linalg import norm
from PIL import Image

# Load images as arrays using NumPy
image1 = np.array(Image.open(r'C:\GIT_pulls\Bejeweled_ai\bejewledAI\images\boards\board_test.png'))
image2 = np.array(Image.open(r'C:\GIT_pulls\Bejeweled_ai\bejewledAI\images\boards\board_test2.png'))

# Check if the images have the same shape
if image1.shape != image2.shape:
    print(image1.shape, image2.shape)
    raise ValueError("Images must have the same shape")

# Calculate element-wise difference
difference = image1 - image2

# Calculate the norm of the difference
norm_difference = norm(difference)

print(f"The norm of the difference between the two images is: {norm_difference}")
