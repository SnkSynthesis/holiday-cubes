
import moderngl as mgl
import moderngl_window as mglw
import numpy as np
from pathlib import Path
from cube import Cube

# This class inherits from moderngl_window's WindowConfig class
# The WindowConfig creates a window and sets up the OpenGL (low-level graphics interface written in C)
class Test(mglw.WindowConfig):
    gl_version = (3, 3)
    window_size = (900, 600)
    resource_dir = (Path().parent / 'resources').resolve()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Make sure faces are being drawn in correct order.
        self.ctx.enable(flags=mgl.DEPTH_TEST)

        # Load shader program (programs that process graphics data on GPU)
        self.shader_prog = self.load_program(
            vertex_shader='shaders/vertexshader.glsl',  # this handles vertices (or positions)
            fragment_shader='shaders/fragmentshader.glsl'  # this handles the colors
        )

        self.cube1 = Cube(self.ctx, self.shader_prog)

        # Simple camera class from moderngl window to move around world with keyboard and mouse
        self.camera = mglw.scene.KeyboardCamera(
            self.wnd.keys,
            fov=75.0,
            aspect_ratio=self.wnd.aspect_ratio,
            near=0.1,
            far=1000.0
        )

        self.camera.set_position(0, 0, -2)
    
    def key_event(self, key, action, modifiers):
        if action == self.wnd.keys.ACTION_PRESS:
            if key == self.wnd.keys.C:
                self.wnd.mouse_exclusivity = not self.wnd.mouse_exclusivity

        self.camera.key_input(key, action, modifiers)
    
    def mouse_position_event(self, x: int, y: int, dx: int, dy: int):
        if self.wnd.mouse_exclusivity:
            self.camera.rot_state(-dx, -dy)

    def render(self, time, frametime):
        self.camera.projection.update(aspect_ratio=self.wnd.aspect_ratio)

        self.ctx.clear(0.0, 0.0, 0.0, 0.0)
        self.shader_prog["m_proj"].write(self.camera.projection.matrix)
        self.shader_prog["m_modelview"].write(self.camera.matrix)
        # self.vao.render()
        self.cube1.render()

        
        
# Blocking call entering rendering/event loop
mglw.run_window_config(Test)
