import setuptools

try:
    with open('README.md') as f:
        long_description = f.read()
except IOError:
    long_description = ""

requirements = ['boto3']

setuptools.setup(
    name='awswrapper',
    license='BSD',
    author='Hector Reyes Aleman',
    author_email='hector@eclecticiq.com',
    install_requires=requirements,
    version='0.3.0',
    packages=['awswrapper'],
    description='Wrapper of AWS API to use with Lambda',
    long_description=long_description,
    url='https://github.com/EclecticIQ/python-aws-wrapper'
)
