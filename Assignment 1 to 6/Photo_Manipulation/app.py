from PIL import Image, ImageFilter, ImageEnhance

def load_image(image_path):
    try:
        img = Image.open(image_path)
        img.show()
        return img
    except Exception as e:
        print(f"Error: {e}")
        return None
    
def grayscale(img):
    return img.convert("L")

def blur(img, radius=2):
    return img.filter(ImageFilter.GaussianBlur(radius))

def sharpen(img):
    return img.filter(ImageFilter.SHARPEN)

def adjust_brightness(img, factor=1.5):
    enhancer = ImageEnhance.Brightness(img)
    return enhancer.enhance(factor)

def adjust_contrast(img, factor=1.5):
    enhancer = ImageEnhance.Contrast(img)
    return enhancer.enhance(factor)

def resize(img, width, height):
    return img.resize((width, height))

def crop(img, left, top, right, bottom):
    return img.crop((left, top, right, bottom))

def rotate(img, angle):
    return img.rotate(angle)

def flip(img):
    return img.transpose(Image.FLIP_LEFT_RIGHT)

def mirror(img):
    return img.transpose(Image.FLIP_TOP_BOTTOM)

def save_image(img, save_path):
    img.save(save_path)
    print(f"Image saved as {save_path}")

def show_image(img):
    img.show()

def main():
    image_path = "C:/Users/Dell/Pictures/mobile photos/2025_01_26_15_50_35_2754.png"
    image = load_image(image_path)
    
    if image:
        gray_img = grayscale(image)
        blurred_img = blur(image, radius=3)
        bright_img = adjust_brightness(image, factor=1.5)
        resized_img = resize(image, 400, 300)
        rotated_img = rotate(image, 45)
        flipped_img = flip(image)
        mirrored_img = mirror(image)

        save_image(resized_img, "modified_image.jpg")
        show_image(resized_img)
        show_image(gray_img)
        show_image(blurred_img)
        show_image(bright_img)
        show_image(rotated_img)
        show_image(flipped_img)  
        show_image(mirrored_img)    

if __name__ == "__main__":
    main()
