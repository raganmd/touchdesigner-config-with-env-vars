import Launcher
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
toe_file    = 'env-vars.toe'

launch_args = [
    {
        "envVar"    : "STARTUP",
        "envVal"    : "controller" 
    },
    {
        "envVar"    : "STARTUP",
        "envVal"    : "node" 
    }
]

Launcher.Start_up(current_dir=current_dir, toe_file=toe_file, launch_args=launch_args)