Plurizymer parameters
------------------------

These are parameters that affect plurizymer. Thus, they affect the way
how the phase space of the system is explored.

List of adaptive plurizymer:

    1. `plurizymer_single_mutation <#iterations>`__
    2. `plurizymer_turn <#spawning>`__
    3. `plurizymer_atom <#adaptive-restart>`__
    4. `plurizymer <#plurizymer>`__

List of examples:

    - `Example 1 <#example-1>`__


plurizymer_single_mutation
+++++++++++++++++++++++++++

    - Description: Name of the residue to mutate to (both 1 and 3 letter codes can be used).

    - Type: ``string``
    - Default: "Required"

plurizymer_turn
+++++++++++++++++++++++++++

    - Description: The number of the round of plurizyme generation, not needed for the first round.

    - Type: ``string``
    - Default: null

plurizymer_atom
+++++++++++++++++++++++++++

    - Description: Atom to use in the search for neighbouring residues in the format chain:resnum:atom_name.

    - Type: ``string``
    - Default: "Required"

plurizymer
+++++++++++++++++++++++++++

    - Description: Set true to activate the plurizymer.

    - Type: ``boolean``
    - Default: none


Example 1
+++++++++

..  code-block:: yaml

    # Required parameters
    system: 'system.pdb'
    chain: 'L'
    resname: 'GTP'

    # General parameters
    cpus: 4
    seed: 2021

    # Package selection
    plurizymer: true

    # Adaptive parameters
    iterations: 1
    plurizymer_single_mutation: SER
    plurizymer_atom: L:GTP:C4
    satumut_hydrogens: True
