# Auto Image Compressor

A Python-based tool that automatically compresses images when added to a watched folder. Perfect for content creators, web developers, or anyone who regularly works with images!

## ✨ Features

- 🖼️ **Automatic Detection**: Instantly detects new images in the watched folder
- 📦 **Smart Compression**: Optimizes images to target size while maintaining quality
- 🔄 **Format Conversion**: Automatically converts images to JPG format
- 🚀 **Easy Access**: Creates desktop shortcuts for quick access (Windows, macOS, Linux)
- ⚡ **Multi-format Support**: Works with PNG, JPG, JPEG, GIF, and BMP formats
- 💻 **Cross-platform**: Works on Windows, macOS, and Linux

## 🚀 Quick Start

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

   The script will:

   - Create necessary folders
   - Set up desktop shortcuts
   - Start watching for new images

## 📁 How to Use

1. **Adding Images**

   - Simply drop your images into the `images` folder
   - Use the desktop shortcut for quick access
   - Supported formats: PNG, JPG, JPEG, GIF, BMP

2. **Getting Compressed Images**

   - Compressed images appear automatically in the `compressed_images` folder
   - Access them through the desktop shortcut
   - All compressed images are saved as JPG format

3. **Stopping the Script**
   - Press `Ctrl + C` in the terminal
   - Or close the terminal window

## 🛠️ Technical Details

- **Default Compression**: Targets 600KB file size
- **Quality Adjustment**: Automatically adjusts quality to meet target size
- **Transparency Handling**: Converts transparent images to RGB
- **Shortcut Management**: Automatically creates and updates desktop shortcuts

## 📂 Project Structure

```
auto-image-compressor/
├── images/              # Drop your images here
├── compressed_images/   # Find compressed images here
├── compress.py          # Main script
├── requirements.txt     # Dependencies
└── README.md           # This file
```

## ⚙️ Requirements

- Python 3.x
- Pillow (for image processing)
- watchdog (for folder monitoring)

All required packages are listed in `requirements.txt`

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📝 License

This project is open source and available under the [MIT License](LICENSE).
