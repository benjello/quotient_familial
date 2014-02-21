# -*- coding: utf-8 -*-

from datetime import datetime

from openfisca_core import model
import openfisca_france
openfisca_france.init_country()
from openfisca_core.simulations import ScenarioSimulation


def case_study(year = 2013) :
#simulation est une classe , Scenariosimulation  est une instance, on a instancier "simulation"
#on a mainteant fait simulation.set_congif pour modifier les attributs. on lui a dit de prendre l'année 2013
#avec year=year. reforme = true. Nmen est le nombre de ménage. Maxrev est le salaire imposable de la première personne déclaré.
# Ici tu prends que deux menage et on fait varier les salaire. Simulation.set.param est la legislation par défaut.

    simulation = ScenarioSimulation()
    simulation.set_config(year = year,
                          nmen = 2,
                          maxrev = 500000,
                          x_axis= 'sali')
    simulation.set_param()
    df = simulation.get_results_dataframe()
    print df.to_string()
    
    

def couple_38ans_avec_3enfants(year = 2013):
    simulation = ScenarioSimulation()
    simulation.set_config(year=year,
					nmen=1,
					maxrev = 500000,
                          x_axis= 'sali',
                          )
    print simulation.scenario
    simulation.scenario.addIndiv(1, datetime(1975,1,1).date(), 'conj', 'part')
    simulation.scenario.addIndiv(2, datetime(2000,1,1).date(), 'pac1', 'enf1')
    simulation.scenario.addIndiv(3, datetime(2005,1,1).date(), 'pac2', 'enf2')
    simulation.scenario.addIndiv(4, datetime(2010,1,1).date(), 'pac3', 'enf3')

if __name__ == '__main__':
    case_study()
    couple_38ans_avec_3enfants()
