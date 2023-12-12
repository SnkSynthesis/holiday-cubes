#version 330 core

layout (location = 0) in vec3 in_pos;
layout (location = 1) in vec2 in_tex_coord;
layout (location = 2) in float in_ambient;

out vec2 tex_coord;
out float ambient_val;

uniform mat4 m_proj;
uniform mat4 m_view;
uniform mat4 m_transformation;

void main() {
    gl_Position = m_proj * m_view * m_transformation * vec4(in_pos, 1.0);
    tex_coord = in_tex_coord;
    ambient_val = in_ambient;
}