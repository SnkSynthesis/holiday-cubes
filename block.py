import numpy as np
from texture_atlas import get_tex_coords

class Block:
    def __init__(self, block_type, ctx, shader_prog):
        self.ctx = ctx
        self.shader_prog = shader_prog
        self.block_type = block_type

        self.left_tex_coords = get_tex_coords(self.block_type, 'left')
        print(self.left_tex_coords)
        self.right_tex_coords = get_tex_coords(self.block_type, 'right')
        self.front_tex_coords = get_tex_coords(self.block_type, 'front')
        self.back_tex_coords = get_tex_coords(self.block_type, 'back')
        self.bottom_tex_coords = get_tex_coords(self.block_type, 'bottom')
        self.top_tex_coords = get_tex_coords(self.block_type, 'top')

        self.vertices = np.array([
            # left
            -0.5, -0.5, -0.5, *self.left_tex_coords[0],
            0.5, -0.5, -0.5,  *self.left_tex_coords[1],
            0.5,  0.5, -0.5,  *self.left_tex_coords[2],
            0.5,  0.5, -0.5,  *self.left_tex_coords[3],
            -0.5,  0.5, -0.5, *self.left_tex_coords[4],
            -0.5, -0.5, -0.5, *self.left_tex_coords[5],

            # right
            -0.5, -0.5,  0.5, *self.right_tex_coords[0],
            0.5, -0.5,  0.5,  *self.right_tex_coords[1],
            0.5,  0.5,  0.5,  *self.right_tex_coords[2],
            0.5,  0.5,  0.5,  *self.right_tex_coords[3],
            -0.5,  0.5,  0.5, *self.right_tex_coords[4],
            -0.5, -0.5,  0.5, *self.right_tex_coords[5],

            # front
            -0.5,  0.5,  0.5, *self.front_tex_coords[0],
            -0.5,  0.5, -0.5, *self.front_tex_coords[1],
            -0.5, -0.5, -0.5, *self.front_tex_coords[2],
            -0.5, -0.5, -0.5, *self.front_tex_coords[3],
            -0.5, -0.5,  0.5, *self.front_tex_coords[4],
            -0.5,  0.5,  0.5, *self.front_tex_coords[5],

            # back
            0.5,  0.5,  0.5,  *self.back_tex_coords[0],
            0.5,  0.5, -0.5,  *self.back_tex_coords[1],
            0.5, -0.5, -0.5,  *self.back_tex_coords[2],
            0.5, -0.5, -0.5,  *self.back_tex_coords[3],
            0.5, -0.5,  0.5,  *self.back_tex_coords[4],
            0.5,  0.5,  0.5,  *self.back_tex_coords[5],

            # bottom
            -0.5, -0.5, -0.5, *self.bottom_tex_coords[0],
            0.5, -0.5, -0.5,  *self.bottom_tex_coords[1],
            0.5, -0.5,  0.5,  *self.bottom_tex_coords[2],
            0.5, -0.5,  0.5,  *self.bottom_tex_coords[3],
            -0.5, -0.5,  0.5, *self.bottom_tex_coords[4],
            -0.5, -0.5, -0.5, *self.bottom_tex_coords[5],

            # top
            -0.5,  0.5, -0.5, *self.top_tex_coords[0],
            0.5,  0.5, -0.5,  *self.top_tex_coords[1],
            0.5,  0.5,  0.5,  *self.top_tex_coords[2],
            0.5,  0.5,  0.5,  *self.top_tex_coords[3],
            -0.5,  0.5,  0.5, *self.top_tex_coords[4],
            -0.5,  0.5, -0.5, *self.top_tex_coords[5],
        ], dtype="f4")

        
        self.vbo = self.ctx.buffer(self.vertices)
        self.vao = self.ctx.vertex_array(self.shader_prog, [(self.vbo, '3f 2f', 'in_pos', 'in_tex_coord')])
    
    def render(self):
        self.vao.render()

    

