
A PrimeCuber variant for LEGO Mindstorms 51515

The code is a work by David Gilday (mindcuber.com). This is just a Mindstorms 51515 port.

The build adaptation is done by my son Marin using the Primecuber instructions and only the Mindstorms 51515 parts.

The solver can be seen in action at https://youtu.be/e2EDLIPwlSM 

INSTRUCTIONS

1. Open & run program "PCSolver-v1p 5.lms"

There is 1-2 minutes wait before you can see a dial (sort of) moving on the hub.
The expected output is:

	> SLOT: 0 6008.py 496B
	> SLOT: 1 11624.py 80977B
	> SAVING: /pccolors_vlp4.py
	> SAVING: /pcsolver_vlp4.py
	> SAVING: /primecuber_v1p4.py
	> SAVING: /pcmtab1_y1p4.bin
	> FINISHED

2. Open & run program "PrimeCuber-v1p 5.lms"

This program calls the previously loaded programs and solves the cube.
Before the cube is inserted, the left & right buttons can be used to properly align the cradle.

FILES DESCRIPTION

*** PCSolver-v1p 5.lms

Loader which loads .py files into the Mindstorms hub. The modifications are in the ScanFace function (as the scanning arm design is different) and also at the beginning of the code so the program files are installed every time even if they are present in the hub.

*** PrimeCuber-v1p 5.lms

The project which solves a cube by calling the functions in the .py files loaded by PCSolver-v1p 5.lms.

*** CubeTestScan 1.lms

A quick and dirty program used to determine proper scanning arm positions:

- parking position
- corner squares
- side squares
- the middle square

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
