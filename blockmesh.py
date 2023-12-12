import random
import block
import numpy as np
import glm


class Block:
    def __init__(self, block_type, ctx, shader_prog):
        self.ctx = ctx  # OpenGL context
        self.shader_prog = shader_prog  # helps us connect to shaders
        self.vbo = None  # object that holds vertex data
        self.vao = None  # object that holds attributes about vertex data
        self.pos = (0, 0, 0)

        # vertices that hold data that GPU needs to draw on to screen
        self.vertices = []

        # type of block e.g. sand, dirt, stone, etc.
        self.block_type = block_type

        # angle in degrees
        self.angle = 0.0

        # block.d_angle whether change in angle should be positive or negative
        self.d_angle = random.choice([-1, 1])

        # randomly chooses one of the given colors (in RGB vectors)
        self.color = random.choice(
            [
                glm.vec3(0, 255, 17),
                glm.vec3(255, 43, 43),
                glm.vec3(242, 255, 0),
                glm.vec3(0, 94, 255),
            ]
        )

        self.pos = (0, 0, 0)
    
    def update(self, time, frametime):
        """
        Updates rotation and sends updated values to GPU
        """
        # update angle of rotation
        self.angle += self.d_angle * random.randint(1, 5) * 1 * frametime

        # rotation matrix
        rot = glm.rotate(glm.mat4(1.0), self.angle, glm.vec3(*self.pos))

        # send rotation and light_color to GPU (received by shaders)
        self.shader_prog["m_transformation"].write(rot)
        self.shader_prog["rgb_light_color"].write(self.color)

    def init(self):
        """
        Initialization code
        """
        self.vertices.append(block.new_block(self.block_type, *self.pos))
        self.vbo = self.ctx.buffer(np.array(self.vertices, dtype="f4"))
        self.vao = self.ctx.vertex_array(
            self.shader_prog,
            [(self.vbo, "3f 2f 1f", "in_pos", "in_tex_coord", "in_ambient")],
        )

    def render(self):
        self.vao.render()
