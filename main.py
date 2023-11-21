
import moderngl as gl
import moderngl_window as mglw
import numpy as np
from pathlib import Path
from pyrr import Matrix44

class Test(mglw.WindowConfig):
    gl_version = (3, 3)
    window_size = (900, 600)
    resource_dir= (Path().parent / 'resources').resolve()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Do initialization here
        self.vertices = np.array([(-0.6, -0.8, 0.0,), (0.6, -0.8, 0), (0.0, 0.8, 0.0)], dtype="f4")
        self.vbo = self.ctx.buffer(self.vertices)
        self.shader_prog = self.load_program(
            vertex_shader='vertexshader.glsl',
            fragment_shader='fragmentshader.glsl'
        )
        self.vao = self.ctx.vertex_array(self.shader_prog, [(self.vbo, '3f', 'in_pos')])

        self.camera = mglw.scene.KeyboardCamera(
            self.wnd.keys,
            fov=75.0,
            aspect_ratio=self.wnd.aspect_ratio,
            near=0.1,
            far=1000.0
        )

        self.camera.set_position(0, 0, -2)
    
    def key_event(self, key, action, modifiers):
        keys = self.wnd.keys
        if action == keys.ACTION_PRESS:
            if keys == keys.Q:
                exit()
        self.camera.key_input(key, action, modifiers)
    
    def mouse_position_event(self, x: int, y: int, dx: int, dy: int):
        self.camera.rot_state(-dx, -dy)

    def render(self, time, frametime):
        self.camera.projection.update(aspect_ratio=self.wnd.aspect_ratio)
        self.ctx.clear(0.0, 0.0, 0.0, 0.0)
        self.shader_prog["m_proj"].write(self.camera.projection.matrix)
        self.shader_prog["m_modelview"].write(self.camera.matrix)
        self.vao.render()

        
        
# Blocking call entering rendering/event loop
mglw.run_window_config(Test)
