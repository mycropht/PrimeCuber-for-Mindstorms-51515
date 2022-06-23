
A PrimeCuber variant for LEGO Mindstorms 51515

The code is a work by David Gilday (mindcuber.com). This is just a Mindstorms 51515 port.

The build adaptation is done by my son Marin using the Primecuber instructions and only the Mindstorms 51515 parts.

Orione (http://www.orione-alnitak.eu/responsive) liked the design so much that he (she? they?) made the instructions:

https://drive.google.com/file/d/1bPBpQtQXGo1PtdjhdGkOFznhE9t5BwvA/view

Thanks Orione!

The solver can be seen in action at https://youtu.be/e2EDLIPwlSM 

NOTE:

The original method used to load the program into Mindstorms hub does not work with latest firmware.
This is a new method taken from MindCuber-RI. The whole thing is written by David Gilday anyway and all the credit goes to him.

I love this PrimeCuber adaptation as it was done by my 10-year-old son Marin, but the MindCuber-RI is among my favourite LEGO buids ever, together with Lego Technic 42006 Excavator and LEGO Technic Backhoe Loader 8069 (for sentimental reasons). :) 

INSTRUCTIONS

1. Open & run program "PCRISolver-v1p4.lms" in an unused slot (eg. 18)

After a minute, an error message will appear:

SyntaxError: invalid syntax

This is expected!

2. Open & run program "PCRIInstall-v1p4.lms" in ANOTHER unused slot (eg. 19)

There is 1-2 minutes wait before you can see a dial (sort of) moving on the hub.
The expected output is:

	> SLOT: 18 /projects/420/__init__.py 71645B
	> Installing...
	> SAVING: /pccolors_vlp4.py 7706B
	> SAVING: /pcsolver_vlp4.py 22189B
	> SAVING: /primecuber_v1p4.py 14121B
	> SAVING: /pcmtab1_v1p4.bin 18985B
	> FINISHED PrimeCuber-RI v1p4 installed
	
After this point, you can delete the programs in slots 18 & 19
	
3. Open & run program "PrimeCuber-RI-v1p4.lms"

This program calls the previously loaded programs and solves the cube.
Before the cube is inserted, the left & right buttons can be used to properly align the cradle.

FILES DESCRIPTION

*** PCRISolver-v1p4.lms

File with expected and intentional syntax error. Contains text of the programs that will be loaded into the hub by the next program.

*** PCRIInstall-v1p4.lms

Loader which loads .py files into the Mindstorms hub. Compared to the original PrimeCuber, the modifications are in the ScanFace function (as the scanning arm design is different) and also at the beginning of the code so the program files are installed every time even if they are present in the hub.

*** PrimeCuber-RI-v1p4.lms

The project which solves a cube by calling the functions in the .py files loaded by PCRIInstall-v1p4.lms.
After the first start, connection to a PC is not needed any more.

*** CubeTestScan 1.lms

A quick and dirty program used to determine proper scanning arm positions:

- parking position
- corner squares
- side squares
- the middle square

*** PrimeCuber-RI-Clean-Up.lms

A small program which removes PrimeCuber-RI files from the hub.

*** MindCuber-RI-Clean-Up.lms

A small program which removes MindCuber-RI files from the hub.

-------------------------------------------------------------------------------------

Compared to the original David Gilday's code (please check at mindcuber.com), the only changes are in the "PCSolver-v1p4" module.

Here is the changed part (in the ScanFace function):

####            # MD: middle: was +485
####            self.run_to(self.motor_scan, self.motor_scan_base+195, 100)
####            self.ScanRGB(f, 8)
####            self.motor_tilt.brake()
####            if self.slower:
####                self.slower = False
####                self.scan_speed -= 1
####                # MD: decommented:
####                print("Scan speed "+str(self.scan_speed))
####            self.run_nw(self.motor_turn, self.motor_turn_base+self.turn_ratio*360, self.scan_speed)
####            for i in range(4):
####                # MD: corner: was 300
####                self.ScanPiece(145, f, o, i)
####                # MD: side: was 365
####                self.ScanPiece(165, f, o+1, i+4)


Also, in the video, the motors and sensors are connected into different ports. No need for this change if the original PrimeCuber instructions are followed.:


####class primecuber():
...
####            self.sensor_color = self.check_port(hub.port.B, False, [61],    4, 0)
####            self.sensor_dist= self.check_port(hub.port.C, False, [62],    0, 2)
####            self.motor_scan= self.check_port(hub.port.D, True,[48, 75], 4, 2)
####            self.motor_turn= self.check_port(hub.port.F, True,[48, 75], 4, 4)
####            self.motor_tilt= self.check_port(hub.port.E, True,[48, 75], 0, 4)



After the solving program is started, a pixel will be lighted near by the offending port if the expected motor/sensor is not found.


Finally, at the beginning of the same module (at the line 54), the following code was inserted so the program would be reinstalled in the hub even if it already exists:

# MD: force reinstallation
installed = False



Enjoy!

Mladen
