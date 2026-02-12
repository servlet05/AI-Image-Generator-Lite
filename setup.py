from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ai-image-generator-lite",
    version="0.1.0",
    author="Tu Nombre",
    description="Generador de imágenes IA ultra liviano para CPU",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/servlet05/AI-Image-Generator-Lite",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "optimum-intel[openvino]>=1.14.0",
        "diffusers>=0.24.0",
        "pillow>=10.0.0",
    ],
)
