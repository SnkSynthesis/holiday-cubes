#version 330 core

in vec2 tex_coord;
out vec4 frag_color;

uniform sampler2D texture0;

void main() {
    frag_color = vec4(texture(texture0, tex_coord).xyz, 1.0);
}