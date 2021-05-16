from setuptools import setup, find_packages
import os

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

with open(os.path.join("tbomb", ".version"), "r", encoding="utf8") as fh:
    version = fh.read().strip()

with open("requirements.txt", "r", encoding="utf8") as fh:
    requirements = fh.read().strip().splitlines()


setup(
    name='tbomb',
    packages=find_packages(),
    include_package_data=True,
    version=version,
    description='A free and open-source SMS,Call & Mail bombing application',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='TheSpeedX',
    author_email='ggspeedx29@gmail.com',
    url='https://github.com/TheSpeedX/TBomb',
    download_url="https://github.com/TheSpeedX/TBomb/archive/pypi.zip",
        keywords=['android', 'spam', 'sms', 'mail', 'tbomb',
                  'call', 'bomb', 'termux', 'bomber', 'spammer'],
    classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Programming Language :: Python :: 3',
            'Operating System :: OS Independent',
            'Environment :: Console',
    ],
    install_requires=requirements,
    license='GPL',
    entry_points={
            'console_scripts': [
                'tbomb = tbomb.bomber:main',
            ],
    },
    python_requires='>=3.5'
)
