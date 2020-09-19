import labscript_devices

labscript_device_name = 'NarwhalPulseGen'
blacs_tab = 'labscript_devices.NarwhalPulseGen.blacs_tabs.NarwhalPulseGenTab'
parser = 'labscript_devices.NarwhalPulseGen.runviewer_parsers.NarwhalPulseGenParser'

labscript_devices.register_classes(
    labscript_device_name=labscript_device_name,
    BLACS_tab=blacs_tab,
    runviewer_parser=parser,
)
