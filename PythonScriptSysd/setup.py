from setuptools import setup

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
    install_requires=[], # Add dependencies here, e.g., ['requests']
)