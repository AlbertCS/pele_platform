import os
import pele_platform.constants.constants as cs
import pele_platform.Adaptive.interaction_restrictions as ir
import pele_platform.Utilities.Helpers.yaml_parser as yp
import pele_platform.Checker.valid_flags as vf
import pele_platform.main as main

test_path = os.path.join(cs.DIR, "Examples")

ARGS_1 = os.path.join(test_path, "interaction_restrictions/input.yaml")
PDB_FILE = os.path.join(test_path, "interaction_restrictions/complex.pdb")

EXPECTED_METRICS = os.path.join(test_path, "interaction_restrictions/out/expected_metrics.txt")
EXPECTED_CONDITIONS = os.path.join(test_path, "interaction_restrictions/out/expected_conditions.txt")

INTERACTION_RESTRICTIONS_PELE = [
    '"interactionRestrictions":',
	'"distance0 < 3"',
	'"angle1 > 90"',
	'"angle1 < 180"'
    ]

METRIC_DISTANCE_PELE = [
    '"type":"com_distance"',
    '"tag":"distance0"',
    '"selection_group_1":{',
    '"atoms": { "ids":["A:318:_OG1"]}',
    '"selection_group_2":{',
    '"atoms": { "ids":["Z:201:_O3_"]}'
]

METRIC_ANGLE_PELE = [
    '"type":"atomsAngle"',
    '"tag":"angle1"',
    '"selection_group_1":{',
    '"atoms": { "ids":["A:318:_OG1"]}',
    '"selection_group_2":{',
    '"atoms": { "ids":["A:318:_HG1"]}',
    '"selection_group_3":{',
    '"atoms": { "ids":["Z:201:_O3_"]}',
]


def test_interaction_restrictions (ext_args=ARGS_1):
    errors = []
    job = main.run_platform(ext_args)
    errors = check_file(job.pele_dir, "pele.conf", INTERACTION_RESTRICTIONS_PELE, errors)
    errors = check_file(job.pele_dir, "pele.conf", METRIC_DISTANCE_PELE, errors)
    errors = check_file(job.pele_dir, "pele.conf", METRIC_ANGLE_PELE, errors)
    assert not errors


def test_metrics_to_json ():
    # Parse yaml file
    yaml_obj = yp.YamlParser(ARGS_1, vf.VALID_FLAGS_PLATFORM)
    yaml_obj.read()
    # Build interaction restrictions
    interaction_restrictions = ir.InteractionRestrictionsBuilder()
    interaction_restrictions.parse_interaction_restrictions(PDB_FILE, yaml_obj.interaction_restrictions)
    # Check metrics json output
    expected_output = open (EXPECTED_METRICS, "r")
    assert interaction_restrictions.metrics_to_json() == expected_output.read()


def test_conditions_to_json ():
    # Parse yaml file
    yaml_obj = yp.YamlParser(ARGS_1, vf.VALID_FLAGS_PLATFORM)
    yaml_obj.read()
    # Build interaction restrictions
    interaction_restrictions = ir.InteractionRestrictionsBuilder()
    interaction_restrictions.parse_interaction_restrictions(PDB_FILE, yaml_obj.interaction_restrictions)
    # Check metrics json output
    expected_output = open (EXPECTED_CONDITIONS, "r")
    assert interaction_restrictions.conditions_to_json() == expected_output.read()


def check_file(folder, filename, values, errors):
   filename = os.path.join(folder, filename)
   with open(filename, "r") as f:
      lines = f.readlines()
      for value in values:
          if value not in "".join(lines):
              errors.append(value) 
   return errors