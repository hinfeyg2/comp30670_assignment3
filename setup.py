from setuptools import setup, find_packages
setup(name='LedSwitcher',
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'LedSwitcher = LedSwitcher.LedSwitcher:main'
              ]}
)