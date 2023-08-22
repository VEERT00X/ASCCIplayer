import os 
import sys
import cv2
from PIL import Image

# Configuration

ASCII = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", ".", "!", "^", "&", "~", "-", "_"]

# Functions

def resized_gray_image(image, new_width=70):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width)
    resized_gray_image = image.resize((new_width, new_height)).convert('L')
    return resized_gray_image

def pixelate(image, new_width=70):
    new_image_data = resized_gray_image(image, new_width).getdata()
    characters = [ASCII[pixel // 25] for pixel in new_image_data]
    return ''.join(characters)

def generate(image, new_width=70):
    ascii_image = pixelate(image, new_width)
    total_pixels = len(ascii_image)
    rows = [ascii_image[index:(index + new_width)] for index in range(0, total_pixels, new_width)]
    return '\n'.join(rows)

def main():
    # Handle command-line arguments
    display_frame = "--no-frame" not in sys.argv
    file_path = sys.argv[1] if len(sys.argv) > 1 else input("Enter file path: ")
    cap = cv2.VideoCapture(file_path)
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            break
        
        frame_image = Image.fromarray(frame)
        ascii_output = generate(frame_image)
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        if display_frame:
            cv2.imshow("Original Frame", frame)
            
        print(ascii_output)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
