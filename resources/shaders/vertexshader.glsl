#version 330 core

layout (location = 0) in vec3 in_pos;
layout (location = 1) in vec2 in_tex_coord;

out vec2 tex_coord;

uniform mat4 m_proj;
uniform mat4 m_modelview;

void main() {
    gl_Position = m_proj * m_modelview * vec4(in_pos, 1.0);
    tex_coord = in_tex_coord;
}