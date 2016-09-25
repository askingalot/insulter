from setuptools import setup

setup(
    name='insulter-web',
    version='0.1',
    py_modules=['insulter_web'],
    include_package_data=True,
    install_requires=[
        'flask', 'insulter'
    ]
)
