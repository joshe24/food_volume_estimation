from setuptools import setup, find_packages

setup(
    name='food_volume_estimation',
    version='0.1.5',
    install_requires=[
        'PyYAML==6.0.2',
        'opencv-contrib-python-headless==4.11.0.86',
        'numpy<2',
        'open3d==0.19.0',
        'scipy==1.15.3'
    ]
)
