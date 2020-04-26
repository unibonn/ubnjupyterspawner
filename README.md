# NDJupyterSpawner

ND Jupyter spawner

```
pip install git+https://github.com/NDCMS/ndjupyterspawner
```

Add lines in jupyterhub_config.py for the spawner, i.e.:

```
   c.JupyterHub.spawner_class = 'wrapspawner.NDSpawner'
```
