from PIL import Image
import pillow_heif #update pillow_heif to the lastest version
import os

# Register HEIF opener
pillow_heif.register_heif_opener()

def heic_to_jpg(heic_file_path, jpg_file_path):
    try:
        image = Image.open(heic_file_path)
        image = image.convert("RGB")  # Convert to RGB format
        image.save(jpg_file_path, "JPEG")
        print(f"Converted {heic_file_path} to {jpg_file_path}")
    except Exception as e:
        print(f"Error converting {heic_file_path}: {e}")

def convert_directory(heic_directory, jpg_directory):
    if not os.path.exists(jpg_directory):
        os.makedirs(jpg_directory)

    for file_name in os.listdir(heic_directory):
        if file_name.lower().endswith('.heic'):
            heic_file_path = os.path.join(heic_directory, file_name)
            jpg_file_name = os.path.splitext(file_name)[0] + '.jpg'
            jpg_file_path = os.path.join(jpg_directory, jpg_file_name)
            heic_to_jpg(heic_file_path, jpg_file_path)

if __name__ == "__main__":
    heic_directory = '/Users/tao/Downloads/heic'  # Replace with the path to your HEIC files directory
    jpg_directory = heic_directory  # Output in the same directory, you can change this if needed
    convert_directory(heic_directory, jpg_directory)
