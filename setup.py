from setuptools import setup, find_packages, Command


setup(
    name='bem',
    version='0.0.0',
    description='bem',
    author='',
    author_email='',
    packages=find_packages(exclude=('docs', '.circleci')),
    package_data={'bem': ['config/*.ini']},
    include_package_data=True,
    zip_safe=False,
)
