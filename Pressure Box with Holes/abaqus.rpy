# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2019 replay file
# Internal Version: 2018_09_24-14.41.51 157541
# Run by chs17004 on Thu Oct  8 08:11:34 2020
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=315.656280517578, 
    height=249.75)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
openMdb('Pressure_Box With Holes.cae')
#: The model database "C:\Users\chs17004\Desktop\Abaqus Pressure Vessel\Pressure_Box With Holes.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['Bottom']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/chs17004/Desktop/Abaqus Pressure Vessel/Pressure_Box_With_Holes.odb')
#: Model: C:/Users/chs17004/Desktop/Abaqus Pressure Vessel/Pressure_Box_With_Holes.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     7
#: Number of Meshes:             7
#: Number of Element Sets:       27
#: Number of Node Sets:          29
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/chs17004/Desktop/Abaqus Pressure Vessel/Pressure_Box_With_Holes.odb'])
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.6693, 
    farPlane=2.56979, width=1.05265, height=0.650831, cameraPosition=(1.10017, 
    -0.305067, -2.02394), cameraUpVector=(-0.784843, 0.617651, -0.0502846), 
    cameraTarget=(0.409053, 0.101596, -0.0942411))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.54548, 
    farPlane=2.74565, width=0.974567, height=0.602555, cameraPosition=(2.23372, 
    -0.762297, -0.675363), cameraUpVector=(-0.699354, -0.178417, -0.69215), 
    cameraTarget=(0.425025, 0.0951534, -0.0752388))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p1 = mdb.models['Model-1'].parts['Short Side With Holes']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Model-1'].parts['Short Side With Holes']
