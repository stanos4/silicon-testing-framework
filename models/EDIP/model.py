# parameters from LAMMPS distribution

import os
import sys

try:
    from lammpslib import LAMMPSlib
except:
    sys.exit("Failed to import lammpslib module")

model_dir = os.path.dirname(__file__)

header=['units metal',
        'atom_modify map array sort 0 0']

cmds = ["pair_style edip",
        "pair_coeff * * {}/Si.edip Si".format(model_dir)]

try:
    calculator = LAMMPSlib(lmpcmds = cmds,keep_alive=True,lammps_header=header,atom_types={"Si":1}, lammps_name=os.environ['LAMMPS_NAME'])
except:
    raise RuntimeError

no_checkpoint = True

name = 'EDIP'
