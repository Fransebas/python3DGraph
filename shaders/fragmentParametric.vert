#version 330

layout (location = 0) in vec3 position;

uniform mat4 M;
uniform mat4 P;
uniform mat4 V;

uniform float scale = 5.0;

void main()
{
        vec4 pos =  M * vec4(position, 1.0);
        pos[3] = scale;
        gl_Position = P * V * pos;
        //gl_Position[3] = scale;
}