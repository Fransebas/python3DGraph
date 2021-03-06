#version 330

in vec2 textCoord;
in vec3 vNormal;
in vec3 FragPos;
out vec4 outColor;

uniform sampler2D text;



vec4 pixel;
vec4 ambient = vec4(0.3, 0.3, 0.3,1);

vec4 diffuse = vec4(1, 1, 1, 1);
in vec3 lightPos;


vec3 viewPos = vec3(0,0,-1);
float specularStrength = 1;
vec4 lightColor = vec4(1, 1, 1,1);

vec4 getSpecular()
{
    vec3 lightDir = normalize(lightPos - FragPos);
    vec3 viewDir = normalize(viewPos - FragPos);
    vec3 reflectDir = reflect(-lightDir, vNormal);
    float spec = pow(max(dot(viewDir, reflectDir), 0.0), 32);
    return specularStrength * spec * lightColor;
}

vec4 getDiffuse()
{
    vec3 lightDir = normalize(lightPos - FragPos);
    float diff = max(dot(vNormal, lightDir), 0.0);
    return diff*diffuse;
}

void main()
{


    pixel = texture(text, textCoord);
    if (pixel.x > 0.5)
        outColor = (getDiffuse() + ambient + getSpecular())*vec4(0,1,0,1) + getSpecular();
    else
        outColor = (getDiffuse() + ambient + getSpecular())*vec4(0,0.5,0,1) + getSpecular();
    //outColor = vec4(vNormal,1);
}