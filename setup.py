from setuptools import setup


setup(
    name='ptvsd wrapper',
    license='MIT',
    version='0.1',
    description=(
        'Python wrapper for remote debugging with Visual Studio Code.'
    ),
    author='Yannick Chabbert',
    author_email='yannick.chabbert@gmail.com',
    # url='https://github.com/ychab/ptvsd_wrapper',
    scripts=['ptvsd_wrapper.py'],
    install_requires=['ptvsd'],
    extras_require={
        "pylint": ["pylint"],
    },
    keywords='Python, Visual Studio Code, Debug, Remote Debugging',
    classifiers=[
        'Intended Audience :: Developers',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Debuggers',
    ],
)
