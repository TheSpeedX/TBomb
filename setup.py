from setuptools import setup

with open("README.md", "r") as fh:
	long_description = fh.read()
setup(
	name = 'insh',
	packages = ['insh'],
   	version = '1.3',
	description = 'Insults You When You Get An Error',
	long_description=long_description,
	long_description_content_type="text/markdown",
	author='TheSpeedX',
	author_email='ggspeedx29@gmail.com',
	url = 'https://github.com/TheSpeedX/insh',
	download_url ="https://github.com/TheSpeedX/insh/archive/master.zip",
	keywords = ['shell','funny','insult','python'],
	data_files=[('', ['LICENSE'])],
	classifiers=[
	'Development Status :: 4 - Beta',
	'Intended Audience :: Developers',
	'Topic :: Software Development :: Libraries :: Python Modules',
	'License :: OSI Approved :: MIT License',
	'Programming Language :: Python :: 3',
	'Programming Language :: Python :: 3.4',
	'Programming Language :: Python :: 3.5',
	'Programming Language :: Python :: 3.6',
	'Programming Language :: Python :: 3.7',
	'Operating System :: OS Independent',
	'Environment :: Console',
	],
    license = 'MIT',
	entry_points={
        'console_scripts': [
            'insh = insh.insh:main',
        ],
		}
)
