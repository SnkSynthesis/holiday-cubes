#version 330 core

in vec2 tex_coord;
in float ambient_val;
out vec4 frag_color;

uniform sampler2D texture0;

void main() {
    vec3 light_color = vec3(191, 200, 255) / 255.0;
    vec4 ambient = vec4(light_color * ambient_val, 1.0);
    frag_color = vec4(texture(texture0, tex_coord).xyz, 1.0) * ambient;
}