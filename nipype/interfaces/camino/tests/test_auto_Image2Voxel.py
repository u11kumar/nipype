# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.camino.convert import Image2Voxel

def test_Image2Voxel_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='-4dimage %s',
    mandatory=True,
    position=1,
    ),
    out_file=dict(argstr='> %s',
    genfile=True,
    position=-1,
    ),
    out_type=dict(argstr='-outputdatatype %s',
    position=2,
    usedefault=True,
    ),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = Image2Voxel.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_Image2Voxel_outputs():
    output_map = dict(voxel_order=dict(),
    )
    outputs = Image2Voxel.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

