#version 330

in vec2 textCoord;
in vec3 vNormal;
in vec3 FragPos;
out vec4 outColor;

in vec4 colorFrag;

vec4 ambient = vec4(0.3, 0.3, 0.3,1);

vec4 diffuse = vec4(1, 1, 1, 1);
vec3 lightPos = vec3(0.3, 0.6, 0);


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
    outColor = (getDiffuse() + ambient + getSpecular())*colorFrag + getSpecular();
    //outColor = vec4(vNormal,1);
}