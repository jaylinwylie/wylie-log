from setuptools import setup, find_packages

setup(
        name="wylielog",
        version="0.1.1",
        description="A logging utility with support for dynamic call depth tracking and function/class IO logging.",
        author="Jaylin Io Wylie",
        author_email="jaylinwylie@gmail.com",
        url="https://github.com/jaylinwylie/wylielog",
        packages=find_packages(),
        py_modules=["wylielog"],
        license="MIT",
        classifiers=[
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",
        ],
        python_requires=">=3.11",
        install_requires=[],
        long_description=open("README.md").read(),
        long_description_content_type="text/markdown"
)