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
out vec3 lightPos;

vec3 initLightPos = vec3(0.3, 0.6, 0);

uniform float scale = 5.0;

void main()
{
        vec4 pos =  M * vec4(position, 1.0);
        lightPos = (V * vec4(initLightPos,1.0)).xyz;
        //lightPos = (vec4(initLightPos,1.0)).xyz;
        pos[3] = scale;
        gl_Position = P * V * pos;
        textCoord = tCoord;
        FragPos = vec3(M * vec4(position, scale));
        vNormal = normalize(normal);
}