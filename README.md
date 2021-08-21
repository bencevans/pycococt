# pycococt

> [COCO-CameraTrap](https://github.com/microsoft/CameraTraps/blob/9384e69564a0c425b9ecdef3b050ab75a14e4413/data_management/README.md) Indexer. An extension to pycocotools including location and sequence indexing.

## Features

- Extends / Backwards compatable with [pycocotools](https://github.com/cocodataset/cocoapi/tree/master/PythonAPI/pycocotools)
- Indexing for Locations and Sequences

## Install

```sh
pip install pycococt
```

## Usage

```python
from pycococt.cococt import COCOCT

ds = COCOCT('path to COCO-CameraTrap')

# all the core indexes and helpers in pycocotools
ds.imgs
ds.anns
ds.cats
ds.catToImgs
ds.imgToAnns

# with aditional camera trap indexes
ds.locs      # = [
             #   'Location1',
             #   'Location2',
             #   'Location3',
             #   ...
             # ]

ds.locToImgs # = { 'Location1': {
             #        'imageid': {
             #           'id': 'imageid',
             #           'location': 'Location1',
             #           'height': ...
             #         }
             #      },
             #      ...
             #    }

ds.locToSeqs # = {
             #     'Location1': [
             #         'seq id 1_1',
             #         'seq id 1_2',
             #         ...
             #     ],
             #     'Location2': [
             #         'seq id 2_1',
             #         'seq id 2_2',
             #         ...
             #     ]
             #     ...
             # }

ds.seqToImgs # = { 'sequence 1 id': [
             #       {
             #           'id': 'image id',
             #           ...
             #        },
             #        {
             #           'id': 'image id',
             #           ...
             #        },
             #        ...
             #     ],
             #     'sequence 2 id: [
             #       ...
             #     ]
             #       ...
             #    }
```
