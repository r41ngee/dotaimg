# В ФОТО РАСПОЛОЖИТЬ 34 * 41 = 1394 СКИЛЛА
import selector
import hue
import placer
from PIL import Image


def grid_div(mul: int) -> tuple[int, int]:
    """
    Функция подбирает целочисленные размеры сетки (rows, cols) для заданного количества элементов mul,
    при этом разница между количеством строк и столбцов минимальна.
    Возвращает кортеж (rows, cols).
    """
    best_pair = (1, mul)
    min_diff = abs(mul - 1)
    for i in range(1, int(mul ** 0.5) + 1):
        if mul % i == 0:
            j = mul // i
            if abs(i - j) < min_diff:
                best_pair = (i, j)
                min_diff = abs(i - j)
    return best_pair

def main():
    rows, cols = 14, 88
    pic_size = 128

    pics = selector.recursive_search('dota_images')

    pics_len = len(set(pics))
    if pics_len != rows * cols:
        print("Incorrect grid size!")
        print("trying to guess the best grid size ...")
        rows, cols = grid_div(pics_len)


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