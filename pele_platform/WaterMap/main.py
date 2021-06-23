import os

import pele_platform.Utilities.Helpers.helpers as hp
import pele_platform.Adaptive.simulation as sim
import pele_platform.WaterMap.preparation as prep
import pele_platform.WaterMap.analysis as an


def run_watermap(parsed_yaml):
    """
    Runs the whole water map package and performs analysis.

    Parameters
    ----------
    parsed_yaml : YamlParser
        Arguments from input.yaml.
    Returns
    -------
        Output of the analysis.
    """

    # Remove all waters from the system
    user_radius = parsed_yaml.water_radius if parsed_yaml.water_radius else 6.0

    try:
        water_center = hp.get_coords_from_residue(
            parsed_yaml.system, parsed_yaml.water_center
        )
    except:  # TODO: Fix base exception
        water_center = parsed_yaml.water_center
    parsed_yaml.system = prep.prepare_system(
        parsed_yaml.system, water_center, user_radius
    )
    parsed_yaml.water_center = water_center

    # Launch adaptive simulation
    simulation = sim.run_adaptive(parsed_yaml)

    # Get path to simulation output
    simulation_output = os.path.join(simulation.pele_dir, simulation.output)

    return simulation
    # Analyse
    # analysis = an.main(
    #     simulation.water_center, simulation.water_radius, simulation_output
    # )
    #
    # return analysis