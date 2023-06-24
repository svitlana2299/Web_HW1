from setuptools import setup, find_packages

setup(
    name='myassistantbot',  # Назва пакету
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'myassistantbot = main:main'  # Назва команди та шлях до точки входу вашого бота
        ]
    },
    install_requires=[
        'requests',
        'datetime',
        'os',
        'json',
        'pathlib'
    ],
)