p.deleteMesh()
p = mdb.models['Model-1'].parts['Short Side With Holes']
p.seedPart(size=0.025, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Short Side With Holes']
p.generateMesh()
p1 = mdb.models['Model-1'].parts['Bottom']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['Bottom']
p.deleteMesh()
p = mdb.models['Model-1'].parts['Bottom']
p.seedPart(size=0.025, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Bottom']
p.generateMesh()
p = mdb.models['Model-1'].parts['Bottom']
p.deleteMesh()
p = mdb.models['Model-1'].parts['Bottom']
p.seedPart(size=0.02, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Bottom']
p.generateMesh()
p = mdb.models['Model-1'].parts['Bottom']
p.deleteMesh()
p = mdb.models['Model-1'].parts['Bottom']
p.seedPart(size=0.01, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Bottom']
p.generateMesh()
p1 = mdb.models['Model-1'].parts['Long_Side']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['Long_Side']
p.deleteMesh()
p = mdb.models['Model-1'].parts['Long_Side']
p.seedPart(size=0.025, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Long_Side']
p.generateMesh()
p1 = mdb.models['Model-1'].parts['Short Side With Holes']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p1 = mdb.models['Model-1'].parts['Short Side']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['Short Side']
p.deleteMesh()
p = mdb.models['Model-1'].parts['Short Side']
p.seedPart(size=0.025, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Short Side']
p.generateMesh()
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
mdb.jobs['Pressure_Box_With_Holes'].submit(consistencyChecking=OFF)
#: The job input file "Pressure_Box_With_Holes.inp" has been submitted for analysis.
#: Error in job Pressure_Box_With_Holes: Normal cannot be computed in 26 elements. The nodal coordinates may be incorrect or the element aspect ratio may exceed 1000 to 1. The elements have been identified in element set ErrElemNormal.
#: Error in job Pressure_Box_With_Holes: The geometry of 8 elements is too distorted. Check the nodal coordinates or node numbering on elements identified in element set ErrElemDistorted.
#: Error in job Pressure_Box_With_Holes: The area of 7 elements is zero, small, or negative. Check coordinates or node numbering, or modify the mesh seed. The elements have been identified in element set ErrElemAreaSmallNegZero.
#: Error in job Pressure_Box_With_Holes: Error in defining normal to the element surface at a node in 26 elements. The elements have been identified in element set ErrElemShellNormal.
#: Job Pressure_Box_With_Holes: Analysis Input File Processor aborted due to errors.
#: Error in job Pressure_Box_With_Holes: Analysis Input File Processor exited with an error.
#: Job Pressure_Box_With_Holes aborted due to errors.
p1 = mdb.models['Model-1'].parts['Bottom']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['Bottom']
p.deleteMesh()
p = mdb.models['Model-1'].parts['Bottom']
p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Bottom']
p.generateMesh()
p = mdb.models['Model-1'].parts['Bottom']
p.deleteMesh()
p = mdb.models['Model-1'].parts['Bottom']
p.deleteSeeds()
p = mdb.models['Model-1'].parts['Bottom']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#fff ]', ), )
p.deleteSeeds(regions=pickedEdges)
p = mdb.models['Model-1'].parts['Bottom']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#fff ]', ), )
p.seedEdgeBySize(edges=pickedEdges, size=0.025, deviationFactor=0.1, 
    constraint=FINER)
p = mdb.models['Model-1'].parts['Bottom']
p.generateMesh()
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.jobs['Pressure_Box_With_Holes'].submit(consistencyChecking=OFF)
#: The job input file "Pressure_Box_With_Holes.inp" has been submitted for analysis.
#: Error in job Pressure_Box_With_Holes: Normal cannot be computed in 3 elements. The nodal coordinates may be incorrect or the element aspect ratio may exceed 1000 to 1. The elements have been identified in element set ErrElemNormal.
#: Error in job Pressure_Box_With_Holes: The geometry of 1 elements is too distorted. Check the nodal coordinates or node numbering on elements identified in element set ErrElemDistorted.
#: Error in job Pressure_Box_With_Holes: The area of 1 elements is zero, small, or negative. Check coordinates or node numbering, or modify the mesh seed. The elements have been identified in element set ErrElemAreaSmallNegZero.
#: Error in job Pressure_Box_With_Holes: Error in defining normal to the element surface at a node in 3 elements. The elements have been identified in element set ErrElemShellNormal.
#: Job Pressure_Box_With_Holes: Analysis Input File Processor aborted due to errors.
#: Error in job Pressure_Box_With_Holes: Analysis Input File Processor exited with an error.
#: Job Pressure_Box_With_Holes aborted due to errors.
mdb.jobs['Pressure_Box_With_Holes'].submit(consistencyChecking=OFF)
#: The job input file "Pressure_Box_With_Holes.inp" has been submitted for analysis.
#: Error in job Pressure_Box_With_Holes: Normal cannot be computed in 3 elements. The nodal coordinates may be incorrect or the element aspect ratio may exceed 1000 to 1. The elements have been identified in element set ErrElemNormal.
#: Error in job Pressure_Box_With_Holes: The geometry of 1 elements is too distorted. Check the nodal coordinates or node numbering on elements identified in element set ErrElemDistorted.
#: Error in job Pressure_Box_With_Holes: The area of 1 elements is zero, small, or negative. Check coordinates or node numbering, or modify the mesh seed. The elements have been identified in element set ErrElemAreaSmallNegZero.
#: Error in job Pressure_Box_With_Holes: Error in defining normal to the element surface at a node in 3 elements. The elements have been identified in element set ErrElemShellNormal.
#: Job Pressure_Box_With_Holes: Analysis Input File Processor aborted due to errors.
#: Error in job Pressure_Box_With_Holes: Analysis Input File Processor exited with an error.
#: Job Pressure_Box_With_Holes aborted due to errors.
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.57317, 
    farPlane=2.68544, width=0.992031, height=0.613352, cameraPosition=(1.93723, 
    -0.834255, -1.20178), cameraUpVector=(-0.15279, 0.921125, -0.358027), 
    cameraTarget=(0.404633, 0.0877602, -0.121141))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.61461, 
    farPlane=2.64819, width=1.01816, height=0.629508, cameraPosition=(
    -0.907652, -1.52904, -0.565832), cameraUpVector=(0.57629, 0.206851, 
    -0.790634), cameraTarget=(0.351684, 0.074829, -0.109305))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.59483, 
    farPlane=2.64807, width=1.00569, height=0.621798, cameraPosition=(-1.22204, 
    1.51627, -0.0948791), cameraUpVector=(0.392218, -0.0556871, -0.918185), 
    cameraTarget=(0.34553, 0.134442, -0.100086))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.55901, 
    farPlane=2.66856, width=0.983103, height=0.607832, cameraPosition=(
    -1.24763, 0.878235, -1.24077), cameraUpVector=(0.745507, -0.262242, 
    -0.612739), cameraTarget=(0.345147, 0.124885, -0.117249))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.588, 
    farPlane=2.64747, width=1.00139, height=0.619137, cameraPosition=(-1.14231, 
    -1.35126, -0.321406), cameraUpVector=(0.253572, 0.353184, -0.900534), 
    cameraTarget=(0.346348, 0.0994577, -0.106764))
o3 = session.openOdb(
    name='C:/Users/chs17004/Desktop/Abaqus Pressure Vessel/Pressure_Box_With_Holes.odb')
#: Model: C:/Users/chs17004/Desktop/Abaqus Pressure Vessel/Pressure_Box_With_Holes.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     7
#: Number of Meshes:             7
#: Number of Element Sets:       32
#: Number of Node Sets:          29
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/chs17004/Desktop/Abaqus Pressure Vessel/Pressure_Box_With_Holes.odb'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.73075, 
    farPlane=2.38556, width=1.0914, height=0.674791, cameraPosition=(0.163663, 
    2.16349, -0.124987), cameraUpVector=(-0.812001, -0.430567, -0.394039), 
    cameraTarget=(0.404633, 0.0877594, -0.121142))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.47654, 
    farPlane=2.58117, width=0.931095, height=0.575677, cameraPosition=(
    -1.60853, 0.448657, 0.177386), cameraUpVector=(0.127065, -0.573911, 
    -0.809), cameraTarget=(0.431773, 0.114021, -0.125773))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.4814, 
    farPlane=2.5666, width=0.934161, height=0.577573, cameraPosition=(
    -0.999431, -1.04525, -1.04848), cameraUpVector=(0.754191, 0.193501, 
    -0.627497), cameraTarget=(0.413513, 0.158806, -0.0890232))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.54503, 
    farPlane=2.49434, width=0.974289, height=0.602383, cameraPosition=(
    -0.535488, -0.864898, 1.39949), cameraUpVector=(0.00689346, -0.578475, 
    -0.815671), cameraTarget=(0.39846, 0.152954, -0.16845))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.56343, 
    farPlane=2.47595, width=0.769732, height=0.47591, viewOffsetX=-0.000525907, 
    viewOffsetY=0.0426961)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.45742, 
    farPlane=2.54445, width=0.717542, height=0.443641, cameraPosition=(
    -1.28822, 1.11572, 0.384812), cameraUpVector=(-0.103019, -0.391099, 
    -0.914565), cameraTarget=(0.439757, 0.0532142, -0.117099), 
    viewOffsetX=-0.000490248, viewOffsetY=0.0398012)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.54707, 
    farPlane=2.47107, width=0.761682, height=0.470932, cameraPosition=(
    -0.52067, 1.46317, -1.30975), cameraUpVector=(0.189556, -0.83683, 
    -0.513599), cameraTarget=(0.380381, 0.0611756, -0.0490957), 
    viewOffsetX=-0.000520406, viewOffsetY=0.0422496)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.55039, 
    farPlane=2.55203, width=0.763315, height=0.471942, cameraPosition=(
    -1.12025, -1.29281, -0.0971343), cameraUpVector=(0.209565, 0.272819, 
    -0.938964), cameraTarget=(0.408171, 0.132137, -0.0838258), 
    viewOffsetX=-0.000521522, viewOffsetY=0.0423402)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.52894, 
    farPlane=2.58009, width=0.752754, height=0.465412, cameraPosition=(
    -1.17759, -1.20022, -0.418452), cameraUpVector=(0.404739, 0.267671, 
    -0.874379), cameraTarget=(0.397918, 0.129824, -0.0786406), 
    viewOffsetX=-0.000514306, viewOffsetY=0.0417544)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.69984, 
    farPlane=2.39488, width=0.836893, height=0.517434, cameraPosition=(
    -0.091419, 2.11026, -0.110634), cameraUpVector=(0.262351, -0.293594, 
    -0.919225), cameraTarget=(0.378392, 0.0742623, -0.0840348), 
    viewOffsetX=-0.000571793, viewOffsetY=0.0464215)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.51064, 
    farPlane=2.61066, width=0.743744, height=0.459842, cameraPosition=(2.09959, 
    1.13705, -0.581505), cameraUpVector=(-0.515431, -0.211382, -0.830451), 
    cameraTarget=(0.358522, 0.0982602, -0.0752475), viewOffsetX=-0.00050815, 
    viewOffsetY=0.0412546)
