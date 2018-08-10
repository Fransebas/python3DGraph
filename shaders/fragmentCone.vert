 #version 330

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 tCoord;
layout (location = 2) in vec3 normal;

uniform mat4 M;
uniform mat4 P;
uniform mat4 V;
uniform vec3 colorVect;

out vec4 colorFrag;
out vec2 textCoord;
out vec3 vNormal;
out vec3 FragPos;

uniform float scale = 5.0;

void main()
{
        vec3 position2 = position.xyz;
        vec3 normal2 = normal.xyz;

        colorFrag = vec4(colorVect, 1);
        vec4 pos =  M * vec4(position2, 1.0);
        pos[3] = scale;
        gl_Position = P * V * pos;
        textCoord = tCoord;
        FragPos = vec3(M * vec4(position2, scale));
        vNormal = normalize(normal2);
}