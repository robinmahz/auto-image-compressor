# Image Compression Tool

This tool automatically compresses images when they are added to the `images` folder. It's perfect for quickly reducing image file sizes while maintaining good quality.

## Features

- 🖼️ Automatically detects new images in the `images` folder
- 📦 Compresses images to a target size (default: 600KB)
- 🔄 Converts images to JPG format
- 🚀 Easy access through desktop shortcuts
- ⚡ Supports PNG, JPG, JPEG, GIF, and BMP formats

## Setup Instructions

1. **Install Required Packages**

   ```bash
   pip install -r requirements.txt
   ```

2. **Start the Script**

   ```bash
   # Activate the virtual environment
   source venv/bin/activate

   # Run the compression tool
   python compress.py
   ```

## How to Use

1. **Adding Images**

   - Place your images in the `images` folder
   - You can use the desktop shortcut for easy access
   - Supported formats: PNG, JPG, JPEG, GIF, BMP

2. **Getting Compressed Images**

   - Compressed images will automatically appear in the `compressed_images` folder
   - Use the desktop shortcut to quickly access compressed images
   - All compressed images are saved as JPG format

3. **Stopping the Script**
   - Press `Ctrl + C` in the terminal
   - Or close the terminal window

## Folder Structure

- `images/` - Place your original images here
- `compressed_images/` - Find your compressed images here
- Desktop shortcuts are available for both folders

## Notes

- The script will continue running until you stop it
- Each new image will be automatically compressed
- Original images remain unchanged
- Compressed images are saved with the same name but in JPG format

## Requirements

- Python 3.x
- Pillow
- watchdog

All required packages are listed in `requirements.txt`
