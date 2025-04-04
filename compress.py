from PIL import Image
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def compress_image(input_path, output_path, target_kb=600):
    img = Image.open(input_path)

    # Convert to RGB if image has transparency
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    quality = 95  # Start high
    while True:
        img.save(output_path, 'JPEG', quality=quality)
        size_kb = os.path.getsize(output_path) / 1024
        if size_kb <= target_kb or quality <= 10:
            break
        quality -= 5

    print(f"✅ Compressed to {round(size_kb, 2)} KB as {output_path}")

class ImageHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and event.src_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            print(f"New image detected: {event.src_path}")
            filename = os.path.basename(event.src_path)
            name, ext = os.path.splitext(filename)
            output_path = os.path.join('compressed_images', f"{name}.jpg")
            compress_image(event.src_path, output_path)

def main():
    # Create necessary folders if they don't exist
    os.makedirs('images', exist_ok=True)
    os.makedirs('compressed_images', exist_ok=True)

    # Set up the file system observer
    event_handler = ImageHandler()
    observer = Observer()
    observer.schedule(event_handler, path='images', recursive=False)
    observer.start()

    print("🔄 Watching 'images' folder for new images...")
    print("📁 Place images in the 'images' folder to automatically compress them")
    print("📁 Compressed images will be saved in the 'compressed_images' folder")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n👋 Stopping image watcher...")
    observer.join()

if __name__ == "__main__":
    main()
