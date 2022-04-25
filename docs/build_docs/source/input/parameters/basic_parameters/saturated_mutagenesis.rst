Saturated mutagenesis parameters
--------------------------------

These are parameters that affect saturated mutagenesis. Thus, they affect the way
how the phase space of the system is explored.

List of adaptive PELE parameters:

    1. `satumut_positions_mutations <#satumut_positions_mutations>`__
    2. `satumut_mutation <#satumut_mutation>`__
    3. `satumut_multiple_mutations <#satumut_multiple_mutations>`__
    4. `satumut_enantiomer_improve <#satumut_enantiomer_improve>`__
    5. `satumut_energy_threshold <#satumut_energy_threshold>`__
    6. `satumut_dihedrals_analysis <#satumut_dihedrals_analysis>`__
    7. `satumut_conservative <#satumut_conservative>`__
    8. `satumut_catalytic_distance <#satumut_catalytic_distance>`__
    9. `satumut_plots_path <#satumut_plots_path>`__
    10. `satumut_profile_metric <#satumut_profile_metric>`__
    11. `satumut_plots_dpi <#satumut_plots_dpi>`__
    12. `satumut_fixed_residues <#satumut_fixed_residues>`__
    13. `satumut_radius_neighbors <#satumut_radius_neighbors>`__
    14. `satumut_consecutive <#satumut_consecutive>`__
    15. `satumut_hydrogens <#satumut_hydrogens>`__
    16. `satumut_pdb_dir <#satumut_pdb_dir>`__
    17. `satumut_wild <#satumut_wild>`__
    18. `saturated_mutagenesis <#saturated_mutagenesis>`__

List of examples:

    - `Example 1 <#example-1>`__


satumut_positions_mutations
++++++++++

    - Description: Residues to mutate, in the format chain:resnum (if not specified neighbouring residues around the mutation atom will be selected).

    - Type: ``array``
    - Default: none

satumut_mutation
++++++++

    - Description: Residues to mutate to mutate to (using the 3 letter code).

    - Type: ``array``
    - Default: none

satumut_multiple_mutations
++++++++

    - Description: Whether to mutate two residues in the same pdb.

    - Type: ``boolean``
    - Default: false

satumut_enantiomer_improve
++++++++

    - Description: The enantiomer that should improve (R or S).

    - Type: ``string``
    - Default: "R"

satumut_energy_threshold
++++++++

    - Description: An energy threshold that limits the points of scatter plots.

    - Type: ``integer``
    - Default: 20

satumut_dihedrals_analysis
++++++++

    - Description: The four atoms necessary to calculate the dihedrals in format chain:resnum:atom_name.

    - Type: ``array``
    - Default: none

satumut_conservative
++++++++

    - Description: How conservative the mutations sould be, options are 1 or 2.

    - Type: ``integer``
    - Default: null

satumut_catalytic_distance
++++++++

    - Description: The distance considered to be catalytic.

    - Type: ``number``
    - Default: 3.5

satumut_plots_path
++++++++

    - Description: Path of the folder to where to store the plots.

    - Type: ``string``
    - Default: null

satumut_profile_metric
++++++++

    - Description: The metric to generate the pele profiles with (options are Binding energy or currentEnergy).

    - Type: ``string``
    - Default: "Binding Energy"

satumut_plots_dpi
++++++++

    - Description: The dpi value to use for the plots.

    - Type: ``integer``
    - Default: 800

satumut_fixed_residues
++++++++

    - Description: List of residues that you don't want to have mutated (Must write the list of residue numbers).

    - Type: ``array``
    - Default: none

satumut_radius_neighbors
++++++++

    - Description: Radius around the plurizymer_atom to search for residues to mutate.

    - Type: ``number``
    - Default: 5.0

satumut_consecutive
++++++++

    - Description: "Whether to consecutively mutate the PDB file for several round.

    - Type: ``boolean``
    - Default: false

satumut_hydrogens
++++++++

    - Description: Whether to remove the pdb hydrogen atoms (generally should be avoided).

    - Type: ``boolean``
    - Default: true

satumut_pdb_dir
++++++++

    - Description: The name for the mutated pdb folder.

    - Type: ``string``
    - Default: "pdb_files"

satumut_wild
++++++++

    - Description: The pdb file with the wild type

    - Type: ``string``
    - Default: none

saturated_mutagenesis
++++++++++

    - Description: Set true to activate the saturated mutagenesis.

    - Type: ``boolean``
    - Default: none



Example 1
+++++++++


..  code-block:: yaml

    # Required parameters
    system: 'system.pdb'
    chain: 'L'
    resname: 'SUB'

    # General parameters
    cpus: 4
    seed: 2021
    steps: 1
    traj: trajectory.xtc
    templates:
      - /home/albert/Documents/WP2/pele_module/biobb_pele-master/bin/test/data/pele/ndpz
    skip_ligand_prep:
      - 'NDP'

    # Package selection
    saturated_mutagenesis: true

    # Saturated_mutagenesis parameters
    satumut_positions_mutations: ['A:297']
    atom_dist:
      - 'C:1:C19'
      - 'L:1:C8'
    satumut_mutation: ['ALA', 'VAL']


