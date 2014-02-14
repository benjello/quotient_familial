# -*- coding: utf-8 -*-

from datetime import datetime

from openfisca_core import model
import openfisca_france
openfisca_france.init_country()
from openfisca_core.simulations import ScenarioSimulation


def case_study (year = 2013) :
#simulation est une classe , Scenariosimulation  est une instance, on a instancier "simulation"
#on a mainteant fait simulation.set_congif pour modifier les attributs. on lui a dit de prendre l'année 2013
#avec year=year. reforme = true. Nmen est le nombre de ménage. Maxrev est le salaire imposable de la première personne déclaré.
# Ici tu prends que deux menage et on fait varier les salaire. Simulation.set.param est la legislation par défaut.

    simulation = ScenarioSimulation()
    simulation.set_config(year = year,
                          nmen = 2,
                          maxrev = 10000,
                          x_axis= 'sali')
    simulation.set_param()
    df = simulation.get_results_dataframe()
    print df.to_string()
    

if __name__ == '__main__':

 case_study()