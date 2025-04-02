from PIL import Image, ImageDraw, ImageFont

# Create a blank image with a soft background color
width, height = 800, 1200
background_color = (240, 248, 255)  # AliceBlue color
img = Image.new("RGB", (width, height), background_color)
draw = ImageDraw.Draw(img)

# Load fonts (ensure the fonts are available on your system)
try:
    header_font = ImageFont.truetype("arialbd.ttf", 36)
    subheader_font = ImageFont.truetype("arialbd.ttf", 32)
    text_font = ImageFont.truetype("arial.ttf", 24)
except IOError:
    # Fallback to default font if custom fonts aren't found
    header_font = ImageFont.load_default()
    subheader_font = ImageFont.load_default()
    text_font = ImageFont.load_default()


# Helper function to center text horizontally
def center_text(text, font, y):
    text_width = draw.textlength(text, font=font)
    x = (width - text_width) // 2
    draw.text((x, y), text, fill="black", font=font)


# Draw header
center_text("Exclusive Church Member Offer!", header_font, 50)
center_text("Koodo Mobile Promo", subheader_font, 130)

# Draw the promotional details
y_offset = 220
lines = [
    "Free SIM Card, No Activation Fee, No Contracts",
    "Member of the church receives a $25 voucher toward bill!",
    "",
    "$29  -  20GB",
    "$34  -  60GB",
    "$45  -  80GB",
    "",
    "Unlimited call & text (Canada/USA, within Canada)",
    "",
    "6-Month Offer: FREE 6-Hour International Calling per Month",
    "3rd Month FREE!",
]

for line in lines:
    center_text(line, text_font, y_offset)
    y_offset += 50

# Draw footer call-to-action
y_offset += 30
center_text("Visit us today & start saving!", subheader_font, y_offset)

# Save the flyer as a PNG file
img.save("koodo_church_promo_flyer.png")
print("Flyer generated and saved as koodo_church_promo_flyer.png")
