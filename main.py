from PIL import Image, ImageDraw, ImageFont

def generate_meme(image_path, top_text, bottom_text, output_path):
    try:
        # Load the image
        image = Image.open(image_path)
        
        # Get image dimensions
        width, height = image.size
        
        # Load a font
        font_size = int(height / 10)
        font = ImageFont.truetype("arial.ttf", font_size)
        
        # Create a drawing object
        draw = ImageDraw.Draw(image)
        
        # Calculate text size and position
        text_width, text_height = draw.textsize(top_text, font=font)
        x = (width - text_width) / 2
        y = 10
        
        # Draw top text
        draw.text((x, y), top_text, font=font, fill="white")
        
        # Calculate text size and position for bottom text
        text_width, text_height = draw.textsize(bottom_text, font=font)
        x = (width - text_width) / 2
        y = height - text_height - 10
        
        # Draw bottom text
        draw.text((x, y), bottom_text, font=font, fill="white")
        
        # Save the meme
        image.save(output_path)
        print("Meme generated successfully!")
    
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    image_path = "meme.jpeg"
    top_text = "Finally"
    bottom_text = "a Worthy Opponent"
    output_path = "output_meme.jpg"
    
    generate_meme(image_path, top_text, bottom_text, output_path)
