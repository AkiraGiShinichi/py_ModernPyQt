from setuptools import setup

requirements = [
    # TODO: put your package requirements here
    'PyQt5',
    'opencv-python',
    'opencv-contrib-python',
    'pyrealsense2',
    'pywin32',
    'pep8',
    'autopep8',
]

setup(
    install_requires=requirements,
    classifiers=[
        'Programming Language :: Python :: 3.7'
    ],
)
