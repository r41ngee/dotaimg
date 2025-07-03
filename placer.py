def place_in_coords(
        pics: dict[str, tuple[float, float, float]],
        grid: tuple[int, int]
    ):

    pics = _sort_by_hue(pics)
    # pics - отсортированный список кортежей (путь, (r, g, b))
    # grid - (cols, rows)
    cols, rows = grid
    matrix = []
    pics_list = [pic[0] for pic in pics]  # только пути к изображениям
    total = cols * rows
    # Если картинок меньше, чем нужно, дополним None
    if len(pics_list) < total:
        pics_list += [None] * (total - len(pics_list))
    # Если больше, обрежем
    pics_list = pics_list[:total]
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(pics_list[r * cols + c])
        matrix.append(row)
    return matrix
    
        
def _sort_by_hue(pics: dict[str, tuple[float, float, float]]):
    return sorted(pics.items(), key=_get_hue)

def _get_hue(pic: tuple[str, tuple[float, float, float]]) -> float:
    rgb = pic[1]
    max_rgb = max(rgb)
    min_rgb = min(rgb)
    delta = max_rgb - min_rgb

    if max_rgb == min_rgb:
        return 0
    
    if max_rgb == rgb[0]:
        return 60 * (((rgb[1] - rgb[2]) / delta ) % 6)
    if max_rgb == rgb[1]:
        return 60 * (((rgb[2] - rgb[0]) / delta) + 2)
    if max_rgb == rgb[2]:
        return 60 * (((rgb[0] - rgb[1]) / delta) + 4)
    
    
