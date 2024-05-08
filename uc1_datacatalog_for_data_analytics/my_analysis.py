# Setup the configloader

import os

from kedro.config import OmegaConfigLoader
from kedro.io import DataCatalog

# in real life we have customer reslovers at my company and hereafter is just an exemple, even if specifically for env var there exist a built in one
conf_loader = OmegaConfigLoader(
    ".",
    base_env="",
    default_run_env="",
    custom_resolvers={"oc.env": lambda x: os.environ.get(x)},
)
# Read the configuration file
conf_params = conf_loader["parameters"]
conf_catalog = conf_loader["catalog"]

# Create the DataCatalog instance from the configuration
catalog = DataCatalog.from_config(conf_catalog)


# ANALYSIS

print(catalog)  # not understandable
catalog.list()
catalog.load("companies")
