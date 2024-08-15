import os
from PIL import Image


def compress_image(input_path: str, output_path: str, quality: int = 85) -> bool:
    """
    Compresses an image, preserves EXIF data, and saves it to the specified output path.

    Parameters:
    - input_path (str): Path to the original image.
    - output_path (str): Path to save the compressed image.
    - quality (int): Compression quality (1-100). Higher is better quality and larger size.

    Returns:
    - bool: True if compression was successful, False otherwise.
    """
    try:
        # Open the image
        img = Image.open(input_path)

        # Preserve EXIF data
        exif_data = img.info.get('exif')

        # Compress and save the image with EXIF data
        img.save(output_path, "JPEG", quality=quality, exif=exif_data)

        print(f"Image compressed and saved to {output_path}.")
        return True
    except Exception as e:
        print(f"Failed to compress image: {e}")
        return False


def compress_images_in_folder(src_folder: str, dest_folder: str, quality: int = 85) -> None:
    """
    Compresses all images in the source folder and saves them to the destination folder.
    Deletes original images if compression is successful.

    Parameters:
    - src_folder (str): The folder containing the original images.
    - dest_folder (str): The folder to save the compressed images.
    - quality (int): Compression quality (1-100). Higher is better quality and larger size.
    """
    # Ensure destination folder exists
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
        print(f"Created destination folder: {dest_folder}")

    # Iterate over all files in the source folder
    for filename in os.listdir(src_folder):
        input_path = os.path.join(src_folder, filename)
        output_path = os.path.join(dest_folder, filename)

        # Only process files that are images (based on their extension)
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
            print(f"Processing {filename}...")
            success = compress_image(input_path, output_path, quality)

            if success:
                # Delete the original image if compression was successful
                os.remove(input_path)
                print(f"Deleted original file: {input_path}")
            else:
                print(f"Compression failed for {input_path}, leaving the file as is.")
        else:
            print(f"Skipping non-image file: {filename}")
