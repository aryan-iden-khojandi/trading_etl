from distutils.core import setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(name='trading_etl',
      author='Aryan Iden Khojandi',
      author_email='akhojandi@gmail.com',
      url='https://github.com/aryan-iden-khojandi/trading_etl',
      version='0.1',
      description='A package for high-frequency trade research.',
      long_description=readme,
      license=license,
      install_requires=['numpy', 'h5py', 'pandas', 'matplotlib'],
      packages=['trading_etl']
)
