import moderngl as mgl
import moderngl_window as mglw
from pathlib import Path
import random
from blockmesh import Block
import util
import glm

# This class inherits from moderngl_window's WindowConfig class
# The WindowConfig creates a window and sets up the OpenGL (low-level graphics interface written in C)
class App(mglw.WindowConfig):
    gl_version = (3, 3)  # version of OpenGL
    window_size = (900, 600)
    resource_dir = (
        Path().parent / "resources"
    ).resolve()  # directory to get assets like textures
    aspect_ratio = (
        None  # set aspect ratio to None in order to avoid bars at top of screen
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Make sure faces are being drawn in correct order.
        self.ctx.enable(flags=mgl.DEPTH_TEST)

        # Load shader program (programs that process graphics data on GPU)
        self.shader_prog = self.load_program(
            vertex_shader="shaders/vertexshader.glsl",  # this handles vertices (or positions)
            fragment_shader="shaders/fragmentshader.glsl",  # this handles the colors
        )

        # set value of texture to 0 to avoid errors
        self.shader_prog["texture0"].value = 0

        self.blocks = []
        for i in range(100):
            for j in range(100):
                c = Block(self.ctx, self.shader_prog)
                c.add_block(
                    random.choice(["sand", "dirt", "stone"]),
                    i,
                    random.randint(0, 200),
                    j,
                )
                c.init()
                self.blocks.append(c)

        # load texture (all textures combined into one image for performance and ease of use)
        self.tex = self.load_texture_2d("images/atlas.png", mimap=True, anisotrpy=0.0)
        self.tex.filter = (
            mgl.NEAREST,
            mgl.NEAREST,
        )  # set to NEAREST for pixelated look

        # Simple camera class from moderngl window to move around world with keyboard and mouse
        self.camera = mglw.scene.KeyboardCamera(
            self.wnd.keys,
            fov=75.0,
            aspect_ratio=self.wnd.aspect_ratio,
            near=0.1,
            far=1000.0,
        )

        self.camera.set_position(0, 0, -2)

        # used to calculate FPS which is frames / time passed
        self.frames = 0
        self.fpstime = 0

    def key_event(self, key, action, modifiers):
        # make mouse disappear and be exclusive to window if key C is pressed.
        if action == self.wnd.keys.ACTION_PRESS:
            if key == self.wnd.keys.C:
                self.wnd.mouse_exclusivity = not self.wnd.mouse_exclusivity

        self.camera.key_input(key, action, modifiers)

    def mouse_position_event(self, x, y, dx, dy):
        # update camera rotation relative to position of mouse
        if self.wnd.mouse_exclusivity:
            self.camera.rot_state(-dx, -dy)

    def resize(self, width, height):
        # resize to update aspect ratio
        self.camera.projection.update(aspect_ratio=self.wnd.aspect_ratio)

    def render(self, time, frametime):
        # calculate FPS and write FPS in window title
        self.fpstime += frametime
        self.frames += 1
        if self.fpstime > 1.0:
            self.wnd.title = f"FPS: {int(self.frames / self.fpstime)}"

        # clear screen
        self.ctx.clear(*util.rgb255_to_rgb1(41, 45, 71), 0.0)

        

        # set variables in shader
        self.shader_prog["m_proj"].write(self.camera.projection.matrix)
        self.shader_prog["m_view"].write(self.camera.matrix)
        self.tex.use(location=0)

        for block in self.blocks:
            block.angle += block.d_angle * random.randint(1, 5) * 1 * frametime
            rot = glm.rotate(glm.mat4(1.0), block.angle, glm.vec3(*block.pos))
            self.shader_prog["m_transformation"].write(glm.mat4(1.0) * rot)
            block.render()


if __name__ == "__main__":
    # Blocking call entering rendering/event loop
    mglw.run_window_config(App)
