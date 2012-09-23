from distutils.core import setup

setup(
        name='Poodledo',
        version='0.1dev',
        packages=['poodledo',],
        # TODO: not sure how to reference this license
        license='see LICENSE.txt',
        # TODO: should be a ReST file
        long_description=open('README.markdown').read(),
)
