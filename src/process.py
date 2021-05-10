import argparse
import json
from typing import Dict, Any

from utils import *
from dataset import DatasetManager
from transforms import TransformManager

def process():
    '''
    process

    Wrapper to execute pre-processing pipeline
    Load the configuration file, declare utility objects
    '''
    config = json.load(open("config.json"))

    if not isinstance(config, dict):
        raise TypeError("Expected dict; got %s" % type(params).__name__)
    if not config:
        raise ValueError("Expected %s dict; got empty dict" %
                         os.path.basename(__file__))

    verbose = config["verbose"]
    # Verbose mode
    if verbose:

        def verbosePrint(*args):
            for arg in args:
                print(arg, )
    else:
        verbosePrint = lambda *a: Nones

    
    path_manager = PathManager(config["pathManager"])
    export_path = path_manager.visuals_data_dir()
    
    transforms_manager = TransformManager(config["transformManager"])
    transforms = transforms_manager.transforms()

    # Pre-process dataset
    dataset_manager = DatasetManager(config["datasetManager"], path_manager,
                                     transforms)
    dataset_manager.process_images()


process()