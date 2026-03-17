from dask.distributed import Client
from dask_kubernetes import KubeCluster

def get_cluster_client():
    """Initializes Dask on Kubernetes for terabyte-scale imagery analysis."""
    cluster = KubeCluster.from_yaml('deploy/k8s/dask-spec.yml')
    cluster.scale(10) # Scalable workers for peak disaster loads
    return Client(cluster)