============================
For plurizymer
============================

Introduction
---------------

This python package is wrapped around the pmx package that performs saturated mutations
in the active site of the enzyme

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

Make sure the ligand has:

 - unique chain ID
 - unique PDB atom names with no spaces or single letters
 - any residue name except for ``UNK``
 - correct template

2. Input Preparation
----------------------

Prepare the input file ``input.yml``:

..  code-block:: yaml

    plurizymer: true # To activate plurizymer
    system: '../pele_platform/Examples/enzyme_engineering/pdb_files/*.pdb' # Pdb file to mutate
    chain: 'L' # Ligand chain ID
    resname: 'GTP' # Ligand residue name
    seed: 12345
    steps: 1
    iterations: 1
    cpus_per_mutations: 1 # Number of cpus for mutation
    cpus: 4 # Number of cpus
    satumut_hidrogens: True
    plurizymer_atom:
      - L:GTP:C4
    plurizymer_single_mutation: SER


For more optional flags please refer to `optional flags <../../input/yaml.html>`_.

3. Run simulation
----------------------

To run the system launch the simulation with the following command:

``python -m pele_platform.main input.yml``

4. Output
----------------

Raw output
+++++++++++++
The report files and pdb files for each simulation are located in ``working_folder/Resname_Pele_mut``. That's where you can find
detailed information on each snapshot (PDB file, binding energy, metrics, etc.).

Results
++++++++++++++++

Pdb files
***************

The pdb files with the mutation and the original. They are stored in:

``working_folder/Resname_Pele_mut/pdb_files``
