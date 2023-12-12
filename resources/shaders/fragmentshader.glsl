#version 330 core

in vec2 tex_coord;
in float ambient_val;
out vec4 frag_color;

uniform sampler2D texture0;
uniform vec3 rgb_light_color;

void main() {
    vec3 light_color = rgb_light_color / 255.0;
    vec4 ambient = vec4(light_color * ambient_val, 1.0);
    frag_color = vec4(texture(texture0, tex_coord).xyz, 1.0) * ambient;
}