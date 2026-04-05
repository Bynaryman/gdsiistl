"""IHP SG13G2 (BiCMOS) layer mapping for gdsiistl.

This script can be passed to gdsiistl.py with:
    python gdsiistl.py --pdk-script example/ihp_bicmos_sg13g2.py <file.gds>
"""

# (layer, datatype) -> canonical layer name used for STL output
LAYER_DEFINITIONS = {
    (40, 0): 'substrate',
    (31, 0): 'nwell',
    (1, 0): 'activ',
    (7, 0): 'nsd',
    (14, 0): 'psd',
    (5, 0): 'poly',
    (6, 0): 'cont',
    (8, 0): 'metal1',
    (19, 0): 'via1',
    (10, 0): 'metal2',
    (29, 0): 'via2',
    (30, 0): 'metal3',
    (49, 0): 'via3',
    (50, 0): 'metal4',
    (66, 0): 'via4',
    (67, 0): 'metal5',
    (125, 0): 'topvia1',
    (126, 0): 'topmetal1',
    (133, 0): 'topvia2',
    (134, 0): 'topmetal2',
    (9, 0): 'passiv',
}

# Simple ordered z stack for visualization.
HEIGHT_SCHEMES = {
    'flat': {
        'substrate': (-0.5, 0.0),
        'nwell': (0.0, 0.15),
        'activ': (0.0, 0.18),
        'nsd': (0.0, 0.18),
        'psd': (0.0, 0.18),
        'poly': (0.18, 0.32),
        'cont': (0.32, 0.42),
        'metal1': (0.42, 0.55),
        'via1': (0.55, 0.65),
        'metal2': (0.65, 0.78),
        'via2': (0.78, 0.88),
        'metal3': (0.88, 1.01),
        'via3': (1.01, 1.11),
        'metal4': (1.11, 1.24),
        'via4': (1.24, 1.34),
        'metal5': (1.34, 1.47),
        'topvia1': (1.47, 1.58),
        'topmetal1': (1.58, 1.78),
        'topvia2': (1.78, 1.89),
        'topmetal2': (1.89, 2.14),
        'passiv': (2.14, 2.22),
    }
}

DEFAULT_HEIGHT_SCHEME = 'flat'
