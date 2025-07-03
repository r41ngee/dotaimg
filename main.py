# В ФОТО РАСПОЛОЖИТЬ 34 * 41 = 1394 СКИЛЛА
import selector
import hue
import placer
from PIL import Image

def main():
    rows, cols = 41, 17
    pic_size = 128

    pics = selector.recursive_search('dota_images')
    print(len(pics))
    pics_dict = {pic: hue.single_pic(pic) for pic in pics}
    matrix = placer.place_in_coords(pics_dict, (cols, rows))
    print(len(matrix))
    print(len(matrix[0]))
    
    big_image = Image.new("RGB", (cols * pic_size, rows * pic_size))
    for row in range(rows):
        for col in range(cols):
            with Image.open(matrix[row][col]) as img:
                # Вставляем маленькое изображение в нужную позицию
                big_image.paste(img, (col * pic_size, row * pic_size))

    big_image.save('mosaic.png')
    big_image.show()

if __name__ == '__main__':
    main()