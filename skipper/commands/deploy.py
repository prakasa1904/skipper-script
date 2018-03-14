"""The deploy command."""

import os
import tarfile
from json import dumps
from fabric.api import *

from .base import Base
from .config import *


class Deploy(Base):
  """Deploy into env you define for"""
  
  def run(self):
    print('Deploy into ....')
    print('Run docker for sync into s3cmd only') # this the important think is, files inside docker will consistent environment
    print('yarn')
    print('yarn start')
    print('tar.gz requirements files from identifier')
    print('s3cmd <BUILD_PATH> <s3://[LITE_PATH]>')
    print('Trigger Jenkins with identifier')
    print('Jenkins Trigger Ansible')
    print('Server Script Execute....')
    print('Pull files from s3://[LITE_PATH]')
    print('docker-compose -f docker-compose.<IDENTIFIER>.yml build')
    print('docker-compose -f docker-compose.<IDENTIFIER>.yml up')
    print('=============================')
    with lcd(project_path):
      # create path to store temporary files
      requirements_files()
      local('git status')
      #local('yarn && yarn run deploy:staging')

def requirements_files():
  if os.path.isdir(project_path + tmp_requirement) == False:
    local('mkdir requirements')
  for i in range(len(requirement_files)):
    local('cp -rf ' + requirement_files[i] + ' ' + tmp_requirement)
  make_tarfile('deploy_feauture_24', project_path + tmp_requirement)
  
def make_tarfile(output_filename, source_dir):
  destination = project_path + tmp_requirement + output_filename + '.tar.gz'
  with tarfile.open(destination, "w:gz") as tar:
    tar.add(source_dir, arcname=os.path.basename(source_dir))