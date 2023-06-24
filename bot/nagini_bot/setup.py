from setuptools import setup, find_namespace_packages

setup(
    name='nagini_bot',
    version='0.1.1',
    description='Personal assistant',
    url='https://github.com/svitlana2299/Nagini_team',
    author='Nagini_team',
    license='MIT',
    packages= find_namespace_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"],   
    entry_points={'console_scripts': ['nagini-bot=nagini_bot.main:start_bot']}

)