from setuptools import find_packages, setup

package_name = 'sensor_fusion_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/sensor_fusion_pkg/launch', ['launch/fused_data_launch.py'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sreekompe',
    maintainer_email='sreekompe@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'fused_data = sensor_fusion_pkg.fused_data:main'
        ],
    },
)
