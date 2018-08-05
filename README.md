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

### OpenGL

Currently the shaders are only for `#version 330` but I think It will be easy to change the shader for other versions.

<h2> Supported graphs </h2>
<ul>
  <li> Tow variable function of the form z = f(x,y) </li>
  <li> Parametric functions of the form f(t) = [ g(t), h(t), p(t) ]</li>
</ul>

![image](https://i.imgur.com/7etOedx.png)
