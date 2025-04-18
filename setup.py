import setuptools
import distutils.core

setuptools.setup(
    name='obsidian-plugin-stats',
    version=0.1,
    author='Author',
    long_description_content_type='text/markdown',
    author_email='Email',
    description='',
    license='GPLv3',
    keywords='',
    url='',
    packages=["obsidian_plugin_stats"],
    long_description=open('README.md').read(),
    entry_points={
        'console_scripts': ['obsidian-plugin-stats=obsidian_plugin_stats.main:main']},
    classifiers=[
    ],
    test_suite='nose.collector'
)
