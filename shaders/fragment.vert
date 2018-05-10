#version 330
layout (location = 0) in vec3 position;
uniform mat4 M;
out vec3 newColor;
void main()
{
        gl_Position = M * vec4(position, 1.0f);
        newColor = position;
}