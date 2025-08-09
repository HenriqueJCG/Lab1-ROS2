from setuptools import find_packages, setup

package_name = 'temperature_system'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/launch.py']),  
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='henrique',
    maintainer_email='henrique@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'enhanced_publisher_node = temperature_system.enhanced_publisher_node:main',
            'advanced_monitor_node = temperature_system.advanced_monitor_node:main',
            'logger_node = temperature_system.logger_node:main',
        ],
    },
)
