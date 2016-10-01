from setuptools import setup


setup(name='uricrawl',
      version='0.2.1',
      description='Command Line Tool for crawl and '
      'render templates for Problems for URI (Uri Online Judge)',
      url='https://github.com/pyanderson/uricrawl',
      author='Anderson Lima',
      author_email='anderson.sl93@hotmail.com',
      license='MIT',
      install_requires=['scrapy', 'python-slugify', 'jinja2'],
      packages=['uricrawl', ],
      include_package_data=True,
      zip_safe=False,
      entry_points={
          'console_scripts': ['uricrawl=uricrawl.cmdline:main']
      }
      )
