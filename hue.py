from PIL import Image

def single_pic(path):
    img = Image.open(path)
    img = img.convert('RGB')
    pixels = img.getdata()
    r_sum = 0
    g_sum = 0
    b_sum = 0
    for pixel in pixels:
        r_sum += pixel[0]
        g_sum += pixel[1]
        b_sum += pixel[2]
    r_avg = r_sum / len(pixels)
    g_avg = g_sum / len(pixels)
    b_avg = b_sum / len(pixels)
    return r_avg, g_avg, b_avg