from setuptools import setup

setup(
    name='mistra-providers',
    version='0.0.4',
    packages=['mistra.providers.realtime.truefx',
              'mistra.providers.historical.truefx',
              'mistra.providers.historical.filesystem'],
    url='',
    license='MIT',
    author='luismasuelli',
    author_email='luisfmasuelli@gmail.com',
    description='MISTRA Providers contains a collection of custom providers for the MISTRA package',
    python_requires='>=3.3',
    install_requires=['mistra==0.0.1']
)
