import random
import block
import numpy as np
import glm

class Block:
    def __init__(self, ctx, shader_prog):
        self.ctx = ctx  # OpenGL context
        self.shader_prog = shader_prog  # helps us connect to shaders
        self.vbo = None  # object that holds vertex data
        self.vao = None  # object that holds attributes about vertex data
        self.pos = (0, 0, 0)

        # vertices that hold data that GPU needs to draw on to screen
        self.vertices = []

        self.angle = 0
        self.d_angle = random.choice([-1, 1])
        self.color = random.choice([glm.vec3(0, 255, 17), glm.vec3(255, 43, 43), glm.vec3(242, 255, 0), glm.vec3(0, 94, 255)])

    def add_block(self, block_type, x, y, z):
        self.vertices.append(block.new_block(block_type, x, y, z))
        self.pos = (x, y, z)

    def init(self):
        """
        Call only if add_block() calls are over with.
        """
        self.vbo = self.ctx.buffer(np.array(self.vertices, dtype="f4"))
        self.vao = self.ctx.vertex_array(
            self.shader_prog,
            [(self.vbo, "3f 2f 1f", "in_pos", "in_tex_coord", "in_ambient")],
        )

    def render(self):
        self.vao.render()
