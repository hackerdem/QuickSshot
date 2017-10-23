from pkg_resources import WorkingSet,DistributionNotFound
from setuptools.command.easy_install import main as installer
import platform
import subprocess

workingSet=WorkingSet()
dependencies={
    'pynput':'1.0.6',
    'pyscreeze':'0.1.11',
    'playsound':'1.2.1'
}

try:
   for key,value in dependencies.items():
            dep=workingSet.require('{}>={}'.format(key,value))
except:
   try:
      if platform.system()=='Windows':
         installer(['{}>={}'.format(key,value)])
      elif platform.system()=='Linux':
         installer(['{}>={}'.format(key,value)]) # convert this to pip later
      print('{} {} has been installed successfully'.format(key,value))
   except:
      print('Dependecy installation error when installing {}>={}'.format(key,value))
      pass
   pass
