import os
import numpy as np
import pandas as pd
from PIL import Image

# Define the number of avatars to generate
num_avatars = 100  # Example: generate 100 avatars

# Directory to save the generated avatars and labels
image_dir = 'dataset/images'
if not os.path.exists(image_dir):
    os.makedirs(image_dir)

data = []

# Function to simulate avatar generation and save as an image
def generate_avatar(height, weight, chest, waist, filename):
    # Placeholder function to generate a dummy image
    # Replace this with actual MakeHuman automation code if available
    image = Image.new('RGB', (128, 128), (255, 255, 255))  # Dummy white image
    image.save(filename)

for i in range(num_avatars):
    # Generate random height, weight, chest, and waist sizes
    height = np.random.randint(150, 200)  # Height in cm
    weight = np.random.randint(50, 100)   # Weight in kg
    chest = np.random.randint(80, 120)    # Chest in cm
    waist = np.random.randint(60, 100)    # Waist in cm
    
    # Generate a unique filename for each avatar
    filename = f'avatar_{i+1}.png'
    filepath = os.path.join(image_dir, filename)
    
    # Generate avatar and save as image
    generate_avatar(height, weight, chest, waist, filepath)
    
    # Append the details to the dataset
    data.append([filename, height, weight, chest, waist])

# Save labels to CSV
labels_path = os.path.join('dataset', 'labels.csv')
df = pd.DataFrame(data, columns=['filename', 'height', 'weight', 'chest', 'waist'])
df.to_csv(labels_path, index=False)

print("Avatars and labels created successfully!")
