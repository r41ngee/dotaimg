import os
from collections import defaultdict

def _skill_pic(files):
    """
    Функция принимает список файлов и возвращает только те,
    которые имеют одинаковый префикс (до первого символа '_').
    Например, из ['radius.png', 'necrolyte_skull.png', 'necrolyte_ghost.png', 'speed.png']
    вернёт ['necrolyte_skull.png', 'necrolyte_ghost.png']
    """

    prefix_dict = defaultdict(list)
    for file in files:
        if '_' in file:
            prefix = file.split('_', 1)[0]
            prefix_dict[prefix].append(file)
    # Оставляем только те группы, где файлов больше одного
    result = []
    for group in prefix_dict.values():
        if len(group) > 1:
            result.extend(group)
    return result

def recursive_search(path):
    result = []

    for root, dirs, files in os.walk(path):
        for file in _skill_pic(files):
            result.append(os.path.join(root, file))

        for dir in dirs:
            temp_result = recursive_search(os.path.join(root, dir))
            result.extend(temp_result)

    return result

if __name__ == '__main__':
    result = recursive_search('dota_images')
    print(len(set(result)))
