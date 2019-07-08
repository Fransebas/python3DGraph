<h1> Graphy - 3D Graphing calculator in python </h1>

The software uses pyOpengl and glfw to be able to graph 3D ecuations. It's inspired in grapher from mac.

<h1> Dependencies </h1>

### Python

It currently support python3

* install : `pip3 install PyOpenGL PyOpenGL_accelerate`  reference : [PyOpengl](http://pyopengl.sourceforge.net/documentation/installation.html)

* install : `pip3 install pyqt5` reference : [pyqt5](http://pyqt.sourceforge.net/Docs/PyQt5/installation.html)

* install : `pip3 install PyGLM` reference : [glm](https://pypi.org/project/PyGLM/)

* install : `pip3 install Pillow` reference : [PIL / Pillow](https://pillow.readthedocs.io/en/latest/installation.html)

* install : `pip3 install sympy` reference : [pip installation of sympy](https://pypi.org/project/sympy/), site [Sympy](http://www.sympy.org/en/index.html)

* install : `pip install numpy` reference : [pip installation of numpy](https://pypi.org/project/numpy/), site [numpy](http://www.numpy.org)

Useful one-liner
`pip3 install PyOpenGL PyOpenGL_accelerate pyqt5 PyGLM Pillow sympy numpy`

## Attention!
For some reason the try and catch doesn't work and if you type an ecuation wrong it breaks, I know it's really anoying and I'm going to fix it latter.

### OpenGL

Currently the shaders are only for `#version 330` but I think It will be easy to change the shader for other versions.

<h2> Supported graphs </h2>

  * Tow variable function of the form z = f(x,y) , example `x**2 + y**2`
  * Parametric functions of the form f(t) = [ g(t), h(t), p(t) ]
  * Vector Fields of the form f(x,y,z) = g(x,y,z)*i + h(x,y,z)*j + q(x,y,z)*k , example `z*i + y*j + x*k : VField`


![image](https://i.imgur.com/yZOvREQ.png)
![image](https://i.imgur.com/RWqbJ6q.png)

