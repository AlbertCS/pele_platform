============================
For saturated mutagenesis
============================

Introduction
---------------

This python package is wrappped around the pmx package that performs saturated mutations on proteins to study
their effects on protein-ligand interactions via PELE simulations.

Inputs
++++++++
    - protein-ligand PDB file(s)
    - YAML file with parameters
    - txt file for the output status

Default parameters
+++++++++++++++++++++

    None


1. Complex Preparation
--------------------------
   
...

Make sure the ligand has:

 - unique chain ID
 - unique PDB atom names with no spaces or single letters
 - any residue name except for ``UNK``

2. Input Preparation
----------------------

Prepare the input file ``input.yml``:

..  code-block:: yaml

    saturated_mutagenesis: true # To activate saturated_mutagenesis
    system: '../pele_platform/Examples/enzyme_engineering/pdb_files/*.pdb' # Pdb file to mutate
    chain: 'L' # Ligand chain ID
    resname: 'SUB' # Ligand residue name
    seed: 12345
    steps: 1
    cpus_per_mutations: 1 # Number of cpus for mutation
    # Distance between two atoms to track the simulation
    atom_dist:
      - "C:1:C19" # First atom (chain ID:residue number:atom name)
      - "L:1:C8" # Second atom
    cpus: 4 # Number of cpus
    templates:
      - path/ndpz
    skip_ligand_prep:
      - 'NDP'
    satumut_catalytic_distance: 10
    satumut_positions_mutations:
      - A:297
    satumut_mutation:
      - SER
      - ALA
      - VAL


For more optional flags please refer to `optional flags <../../input/yaml.html>`_.

3. Run simulation
----------------------

To run the system launch the simulation with the following command:

``python -m pele_platform.main input.yml``

4. Output
----------------

Raw output
+++++++++++++
The plots, report files and pdb files for each simulation are located in ``working_folder/Resname_Pele_mut``. That's where you can find
detailed information on each snapshot (PDB file, binding energy, metrics, etc.).

Results
++++++++++++++++

Plots
**********

Plots of the Binding Energy vs distance to study.
Plots files:

``working_folder/Resname_Pele_mut/analysis_results/Plots``

Pdb files
***************

The pdb files with the mutation and the original. They are stored in:

``working_folder/Resname_Pele_mut/pdb_files``
