import json
import pandas as pd

from typing import Union
from importlib import resources
from glmpy.sim import Sim, GLMSim, BcsDict
from glmpy.nml import glm_nml as gnml
from glmpy.nml.nml import NMLDict


class SparklingSim(GLMSim):
    def __init__(
        self,
        sim_name: Union[str, None] = "sparkling",
        outputs_dir: str = "."
    ):
        sim_pickle = resources.files(
            "glmpy.data.example_sims"
        ).joinpath("sparkling_sim.glmpy")
        sparkling_sim = GLMSim.from_file(str(sim_pickle))
        self.bcs = sparkling_sim.bcs
        self.nml = sparkling_sim.nml
        self.outputs_dir = outputs_dir
        self._init_sim_name(sim_name, sparkling_sim.nml["glm"])
        