from setuptools import setup

requirements = [
    # TODO: put your package requirements here
    'PyQt5',
    'opencv-python',
    'opencv-contrib-python',
    'pyrealsense2',  # i add by my demand
    'pywin32',  # fix confliction btw PyQt5 & pyrealsense2
    'pep8',  # auto format
    'autopep8',  # auto format
    'PyQtDataVisualization',  # chap 6
]

setup(
    install_requires=requirements,
    classifiers=[
        'Programming Language :: Python :: 3.7'
    ],
)
