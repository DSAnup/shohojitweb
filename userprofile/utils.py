# utils.py
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
import os

def resize_and_optimize_image(image, width, height):
    im = Image.open(image)
    im = im.convert('RGB')  # Ensure consistency
    im.thumbnail((width, height))

    output = BytesIO()
    file_extension = os.path.splitext(image.name)[1].lower()

    # Save image with the same format
    if file_extension in ['.jpg', '.jpeg']:
        img_format = 'JPEG'
    elif file_extension == '.png':
        img_format = 'PNG'
    else:
        img_format = 'JPEG'  # Default to JPEG if format is unknown

    im.save(output, format=img_format, quality=85, optimize=True)
    output.seek(0)

    new_image = InMemoryUploadedFile(output, 'ImageField', image.name, image.content_type, sys.getsizeof(output), None)

    return new_image
