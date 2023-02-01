from setuptools import setup

setup(
    name='jdtree',
    packages=['jdtree'],
    version='0.0.4',
    description='Json Decision Table/Tree',
    author='Matteo Greco',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
    long_description_content_type="text/markdown",
    long_description='Json Decision Table/Tree',
)
