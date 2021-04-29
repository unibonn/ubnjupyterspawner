# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

version_info = (
    2021,
    4,
    30,
    2
)
__version__ = '.'.join(map(str, version_info[:4]))

if len(version_info) > 4:
    __version__ = '%s-%s' % (__version__, version_info[4])
