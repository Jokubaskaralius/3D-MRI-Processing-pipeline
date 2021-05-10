MRI processing pipeline

File list:
process.py - wrapper to execute MRI image processing.
dataset.py - dataset manager, for loading, processing, saving the MRI images on the filesystem
transforms.py - pre-processing transforms to apply to a MRI image
utils.py - project utilities (i.e., project path manager to manage project paths, etc.)
visual.py - 2D and 3D visualization of MRI brain
config.json - configuration file to select transforms

To run the processing pipeline:

1. The project folder structure should be maintained
   Project/
   |-- data/
   | |-- _data files_
   |
   |-- env/
   | |-- _environment files_
   |
   |-- src/
   | |-- _data files_
   | | |-- dataset.py
   | | |-- process.py
   | | |-- transforms.py
   | | |-- utils.py
   | | |-- visual.py
   | |  
   |
   |-- config.json
   |-- requirements.txt
   |-- README

2. Activate your python virtualenv
   Refer to creating a virtualenv and activating one
   https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/
   This step may be skipped if this project and dependencies are to be installed globally,
   however virtualenv is highly recommended.

3. Install the project dependencies
   Execute command:
   pip install -r requirements.txt

4. Run the process.py wrapper
   Execute command:
   python3 src/process.py
