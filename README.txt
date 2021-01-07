
A PrimeCuber variant for LEGO Mindstorms 51515

The code is work by David Gilday (mindcuber.com). This is just a Mindstorm port.

The LEGO design is done by my son Marin using the Primecuber instructions and only the Mindstorms 51515 parts.

The solver can be seen in action at https://youtu.be/e2EDLIPwlSM 

FILES DESCRIPTION

*** PCSolver-v1p 5.lms

Loader which loads .py files into the Mindstorms hub. The modifications are in the ScanFace function (as the scanning arm design is different) and also at the beginning of the code so the program files are installed every time even if they are present in the hub.

*** PrimeCuber-v1p 5.lms

The project which solves a cube by calling the functions in the .py files loaded by PCSolver-v1p 5.lms.

*** CubeTestScan 1.lms

A quick and dirty program used to determine proper scanning arm positions:

- parking position
- scanning corner squares
- scanning side squares
- scanning the middle square

Enjoy!

Mladen
