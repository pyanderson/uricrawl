from setuptools import setup


setup(name='uritool',
      version='0.2',
      description='Command Line Tool for crawl and '
      'render templates for Problems for URI (Uri Online Judge)',
      url='https://github.com/pyanderson/uritool',
      author='Anderson Lima',
      author_email='anderson.sl93@hotmail.com',
      license='MIT',
      install_requires=['scrapy', 'python-slugify', 'jinja2'],
      packages=['uritool', ],
      include_package_data=True,
      zip_safe=False,
      entry_points={
          'console_scripts': ['uritool=uritool.cmdline:main']
      }
      )
