from distutils.core import setup

setup(
    name="huffman",
    author="Kaden Thomas",
    author_email="thomas.kaden4@outlook.com",
    license="MIT",
    keywords="encoding compression tools",
    version="0.1.0",
    install_requires=["heapq"],
    python_requires=">=3.5"
    packages=["huffman"]
)
