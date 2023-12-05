from texture_atlas import get_tex_coords
def new_block(block_type, x, y, z):
    left_tex_coords = get_tex_coords(block_type, 'left')
    right_tex_coords = get_tex_coords(block_type, 'right')
    front_tex_coords = get_tex_coords(block_type, 'front')
    back_tex_coords = get_tex_coords(block_type, 'back')
    bottom_tex_coords = get_tex_coords(block_type, 'bottom')
    top_tex_coords = get_tex_coords(block_type, 'top')

    vertices = [
        # left
        -0.5, -0.5, -0.5, *left_tex_coords[0], 0.8,
        0.5, -0.5, -0.5,  *left_tex_coords[1], 0.8,
        0.5,  0.5, -0.5,  *left_tex_coords[2], 0.8,
        0.5,  0.5, -0.5,  *left_tex_coords[3], 0.8,
        -0.5,  0.5, -0.5, *left_tex_coords[4], 0.8,
        -0.5, -0.5, -0.5, *left_tex_coords[5], 0.8,

        # right
        -0.5, -0.5,  0.5, *right_tex_coords[0], 0.85,
        0.5, -0.5,  0.5,  *right_tex_coords[1], 0.85,
        0.5,  0.5,  0.5,  *right_tex_coords[2], 0.85,
        0.5,  0.5,  0.5,  *right_tex_coords[3], 0.85,
        -0.5,  0.5,  0.5, *right_tex_coords[4], 0.85,
        -0.5, -0.5,  0.5, *right_tex_coords[5], 0.85,

        # front
        -0.5,  0.5,  0.5, *front_tex_coords[0], 0.65,
        -0.5,  0.5, -0.5, *front_tex_coords[1], 0.65,
        -0.5, -0.5, -0.5, *front_tex_coords[2], 0.65,
        -0.5, -0.5, -0.5, *front_tex_coords[3], 0.65,
        -0.5, -0.5,  0.5, *front_tex_coords[4], 0.65,
        -0.5,  0.5,  0.5, *front_tex_coords[5], 0.65,

        # back
        0.5,  0.5,  0.5,  *back_tex_coords[0], 0.7,
        0.5,  0.5, -0.5,  *back_tex_coords[1], 0.7,
        0.5, -0.5, -0.5,  *back_tex_coords[2], 0.7,
        0.5, -0.5, -0.5,  *back_tex_coords[3], 0.7,
        0.5, -0.5,  0.5,  *back_tex_coords[4], 0.7,
        0.5,  0.5,  0.5,  *back_tex_coords[5], 0.7,

        # bottom
        -0.5, -0.5, -0.5, *bottom_tex_coords[0], 0.3,
        0.5, -0.5, -0.5,  *bottom_tex_coords[1], 0.3,
        0.5, -0.5,  0.5,  *bottom_tex_coords[2], 0.3,
        0.5, -0.5,  0.5,  *bottom_tex_coords[3], 0.3,
        -0.5, -0.5,  0.5, *bottom_tex_coords[4], 0.3,
        -0.5, -0.5, -0.5, *bottom_tex_coords[5], 0.3,

        # top
        -0.5,  0.5, -0.5, *top_tex_coords[0], 1.0,
        0.5,  0.5, -0.5,  *top_tex_coords[1], 1.0,
        0.5,  0.5,  0.5,  *top_tex_coords[2], 1.0,
        0.5,  0.5,  0.5,  *top_tex_coords[3], 1.0,
        -0.5,  0.5,  0.5, *top_tex_coords[4], 1.0,
        -0.5,  0.5, -0.5, *top_tex_coords[5], 1.0,
    ]

    for i in range(0, len(vertices), 6):
        vertices[i + 0] += x
        vertices[i + 1] += y
        vertices[i + 2] += z
    
    return vertices