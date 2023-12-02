import block
import numpy as np

CHUNK_WIDTH = 100
CHUNK_HEIGHT = 100

class Chunk:
    def __init__(self, ctx, shader_prog):
        self.ctx = ctx
        self.shader_prog = shader_prog
        self.vbo = None
        self.vao = None
        self.blocks = np.zeros((CHUNK_WIDTH, CHUNK_HEIGHT))
        self.vertices = []

    def add_block(self, block_type, x, y, z):
        self.vertices.append(block.new_block(block_type, x, y, z))
    

    def init(self):
        """
        Call only if add_block() calls are over with.
        """
        self.vbo = self.ctx.buffer(np.array(self.vertices, dtype="f4"))
        self.vao = self.ctx.vertex_array(self.shader_prog, [(self.vbo, '3f 2f', 'in_pos', 'in_tex_coord')])
    

    def render(self):
        self.vao.render()