from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'yoga_mitra'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name), glob('launch/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='wagle',
    maintainer_email='aniruddhawagle@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "talk=yoga_mitra.talker:main",
            "listen=yoga_mitra.listener:main",
        ],
    },
)