p1 = mdb.models['Model-1'].parts['Short Side With Holes']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['Short Side With Holes']
p.deleteMesh()
p = mdb.models['Model-1'].parts['Short Side With Holes']
p.deleteSeeds()
p = mdb.models['Model-1'].parts['Short Side With Holes']
p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Short Side With Holes']
p.generateMesh()
p1 = mdb.models['Model-1'].parts['Bottom']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['Bottom']
f = p.faces
pickedRegions = f.getSequenceFromMask(mask=('[#3 ]', ), )
p.deleteMesh(regions=pickedRegions)
p = mdb.models['Model-1'].parts['Bottom']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#f ]', ), )
p.deleteSeeds(regions=pickedEdges)
p = mdb.models['Model-1'].parts['Bottom']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#fff ]', ), )
p.deleteSeeds(regions=pickedEdges)
p = mdb.models['Model-1'].parts['Bottom']
e = p.edges
pickedEdges = e.getSequenceFromMask(mask=('[#fff ]', ), )
p.seedEdgeBySize(edges=pickedEdges, size=0.05, deviationFactor=0.1, 
    constraint=FINER)
p = mdb.models['Model-1'].parts['Bottom']
p.generateMesh()
p1 = mdb.models['Model-1'].parts['Short Side']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['Short Side']
p.deleteMesh()
p = mdb.models['Model-1'].parts['Short Side']
p.deleteSeeds()
p = mdb.models['Model-1'].parts['Short Side']
p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Short Side']
p.generateMesh()
p1 = mdb.models['Model-1'].parts['Long_Side']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['Long_Side']
p.deleteMesh()
p = mdb.models['Model-1'].parts['Long_Side']
p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Long_Side']
p.generateMesh()
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.jobs['Pressure_Box_With_Holes'].submit(consistencyChecking=OFF)
#: The job input file "Pressure_Box_With_Holes.inp" has been submitted for analysis.
#: Job Pressure_Box_With_Holes: Analysis Input File Processor completed successfully.
#: Job Pressure_Box_With_Holes: Abaqus/Standard completed successfully.
#: Job Pressure_Box_With_Holes completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/chs17004/Desktop/Abaqus Pressure Vessel/Pressure_Box_With_Holes.odb'])
o3 = session.openOdb(
    name='C:/Users/chs17004/Desktop/Abaqus Pressure Vessel/Pressure_Box_With_Holes.odb')
