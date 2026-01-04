import sys, os

# Add the project directory to the sys.path
# 'getcwd' is the directory containing this script
sys.path.append(os.getcwd())

from app import app as application
