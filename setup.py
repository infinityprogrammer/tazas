from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in tazas/__init__.py
from tazas import __version__ as version

setup(
	name="tazas",
	version=version,
	description="Tazas App",
	author="RAFI",
	author_email="info@taza.iq",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
