TEX_WIDTH = 32.0 / 128.0  # width of each texture divided by width of total image.


def get_tex_coords(block_type, face):
    texture_index = {
        "sand": (2, 0),
        "water": (2, 1),
        "grass_top": (1, 0),
        "grass_side": (1, 1),
        "dirt": (0, 0),
        "stone": (0, 1),
    }

    texture_pos = None
    # set each face to different texture for grass block
    if block_type == "grass":
        match face:
            case "top":
                texture_pos = texture_index["grass_top"]
            case "bottom":
                texture_pos = texture_index["dirt"]
            case _:
                texture_pos = texture_index["grass_side"]
    else:  # all other blocks have same texture for each face
        texture_pos = texture_index[block_type]
    offset_x = TEX_WIDTH * texture_pos[1]
    offset_y = TEX_WIDTH * texture_pos[0]

    top_left = (0.0 + offset_x, TEX_WIDTH + offset_y)
    top_right = (TEX_WIDTH + offset_x, TEX_WIDTH + offset_y)
    bottom_left = (0.0 + offset_x, 0.0 + offset_y)
    bottom_right = (TEX_WIDTH + offset_x, 0.0 + offset_y)

    match face:
        case "top" | "bottom":
            return (
                top_left,
                top_right,
                bottom_right,
                bottom_right,
                bottom_left,
                top_left,
            )
        case "left" | "right":
            return (
                bottom_left,
                bottom_right,
                top_right,
                top_right,
                top_left,
                bottom_left,
            )
        case "front" | "back":
            return (
                top_right,
                top_left,
                bottom_left,
                bottom_left,
                bottom_right,
                top_right,
            )
