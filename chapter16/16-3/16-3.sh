### 16-3 -- Environmental Variable.
# 
# Create an environmental variable called $python_projects that is an absolute 
# path to the directory where you keep your Python files. Save the variable in 
# your .profile file and then use the command cd $python_projects to navigate 
# there.
#
###



#!/bin/bash

export python_projects=~
cd /
pwd
cd $python_projects
pwd
