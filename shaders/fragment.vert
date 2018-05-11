#version 330

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 tCoord;
layout (location = 2) in vec3 normal;

uniform mat4 M;
uniform mat4 P;
uniform mat4 V;
out vec2 textCoord;
out vec3 vNormal;
out vec3 FragPos;

uniform float scale = 5.0;

void main()
{
        gl_Position = P * V * M * vec4(position, scale);
        textCoord = tCoord;
        FragPos = vec3(M * vec4(position, scale));
        vNormal = normalize(normal);
}