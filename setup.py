import setuptools

with open('requirements.txt') as f:
     reqs = f.read().split('\n')

setuptools.setup(
    name='pylidator',
    version='1.1',
    scripts=[],
    author="Rajat Kumar Panda",
    author_email="rajat.panda98@gmail.com",
    description="Python schema validator",
    long_description="Python schema validator",
    long_description_content_type="text/markdown",
    url="https://github.com/rajatkumarpanda/pylidator.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=reqs
)
