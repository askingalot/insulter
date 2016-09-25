from setuptools import setup

setup(
    name='insulter-cli',
    version='0.1',
    py_modules=['insulter_cli'],
    include_package_data=True,
    install_requires=[
        'click', 'insulter'
    ],
    entry_points='''
        [console_scripts]
        insult=insulter_cli:cli
    ''',
)
