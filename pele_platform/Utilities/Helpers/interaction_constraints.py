from dataclasses import dataclass

metric_template = """
                     {                                                                                                                                                                  
                     "type":"com_distance",                                                                                                                                             
                     "tag":"distance{tag_num}",                                                                                                                                               
                     "selection_group_1":{                                                                                                                                              
                     "atoms": { "ids":["{atom1}"]}                                                                                                                                  
                     },                                                                                                                                                                 
                     "selection_group_2":{                                                                                                                                              
                     "atoms": { "ids":["{atom2}"]}                                                                                                                                    
                     }                                                                                                                                                                  
                     },
"""


@dataclass
class InteractionConstraints:

    input_pdb: str
    constrain_interaction: list

    def run(self):
        self._parse_constraints()

    def _parse_constraints(self):
        
        self.constraints = []

        for c in self.constrain_interaction:
            atom1, atom2 = [element.strip() for element in c.split("-")]
            self.constraints.append(SingleConstraint(atom1, atom2))

    def _create_tags(self):
        pass


@dataclass
class SingleConstraint:

    atom1: str
    atom2: str

    def _build_tag(self):
        pass
