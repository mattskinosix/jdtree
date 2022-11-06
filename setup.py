from setuptools import find_packages, setup
setup(
    name='jdtree',
    packages=find_packages(include=['jdtree']),
    version='0.0.1',
    description='Json Decision Tree',
    author='Matteo Greco',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)
