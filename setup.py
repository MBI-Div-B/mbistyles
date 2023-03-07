from setuptools import setup, find_packages

setup(
    name='mbistyles',
    version='1.0',
    packages=find_packages(),
    url='https://github.com/MBI-Div-B/mbistyles',
    install_requires=['matplotlib'],
    license='MIT',
    author='Daniel Schick',
    author_email='schick@mbi-berlin.de',
    description='Matplotlib styles inspired by MBI design',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    package_data={
        'mbistyles': ['*.mplstyle']
    },
    python_requires='>=3.5',
    keywords='matplotlib style sheet mbi max born institute',
)
