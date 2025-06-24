import tkinter
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

watermark_text = 'Anonymous'
font_path = 'arial.ttf'  # Path to desired font file (e.g., Arial)
font_size = 13
font = ImageFont.truetype(font_path, font_size)


def upload_image():
    file_path = filedialog.askopenfilename(
        filetypes=[
            ('PNG files', '*.png'),
            ('JPEG files', '*.jpg'),
            ('JPEG files', '*.jpeg'),
            ('GIF files', '*.gif'),
            ('BMP files', '*.bmp'),
            ('All files', '*.*')
        ]  # it allow image with the following extension.
    )
    if file_path:
        try:
            # Open image using Pillow
            img = Image.open(file_path)

            # Resize the image
            img.thumbnail((400, 400))

            # Draw watermark
            watermarked_image = img.copy()
            draw = ImageDraw.Draw(watermarked_image)

            # watermark position (optional - calculate to place the watermarked in the middle)
            # text_width, text_height = draw.textbbox((0, 0), watermark_text, font=font)[2:]
            # image_width, image_height = watermarked_image.size
            # x = (image_width - text_width) // 2
            # y = (image_width - text_width) // 2

            # draw watermark
            draw.text((225, 150), watermark_text, font=font, fill=(255, 255, 255, 100))  # Black text with 50% opacity

            # if want to save the image
            # watermarked_image.save("watermarked_output.png")

            # Convert image to Tkinter PhotoImage
            tk_img = ImageTk.PhotoImage(watermarked_image)

            # Upload a Label to display the image
            image_label.config(image=tk_img)
            image_label.image = tk_img
        except Exception as e:
            print(f'Error loading image: {e}')


window = tkinter.Tk()

window.title("Watermark App")
window.minsize(width=500, height=500)

# Create the button to trigger upload
upload_button = tkinter.Button(window, text='Upload Image', command=upload_image)
upload_button.pack(pady=10)

# Create the label to display the uploaded image
image_label = tkinter.Label(window)
image_label.pack()

window.mainloop()

