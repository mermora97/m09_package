from setuptools import setup

setup(
    name='booklover package',
    version='1.0.0',
    url='https://github.com/mermora97',
    author='Mercedes Mora-Figueroa',
    author_email='eqa7yg@virginia.edu',
    description='Description of my package',
    license='MIT',
    packages = ['booklover'],
    install_requires = [
        "pandas",
    ],
)