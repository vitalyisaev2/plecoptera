from setuptools import setup, find_packages
import pathlib

HERE = pathlib.Path(__file__).parent

setup(name='plecoptera',
      version_config={
          "dev_template": "{tag}",
      },
      description='Find better configuration of your Go service with global optimization algorithms',
      author='Vitaly Isaev',
      author_email='vitalyisaev2@gmail.com',
      url='https://github.com/vitalyisaev2/plecoptera',
      packages=find_packages(),
      setup_requires=["setuptools-git-versioning"],
      install_requires=(
          "jsons==1.6.0",
          "numpy==1.21.4",
          "Pyomo==6.1.2",
          "rbfopt==4.2.2",
          "requests==2.26.0",
          "urllib3==1.26.7",
      ),
      license_file="LICENSE",
      package_dir={
          '': '.'
      },
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Topic :: Scientific/Engineering :: Mathematics",
      ],
      entry_points={
          'console_scripts': [
              'plecoptera = plecoptera.main:main',
          ]
      },
      zip_safe=False,
      python_requires=">=3.7",
      )
