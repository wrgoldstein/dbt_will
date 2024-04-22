from dbt.contracts.graph.node_args import ModelNodeArgs
from dbt.plugins.manager import dbt_hook, dbtPlugin
from dbt.plugins.manifest import PluginNodes


class dbtWill(dbtPlugin):
    """
    dbtWill is a dbt plugin that loads manifest files, parses a DAG from the manifest,
    and injects Will nodes into it.
    """

    def __init__(self, project_name: str):
        self.config = {}
        self.models = {}
        super().__init__(project_name)


    def initialize(self) -> None:
        # (called by the plugin manager)

        # inject an example node. you can walk the local filesystem
        # here instead and look for specific things.
        
        unique_id = "model.will.thing"  # type.project.name typically
        node_args = ModelNodeArgs(
            name = "will",
            package_name ="dbt_will",
            identifier ="my_will_table",
            schema ="public",
            relation_name ="relation_name",
            depends_on_nodes =[]
        )

        self.models.update({unique_id: node_args})


    @dbt_hook
    def get_nodes(self) -> PluginNodes:
        # (called during compilation)
        return PluginNodes(models=self.models)

plugins = [dbtWill]
