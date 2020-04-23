# sdcc_jupyter_spawners

Jupyter spawners for configuration at SDCC

From root directory of this repo (where setup.py is), run pip install -e .

If you don't actually need an editable version, you can simply run:

```
pip install git+https://github.com/jupyterhub/sdcc_jupyter
```

Add lines in jupyterhub_config.py for the spawner you intend to use, e.g.

```
   c.JupyterHub.spawner_class = 'wrapspawner.WrapFormSpawner'
```

Depending on the spawner, additional configuration will likely be needed.
