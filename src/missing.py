import pkg_resources
import pip
from pkg_resources import DistributionNotFound, VersionConflict
import os


# dependencies can be any iterable with strings, 
# e.g. file line-by-line iterator
# dependencies = [
#   'Werkzeug>=0.6.1',
#   'semantic_version>=0.9',
# ]


# Read in requiremetns.txt file
# with open('requirements.txt') as f:
#     dependencies = f.read().splitlines()

# # Process each dependency in turn
# for dependency in dependencies:
# 	try:
# 		pkg_resources.require(dependency)
# 	except:		
# 		print('Missing: ' + dependency)




# here, if a dependency is not met, a DistributionNotFound or VersionConflict
# exception is thrown. 
#pkg_resources.require(dependencies)



# pip install --target=. Alfred-Workflow==1.27
# $ pip install --target=lib -r requirements.txt


# Alfred-Workflow==1.27
# unicodecsv==0.14.1
# dotmap==1.2.17
# pycountry==17.5.14
# Unidecode==0.4.21

#import subprocess

#def install(name):
#    subprocess.call(['pip', 'install', name])


# Works
# print('pip install --target=./lib "semantic_version>=0.9"')

# Works
# print('pip install --prefix=$(pwd)/lib "semantic_version>=0.9"')


# import pip

# lib_path = os.getcwd() + '/lib'
# prefix_option = '--prefix=' + lib_path
# pip.main(['install', prefix_option, 'semantic_version'])




class RequirementsInstaller(object):
	"""This class will look for a `requirements.txt` file in the local directory.  If found it will call
	pip internally to try to install (locally) the missing requirements.  This may allow alfred distribution
	to go faster for soem python libs and stuff,  My default it will install stuff in the ./lib directory - but you
	can program things to go elsewhere"""
	def __init__(self, install_dir='./lib'):
		super(RequirementsInstaller, self).__init__()

		self.lib_path =  os.path.abspath(os.getcwd() + '/' + install_dir)
		self.prefix_option = '--prefix=' + self.lib_path
		self.target_option = '--target=' + self.lib_path
		self.create_setup_cfg()

	def create_setup_cfg(self):
		"""When using homebrew and stuff there are issues wiht pip --target installs unless this file exists
		in the home directory of the project"""
		with open('setup.cfg', "w") as w:
			w.write('[install]\nprefix=\n')

	def install_requirements(self):
		"""Will attempt to parse a `requirements.txt` file and check for which dependencies are missing"""
		# Read in requiremetns.txt file
		with open('requirements.txt') as f:
		    dependencies = f.read().splitlines()

		# Process each dependency in turn
		for dependency in dependencies:
			try:
				pkg_resources.require(dependency)
			except:		
				print('Missing: ' + dependency)
				print('\tInstalling to: ' + self.lib_path)
				self.install_requirement(dependency)

	def install_requirement(self, requirement):
		"""Instals a requirement with the self.prefix_option as specified by the class"""
		pip.main(['install', self.target_option, requirement])



#pip.main(['install', '--user', 'zumba'])



# pip install --install-option="--prefix=$PREFIX_PATH" package_name



# try:
#     import zumba
# except ImportError:
#     import pip
#     pip.main(['install', '--user', 'zumba'])
#     import zumba

def main():
    # my code here

    installer = RequirementsInstaller()
    installer.install_requirements()

if __name__ == "__main__":
    main()