#: Model: C:/Users/chs17004/Desktop/Abaqus Pressure Vessel/Pressure_Box_With_Holes.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     7
#: Number of Meshes:             7
#: Number of Element Sets:       27
#: Number of Node Sets:          29
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.58039, 
    farPlane=2.65134, width=0.996583, height=0.616167, cameraPosition=(2.07742, 
    0.369359, -1.34147), cameraUpVector=(-0.731535, 0.617275, -0.28953), 
    cameraTarget=(0.404633, 0.0877596, -0.121141))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.81054, 
    farPlane=2.43119, width=1.14171, height=0.705897, cameraPosition=(0.37613, 
    -0.847611, -2.00544), cameraUpVector=(-0.404009, 0.911728, -0.0743601), 
    cameraTarget=(0.383575, 0.0726968, -0.129359))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.74645, 
    farPlane=2.53847, width=1.10129, height=0.680908, cameraPosition=(0.669363, 
    2.22382, 0.136338), cameraUpVector=(-0.975019, -0.196632, -0.103319), 
    cameraTarget=(0.392158, 0.162598, -0.0666692))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.54499, 
    farPlane=2.75957, width=0.974259, height=0.602364, cameraPosition=(2.10118, 
    1.16735, -0.798759), cameraUpVector=(-0.614392, -0.202653, -0.762531), 
    cameraTarget=(0.427439, 0.136566, -0.0897108))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.71498, 
    farPlane=2.50451, width=1.08146, height=0.668647, cameraPosition=(
    0.0208899, -1.66892, -1.18511), cameraUpVector=(-0.100634, 0.784412, 
    -0.612022), cameraTarget=(0.361757, 0.0952497, -0.118206))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.56457, 
    farPlane=2.64841, width=0.986615, height=0.610004, cameraPosition=(1.82533, 
    -1.3638, -0.482169), cameraUpVector=(-0.502319, 0.193167, -0.84283), 
    cameraTarget=(0.378921, 0.098152, -0.11152))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.57991, 
    farPlane=2.61605, width=0.996287, height=0.615984, cameraPosition=(1.62196, 
    1.71538, -0.642927), cameraUpVector=(-0.121002, -0.604798, -0.787133), 
    cameraTarget=(0.377299, 0.122719, -0.112803))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.5808, 
    farPlane=2.61388, width=0.996846, height=0.61633, cameraPosition=(
    -0.996714, 1.69203, -0.321722), cameraUpVector=(0.3152, -0.290944, 
    -0.903327), cameraTarget=(0.366947, 0.122627, -0.111533))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.74315, 
    farPlane=2.44387, width=1.09923, height=0.679629, cameraPosition=(0.161473, 
    1.05744, -1.97352), cameraUpVector=(0.377832, -0.916669, -0.130231), 
    cameraTarget=(0.371174, 0.120311, -0.117562))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.57149, 
    farPlane=2.6145, width=0.990984, height=0.612705, cameraPosition=(1.95182, 
    0.267669, -1.4792), cameraUpVector=(-0.467436, -0.875077, -0.125475), 
    cameraTarget=(0.374449, 0.118866, -0.116658))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.6101, 
    farPlane=2.57569, width=1.01533, height=0.627759, cameraPosition=(1.65214, 
    0.368585, -1.75134), cameraUpVector=(0.525292, 0.0711856, 0.847939), 
    cameraTarget=(0.373974, 0.119026, -0.117089))
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'Cap-Copy-1', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.64463, 
    farPlane=2.53927, width=1.03711, height=0.641221, cameraPosition=(1.3872, 
    -0.162383, -1.92306), cameraUpVector=(0.354015, -0.63819, 0.683656), 
    cameraTarget=(0.373567, 0.11821, -0.117353))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.64339, 
    farPlane=2.53884, width=1.03633, height=0.640741, cameraPosition=(
    -0.776826, 0.139725, -1.86323), cameraUpVector=(0.541719, -0.839929, 
    0.0325654), cameraTarget=(0.371219, 0.118538, -0.117288))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.58556, 
    farPlane=2.59573, width=0.999863, height=0.618195, cameraPosition=(1.49457, 
    -0.758874, -1.64671), cameraUpVector=(-0.527702, -0.705634, 0.472875), 
    cameraTarget=(0.372779, 0.117921, -0.117139))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.63254, 
    farPlane=2.54966, width=1.02949, height=0.63651, cameraPosition=(1.34007, 
    -0.425149, -1.88809), cameraUpVector=(-0.474345, -0.795004, 0.378109), 
    cameraTarget=(0.372708, 0.118075, -0.11725))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.73283, 
    farPlane=2.45391, width=1.09273, height=0.675613, cameraPosition=(0.518793, 
    1.53139, -1.65056), cameraUpVector=(-0.000176087, -0.919702, -0.392616), 
    cameraTarget=(0.372152, 0.119399, -0.117089))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.82046, 
    farPlane=2.36371, width=1.14799, height=0.70978, cameraPosition=(0.444819, 
    0.0157762, -2.20403), cameraUpVector=(0.118429, -0.91637, 0.382414), 
    cameraTarget=(0.372022, 0.116729, -0.118064))
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Long_Side-2'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
s2 = a.instances['Short Side With Holes-1'].faces
side1Faces2 = s2.getSequenceFromMask(mask=('[#1 ]', ), )
s3 = a.instances['Long_Side-1'].faces
side1Faces3 = s3.getSequenceFromMask(mask=('[#1 ]', ), )
s4 = a.instances['Short Side-1'].faces
side2Faces4 = s4.getSequenceFromMask(mask=('[#1 ]', ), )
a.Surface(side1Faces=side1Faces1+side1Faces2+side1Faces3, 
    side2Faces=side2Faces4, name='Side_Pressure_Surface')
