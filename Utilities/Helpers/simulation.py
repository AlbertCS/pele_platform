import os
from MSM_PELE.Utilities.Helpers import helpers, template_builder
import MSM_PELE.Utilities.AdaptivePELE.adaptiveSampling as ad
import MSM_PELE.constants as cs
import MSM_PELE.Utilities.Helpers.center_of_mass as cm 

class SimulationBuilder(template_builder.TemplateBuilder):

    def __init__(self, file, topology, keywords, *args, **kwargs):

        self.file = file
        self.topology = topology
        self.keywords = keywords

        self.ad_opt_new = ["false" if opt is False else opt for opt in locals()["args"]]
        self.ad_opt = ["true" if opt is True else opt for opt in self.ad_opt_new]


        self.replace = {keyword : value for keyword, value in zip(self.keywords, self.ad_opt)}

        super(SimulationBuilder, self).__init__(self.file, self.replace)

    @classmethod
    def simulation_handler(cls, env, protein_constraints):
        if not env.hbond:
            cls(env.pele_exit_temp,  env.topology, cs.EX_PELE_KEYWORDS,
                    env.native, env.forcefield, env.chain, "\n".join(protein_constraints), env.cpus, env.license)
            cls(env.pele_temp,  env.topology, cs.EX_PELE_KEYWORDS,
                    env.native, env.forcefield, env.chain, "\n".join(protein_constraints), env.cpus, env.license)
        elif env.hbond:
            cls(env.pele_exit_temp,  env.topology, cs.PELE_GLIDE_KEYWORDS,  cs.LICENSE,
                    "\n".join(protein_constraints), cm.center_of_mass(env.ligand_ref), env.chain, env.native,
                    * env.hbond)
        

    def run(self, hook=False):
        with helpers.cd(os.path.dirname(self.file)):
            if hook:
				ad.main(self.file, clusteringHook=self.interactive_clustering)
            else:
				ad.main(self.file)

    def interactive_clustering(self, cluster_object, paths, simulationRunner, epoch_number):
        initial_rmsd_cluster_values = cluster_object.thresholdCalculator.values
        while len(cluster_object.clusters.clusters) == 1:
            current_values = cluster_object.thresholdCalculator.values
            cluster_object.thresholdCalculator.values = [ value-0.5 if value > 0.5 else value for value in current_values]
            if cluster_object.thresholdCalculator.values == current_values: break
            cluster_object.emptyClustering()
            ad.clusterPreviousEpochs(cluster_object, epoch_number, paths.epochOutputPathTempletized, simulationRunner, self.topology)
            print("Lowering cluster RMSD to: {}".format(cluster_object.thresholdCalculator.values))
        cluster_object.thresholdCalculator.values = initial_rmsd_cluster_values
        print("Interactive clustering ended restoring initial value {}".format(cluster_object.thresholdCalculator.values))

