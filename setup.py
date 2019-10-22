from setuptools import setup

setup(
    name = 'scrap_flipkart',
    version = '0.1',
    install_requires = ['Click',],
    py_modules = ['scrap_flipkart'],
    entry_points = '''
    [console_scripts]
    startTask = scrap_flipkart:startTask
    '''
)