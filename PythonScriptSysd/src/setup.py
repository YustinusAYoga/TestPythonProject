from setuptools import setup
from Cython.Build import cythonize

setup(
    name="python-hello-service",
    version="1.0.0",
    description="A simple Hello World systemd service",
    author="Your Name",
    # This installs the script into /usr/bin/
    scripts=['hello_world.py'], 
    # This places the service file into the systemd directory
    data_files=[
        ('/etc/systemd/system', ['helloworld.service'])
    ],
    install_requires=[], # Add dependencies here, e.g., ['requests'],
    ext_modules=cythonize("helloworldsysd.pyx", compiler_directives={"language_level": "3"})
)