#: The surface 'Side_Pressure_Surface' has been edited (4 faces).
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['Pressure_Box_With_Holes'].submit(consistencyChecking=OFF)
#: The job input file "Pressure_Box_With_Holes.inp" has been submitted for analysis.
#: Job Pressure_Box_With_Holes: Analysis Input File Processor completed successfully.
#: Job Pressure_Box_With_Holes: Abaqus/Standard completed successfully.
#: Job Pressure_Box_With_Holes completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/chs17004/Desktop/Abaqus Pressure Vessel/Pressure_Box_With_Holes.odb'])
o3 = session.openOdb(
    name='C:/Users/chs17004/Desktop/Abaqus Pressure Vessel/Pressure_Box_With_Holes.odb')
#: Model: C:/Users/chs17004/Desktop/Abaqus Pressure Vessel/Pressure_Box_With_Holes.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     7
#: Number of Meshes:             7
#: Number of Element Sets:       27
#: Number of Node Sets:          29
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.56185, 
    farPlane=2.69912, width=0.984893, height=0.608939, cameraPosition=(2.27728, 
    -0.607934, -0.734298), cameraUpVector=(-0.238992, 0.818453, -0.52251), 
    cameraTarget=(0.404633, 0.0877597, -0.121141))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.68964, 
    farPlane=2.58511, width=1.06548, height=0.658762, cameraPosition=(1.03501, 
    -1.58247, -1.23118), cameraUpVector=(-0.132151, 0.778375, -0.613733), 
    cameraTarget=(0.380836, 0.0690916, -0.130659))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.57619, 
    farPlane=2.69564, width=0.993942, height=0.614534, cameraPosition=(2.37626, 
    0.0349005, 0.662388), cameraUpVector=(-0.0339147, 0.61558, -0.787344), 
    cameraTarget=(0.421922, 0.118635, -0.0726547))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.59849, 
    farPlane=2.69635, width=1.00801, height=0.62323, cameraPosition=(1.96774, 
    -0.0768731, -1.50245), cameraUpVector=(-0.76489, 0.485018, -0.423911), 
    cameraTarget=(0.413077, 0.116215, -0.119525))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.63952, 
    farPlane=2.65322, width=1.03389, height=0.63923, cameraPosition=(1.15412, 
    -0.900618, -1.79943), cameraUpVector=(-0.760776, 0.585929, -0.279118), 
    cameraTarget=(0.391197, 0.0940625, -0.127511))
mdb.save()
#: The model database has been saved to "C:\Users\chs17004\Desktop\Abaqus Pressure Vessel\Pressure_Box With Holes.cae".
