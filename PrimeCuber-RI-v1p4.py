#-----------------------------------------------------------------------------
# Title:        PrimeCuber
#
# Author:    David Gilday
#
# Copyright:    (C) 2020 David Gilday
#
# Website:    http://mindcuber.com
#
# Version:    v1p4
#
# Modified:    $Date: 2020-12-04 18:02:42 +0000 (Fri, 04 Dec 2020) $
#
# Revision:    $Revision: 7784 $
#
# Usage:
#
#This software may be used for any non-commercial purpose providing
#that the original author is acknowledged.
#
# Disclaimer:
#
#This software is provided 'as is' without warranty of any kind, either
#express or implied, including, but not limited to, the implied warranties
#of fitness for a purpose, or the warranty of non-infringement.
#
#-----------------------------------------------------------------------------
# Purpose:    PrimeCuber robot Rubik's Cube solver
#-----------------------------------------------------------------------------
# Note:
#The program, PCSolver-v1p4, must be run once to install the two
#modules and data file used by this program. This basic solver will
#allow the cube to be solved in around 3.5 minutes.
#
#Optionally, the program, PCMTab4-v1p4, may be run once to install a
#large data file that enables shorter solutions to be calculated. In
#this case, the cube will be solved in around 2 minutes.
#-----------------------------------------------------------------------------

import hub, os
hub.display.show(hub.Image.DIAMOND)

try:
    installed = os.stat("/pcsolver_v1p4.py")[6] > 21000
except:
    installed = False

if not installed:
    from spike import LightMatrix
    LightMatrix().write("Check PCSolver-v1p4 has been run")

import pcsolver_v1p4
import pccolors_v1p4
import primecuber_v1p4

pcsolver_v1p4.init(pccolors_v1p4)
print("pccolors.init done")
primecuber_v1p4.main()

hub.display.show(hub.Image.YES)

raise SystemExit

# END
