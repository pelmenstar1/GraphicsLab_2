from PIL import Image, ImageDraw

def parse_data_line(text: str) -> tuple[int, int]:
    space_idx = text.index(' ')
    
    x = int(text[:space_idx])
    y = int(text[(space_idx + 1):])

    return (x, y)

img = Image.new("RGB", (960, 540))
img_draw = ImageDraw.ImageDraw(img)

with open("DS4.txt", mode='r') as data_file:
    while True:
        line = data_file.readline()
        if line == "":
            break

        point = parse_data_line(line)
        img_draw.point(point, fill=(255, 255, 255)) 

img.save("result.jpeg", "jpeg")

