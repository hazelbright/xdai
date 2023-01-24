import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='XDAI',  
     version='0.0',
     author="Audun Skau Hansen, Elias Dalan and Hanan Gharayba",
     author_email="a.s.hansen@kjemi.uio.no",
     description="Artificial intelligence for experimental design",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.uio.no/hazelbright/xdai",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     install_requires = ["numpy", "scipy", "matplotlib"],
 )
