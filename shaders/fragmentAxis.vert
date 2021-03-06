#version 330

layout (location = 0) in vec3 position;

uniform mat4 M;
uniform mat4 P;
uniform mat4 V;

uniform float scale = 2.0;

void main()
{
        gl_Position = P * V * M * vec4(position, 1.0);
}