# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2019 replay file
# Internal Version: 2018_09_24-14.41.51 157541
# Run by chs17004 on Thu Oct  8 09:10:57 2020
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=387.285949707031, 
    height=249.75)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
openMdb('Pressure_Box With Bolts.cae')
#: The model database "C:\Users\chs17004\Desktop\Abaqus Pressure Vessel\Pressure Box with Bolts\Pressure_Box With Bolts.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['Bottom']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=2.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.rectangle(point1=(0.0, 0.0), point2=(0.225, -0.15))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.80791, 
    farPlane=1.96332, width=0.830907, height=0.513733, cameraPosition=(
    0.159531, -0.144982, 1.88562), cameraTarget=(0.159531, -0.144982, 0))
s.ObliqueDimension(vertex1=v[3], vertex2=v[0], textPoint=(0.0838877409696579, 
    0.0221644639968872), value=0.38)
d[0].setValues(value=0.375, )
s.undo()
s.undo()
s.undo()
s.rectangle(point1=(0.0, 0.0), point2=(0.425, -0.05))
s.rectangle(point1=(0.0, 0.0), point2=(0.05, -0.275))
s.DistanceDimension(entity1=g[6], entity2=g[8], textPoint=(0.0295801013708115, 
    0.0329481065273285), value=0.04)
d[0].setValues(value=0.03876, )
s.EqualLengthConstraint(entity1=g[4], entity2=g[7])
s.DistanceDimension(entity1=g[8], entity2=g[4], textPoint=(0.228190913796425, 
    0.046319842338562), value=0.375)
s.ObliqueDimension(vertex1=v[0], vertex2=v[4], textPoint=(-0.0309341102838516, 
    -0.0938675403594971), value=0.1525)
s.dragEntity(entity=v[0], points=((0.00562, -0.06125), (0.0, -0.0625), (0.0, 
    -0.0125), (0.0, -0.00630435347557068), (0.0, 0.0)))
s.CircleByCenterPerimeter(center=(0.0191065222024918, -0.0201073884963989), 
    point1=(0.025, -0.025))
s.CircleByCenterPerimeter(center=(0.0125, -0.0625), point1=(0.0183306783437729, 
    -0.0641047060489655))
s.CircleByCenterPerimeter(center=(0.0167790204286575, -0.0938675403594971), 
    point1=(0.0183306783437729, -0.100769072771072))
s.CircleByCenterPerimeter(center=(0.0125, -0.125), point1=(0.0175548642873764, 
    -0.131394624710083))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.83806, 
    farPlane=1.93318, width=0.508567, height=0.314437, cameraPosition=(
    0.103062, -0.111392, 1.88562), cameraTarget=(0.103062, -0.111392, 0))
s.Line(point1=(0.0191065222024918, -0.0201073884963989), point2=(0.0125, 
    -0.0625))
s.Line(point1=(0.0125, -0.0625), point2=(0.0167790204286575, 
    -0.0938675403594971))
s.Line(point1=(0.0167790204286575, -0.0938675403594971), point2=(0.0125, 
    -0.125))
s.VerticalConstraint(entity=g[14])
s.VerticalConstraint(entity=g[15])
s.VerticalConstraint(entity=g[16])
s.EqualLengthConstraint(entity1=g[14], entity2=g[15])
s.EqualLengthConstraint(entity1=g[15], entity2=g[16], addUndoState=False)
s.ObliqueDimension(vertex1=v[7], vertex2=v[9], textPoint=(-0.0161263272166252, 
    -0.0428812503814697), value=0.0688958)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.80627, 
    farPlane=1.96497, width=0.960313, height=0.593742, cameraPosition=(
    0.237964, -0.128745, 1.88562), cameraTarget=(0.237964, -0.128745, 0))
s.undo()
s.delete(objectList=(g[13], ))
s.delete(objectList=(g[16], ))
s.ObliqueDimension(vertex1=v[9], vertex2=v[11], textPoint=(-0.080347016453743, 
    -0.075652003288269), value=0.0688958)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.83416, 
    farPlane=1.93708, width=0.550254, height=0.340211, cameraPosition=(
    0.0822682, -0.0757721, 1.88562), cameraTarget=(0.0822682, -0.0757721, 0))
s.dragEntity(entity=v[7], points=((0.0158032611012459, 0.0440394522874825), (
    0.0125, 0.0440394522874825), (0.0125, 0.0), (0.0125, -0.0125), (
    0.0193306058645248, -0.025), (0.0125, 0.0), (0.0125, 0.0125), (
    0.0185599476099014, 0.025)))
s.undo()
s.RadialDimension(curve=g[10], textPoint=(-0.0148355066776276, 
    0.03834567964077), radius=0.01)
d[4].setValues(value=0.005, )
s.dragEntity(entity=v[7], points=((0.0158032611012459, 0.0440394522874825), (
    0.0125, 0.0440394522874825), (0.0195874869823456, 0.0), (
    0.0193306058645248, -0.0182133316993713), (0.0183030515909195, -0.025), (
    0.0180461555719376, -0.0193559527397156), (0.0190737247467041, -0.0125)))
s.EqualRadiusConstraint(entity1=g[10], entity2=g[11])
s.EqualRadiusConstraint(entity1=g[11], entity2=g[12], addUndoState=False)
s.Line(point1=(0.0190737247467041, -0.0125), point2=(0.0190737247467041, 0.0))
s.VerticalConstraint(entity=g[17], addUndoState=False)
s.CoincidentConstraint(entity1=v[15], entity2=g[5], addUndoState=False)
s.Line(point1=(0.0190737247467041, -0.0125), point2=(0.0, -0.01938))
s.CoincidentConstraint(entity1=v[16], entity2=g[2], addUndoState=False)
s.EqualDistanceConstraint(entity1=v[0], entity2=v[1], midpoint=v[16], 
    addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.86528, 
    farPlane=1.90596, width=0.217511, height=0.134483, cameraPosition=(
    0.0347402, -0.0410777, 1.88562), cameraTarget=(0.0347402, -0.0410777, 0))
s.undo()
s.Line(point1=(0.0, -0.01938), point2=(0.0190737247467041, -0.0125))
s.CoincidentConstraint(entity1=v[16], entity2=g[2], addUndoState=False)
s.EqualDistanceConstraint(entity1=v[0], entity2=v[1], midpoint=v[16], 
    addUndoState=False)
s.HorizontalConstraint(entity=g[18])
s.VerticalConstraint(entity=g[17])
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.86581, 
    farPlane=1.90542, width=0.211765, height=0.13093, cameraPosition=(
    0.0382367, -0.0342407, 1.88562), cameraTarget=(0.0382367, -0.0342407, 0))
s.delete(objectList=(g[17], ))
s.Line(point1=(0.01938, 0.0), point2=(0.0190737247467041, -0.01938))
s.CoincidentConstraint(entity1=v[17], entity2=g[9], addUndoState=False)
s.EqualDistanceConstraint(entity1=v[6], entity2=v[0], midpoint=v[17], 
    addUndoState=False)
s.VerticalConstraint(entity=g[19])
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.83075, 
    farPlane=1.94049, width=0.66407, height=0.410581, cameraPosition=(0.115399, 
    -0.0925801, 1.88562), cameraTarget=(0.115399, -0.0925801, 0))
s.CircleByCenterPerimeter(center=(0.05, -0.025), point1=(0.0564940422773361, 
    -0.0217367187142372))
s.CircleByCenterPerimeter(center=(0.1, -0.025), point1=(0.105167761445045, 
    -0.0207025185227394))
#: Warning: Coincident point selected
s.CircleByCenterPerimeter(center=(0.15, -0.025), point1=(0.1625, -0.025))
s.CircleByCenterPerimeter(center=(0.2125, -0.025), point1=(0.220186486840248, 
    -0.0231156721711159))
s.CircleByCenterPerimeter(center=(0.292421936988831, -0.0241498723626137), 
    point1=(0.3, -0.025))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.83674, 
    farPlane=1.9345, width=0.522723, height=0.323189, cameraPosition=(0.204689, 
    -0.0582766, 1.88562), cameraTarget=(0.204689, -0.0582766, 0))
s.Line(point1=(0.01938, -0.01938), point2=(0.05, -0.025))
s.Line(point1=(0.05, -0.025), point2=(0.1, -0.025))
s.HorizontalConstraint(entity=g[26], addUndoState=False)
s.Line(point1=(0.1, -0.025), point2=(0.15, -0.025))
s.HorizontalConstraint(entity=g[27], addUndoState=False)
s.ParallelConstraint(entity1=g[26], entity2=g[27], addUndoState=False)
s.Line(point1=(0.15, -0.025), point2=(0.2125, -0.025))
s.HorizontalConstraint(entity=g[28], addUndoState=False)
s.ParallelConstraint(entity1=g[27], entity2=g[28], addUndoState=False)
s.Line(point1=(0.2125, -0.025), point2=(0.292421936988831, 
    -0.0241498723626137))
s.HorizontalConstraint(entity=g[25])
s.HorizontalConstraint(entity=g[26])
s.HorizontalConstraint(entity=g[27])
s.HorizontalConstraint(entity=g[28])
s.HorizontalConstraint(entity=g[29])
s.EqualLengthConstraint(entity1=g[25], entity2=g[26])
s.EqualLengthConstraint(entity1=g[26], entity2=g[27], addUndoState=False)
s.EqualLengthConstraint(entity1=g[27], entity2=g[28], addUndoState=False)
s.EqualLengthConstraint(entity1=g[28], entity2=g[29], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.84242, 
    farPlane=1.92881, width=0.461878, height=0.28557, cameraPosition=(0.154551, 
    -0.061401, 1.88562), cameraTarget=(0.154551, -0.061401, 0))
s.ObliqueDimension(vertex1=v[7], vertex2=v[18], textPoint=(0.041776642203331, 
    0.0171246826648712), value=0.07173390909)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.82628, 
    farPlane=1.94495, width=0.634504, height=0.392301, cameraPosition=(
    0.172564, -0.0806814, 1.88562), cameraTarget=(0.172564, -0.0806814, 0))
s.EqualRadiusConstraint(entity1=g[10], entity2=g[20])
s.EqualRadiusConstraint(entity1=g[20], entity2=g[21], addUndoState=False)
s.EqualRadiusConstraint(entity1=g[21], entity2=g[22], addUndoState=False)
s.EqualRadiusConstraint(entity1=g[22], entity2=g[23], addUndoState=False)
s.EqualRadiusConstraint(entity1=g[23], entity2=g[24], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.84207, 
    farPlane=1.92917, width=0.465665, height=0.287911, cameraPosition=(
    0.113093, -0.0802743, 1.88562), cameraTarget=(0.113093, -0.0802743, 0))
s.delete(objectList=(d[2], ))
s.DistanceDimension(entity1=g[3], entity2=g[7], textPoint=(-0.030171737074852, 
    -0.10698651522398), value=0.1525)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.85533, 
    farPlane=1.91591, width=0.323882, height=0.20025, cameraPosition=(
    0.0808019, -0.0473683, 1.88562), cameraTarget=(0.0808019, -0.0473683, 0))
s.setAsConstruction(objectList=(g[3], g[8]))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.83573, 
    farPlane=1.93551, width=0.603784, height=0.373307, cameraPosition=(
    0.171577, -0.0719445, 1.88562), cameraTarget=(0.171577, -0.0719445, 0))
s.Line(point1=(0.03876, -0.03876), point2=(0.03876, -0.19126))
s.VerticalConstraint(entity=g[30], addUndoState=False)
s.PerpendicularConstraint(entity1=g[3], entity2=g[30], addUndoState=False)
s.CoincidentConstraint(entity1=v[28], entity2=g[3], addUndoState=False)
s.Line(point1=(0.03876, -0.03876), point2=(0.41376, -0.03876))
s.HorizontalConstraint(entity=g[31], addUndoState=False)
s.PerpendicularConstraint(entity1=g[30], entity2=g[31], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.8382, 
    farPlane=1.93304, width=0.507102, height=0.313531, cameraPosition=(
    0.432225, -0.00222846, 1.88562), cameraTarget=(0.432225, -0.00222846, 0))
s.setAsConstruction(objectList=(g[7], g[4]))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.80617, 
    farPlane=1.96507, width=0.84955, height=0.525259, cameraPosition=(0.275204, 
    -0.104933, 1.88562), cameraTarget=(0.275204, -0.104933, 0))
s.copyMirror(mirrorLine=g[4], objectList=(g[2], g[3], g[4], g[5], g[6], g[7], 
    g[8], g[9], g[10], g[11], g[12], g[14], g[15], g[18], g[19], g[20], g[21], 
    g[22], g[23], g[24], g[25], g[26], g[27], g[28], g[29], g[30], g[31]))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.74411, 
    farPlane=2.02713, width=1.71257, height=1.05885, cameraPosition=(0.48647, 
    -0.0234098, 1.88562), cameraTarget=(0.48647, -0.0234098, 0))
s.copyMirror(mirrorLine=g[7], objectList=(g[2], g[3], g[4], g[5], g[6], g[7], 
    g[8], g[9], g[10], g[11], g[12], g[14], g[15], g[18], g[19], g[20], g[21], 
    g[22], g[23], g[24], g[25], g[26], g[27], g[28], g[29], g[30], g[31], 
    g[32], g[33], g[34], g[35], g[36], g[37], g[38], g[39], g[40], g[41], 
    g[42], g[43], g[44], g[45], g[46], g[47], g[48], g[49], g[50], g[51], 
    g[52], g[53], g[54], g[55], g[56], g[57], g[58]))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.81309, 
    farPlane=1.95815, width=0.775585, height=0.479528, cameraPosition=(
    0.372458, -0.150161, 1.88562), cameraTarget=(0.372458, -0.150161, 0))
s.undo()
s.undo()
s.undo()
s.undo()
s.undo()
s.setAsConstruction(objectList=(g[4], g[7]))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.77186, 
    farPlane=1.99937, width=1.37664, height=0.851151, cameraPosition=(0.451347, 
    -0.0874417, 1.88562), cameraTarget=(0.451347, -0.0874417, 0))
s.copyMirror(mirrorLine=g[4], objectList=(g[2], g[3], g[4], g[5], g[6], g[7], 
    g[8], g[9], g[10], g[11], g[12], g[14], g[15], g[18], g[19], g[20], g[21], 
    g[22], g[23], g[24], g[25], g[26], g[27], g[28], g[29]))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.76261, 
    farPlane=2.00863, width=1.48863, height=0.920388, cameraPosition=(0.427504, 
    -0.101453, 1.88562), cameraTarget=(0.427504, -0.101453, 0))
s.copyMirror(mirrorLine=g[7], objectList=(g[2], g[3], g[4], g[5], g[6], g[7], 
    g[8], g[9], g[10], g[11], g[12], g[14], g[15], g[18], g[19], g[20], g[21], 
    g[22], g[23], g[24], g[25], g[26], g[27], g[28], g[29], g[30], g[31], 
    g[32], g[33], g[34], g[35], g[36], g[37], g[38], g[39], g[40], g[41], 
    g[42], g[43], g[44], g[45], g[46], g[47], g[48], g[49], g[50], g[51], 
    g[52], g[53], g[54]))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.85693, 
    farPlane=1.9143, width=0.306757, height=0.189662, cameraPosition=(0.736294, 
    -0.315127, 1.88562), cameraTarget=(0.736294, -0.315127, 0))
s.setAsConstruction(objectList=(g[19], g[18], g[44], g[43], g[93], g[94]))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.79753, 
    farPlane=1.97371, width=1.06606, height=0.659126, cameraPosition=(0.691038, 
    -0.234978, 1.88562), cameraTarget=(0.691038, -0.234978, 0))
s.undo()
s.undo()
s.undo()
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.82728, 
    farPlane=1.94395, width=0.705983, height=0.436495, cameraPosition=(
    0.202143, -0.0830964, 1.88562), cameraTarget=(0.202143, -0.0830964, 0))
s.setAsConstruction(objectList=(g[19], g[18], g[25], g[14], g[15], g[26], 
    g[27], g[28], g[29]))
#: Warning: Cannot continue yet--complete the step or cancel the procedure.
s.copyMirror(mirrorLine=g[4], objectList=(g[2], g[3], g[4], g[5], g[6], g[7], 
    g[8], g[9], g[10], g[11], g[12], g[14], g[15], g[18], g[19], g[20], g[21], 
    g[22], g[23], g[24], g[25], g[26], g[27], g[28], g[29]))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.74519, 
    farPlane=2.02605, width=1.69951, height=1.05077, cameraPosition=(0.468116, 
    -0.116756, 1.88562), cameraTarget=(0.468116, -0.116756, 0))
s.copyMirror(mirrorLine=g[7], objectList=(g[2], g[3], g[4], g[5], g[6], g[7], 
    g[8], g[9], g[10], g[11], g[12], g[14], g[15], g[18], g[19], g[20], g[21], 
    g[22], g[23], g[24], g[25], g[26], g[27], g[28], g[29], g[30], g[31], 
    g[32], g[33], g[34], g[35], g[36], g[37], g[38], g[39], g[40], g[41], 
    g[42], g[43], g[44], g[45], g[46], g[47], g[48], g[49], g[50], g[51], 
    g[52], g[53], g[54]))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.75613, 
    farPlane=2.01511, width=1.38468, height=0.856119, cameraPosition=(0.410241, 
    -0.262717, 1.88562), cameraTarget=(0.410241, -0.262717, 0))
s.removeGapsAndOverlaps(geomList=(g[2], g[3], g[4], g[5], g[6], g[7], g[8], 
    g[9], g[10], g[11], g[12], g[14], g[15], g[18], g[19], g[20], g[21], g[22], 
    g[23], g[24], g[25], g[26], g[27], g[28], g[29], g[30], g[31], g[32], 
    g[33], g[34], g[35], g[36], g[37], g[38], g[39], g[40], g[41], g[42], 
    g[43], g[44], g[45], g[46], g[47], g[48], g[49], g[50], g[51], g[52], 
    g[53], g[54], g[55], g[56], g[57], g[58], g[59], g[60], g[61], g[62], 
    g[63], g[64], g[65], g[66], g[67], g[68], g[69], g[70], g[71], g[72], 
    g[73], g[74], g[75], g[76], g[77], g[78], g[79], g[80], g[81], g[82], 
    g[83], g[84], g[85], g[86], g[87], g[88], g[89], g[90], g[91], g[92], 
    g[93], g[94], g[95], g[96], g[97], g[98], g[99], g[100], g[101], g[102], 
    g[103], g[104]), tolerance=0.001)
#: 16 gaps and overlaps have been removed.
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.77807, 
    farPlane=1.99317, width=1.3016, height=0.804752, cameraPosition=(0.392094, 
    -0.25147, 1.88562), cameraTarget=(0.392094, -0.25147, 0))
s.rectangle(point1=(0.03876, -0.03876), point2=(0.78876, -0.34376))
s.CoincidentConstraint(entity1=v[103], entity2=g[3], addUndoState=False)
s.CoincidentConstraint(entity1=v[105], entity2=g[81], addUndoState=False)
s.undo()
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.84805, 
    farPlane=1.92318, width=0.454622, height=0.281084, cameraPosition=(
    0.141996, -0.0981043, 1.88562), cameraTarget=(0.141996, -0.0981043, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.269766, 
    -0.08654, 1.88562), cameraTarget=(0.269766, -0.08654, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.389471, 
    -0.0794598, 1.88562), cameraTarget=(0.389471, -0.0794598, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.34108, 
    -0.0608153, 1.88562), cameraTarget=(0.34108, -0.0608153, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.86539, 
    farPlane=1.90585, width=0.244867, height=0.151396, cameraPosition=(
    0.356363, -0.0443814, 1.88562), cameraTarget=(0.356363, -0.0443814, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.306064, 
    -0.0498474, 1.88562), cameraTarget=(0.306064, -0.0498474, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.192433, 
    -0.0554405, 1.88562), cameraTarget=(0.192433, -0.0554405, 0))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(0.0772017, 
    -0.0612879, 1.88562), cameraTarget=(0.0772017, -0.0612879, 0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.84293, 
    farPlane=1.92831, width=0.516617, height=0.319414, cameraPosition=(
    0.142131, -0.129461, 1.88562), cameraTarget=(0.142131, -0.129461, 0))
s.undo()
s.undo()
s.undo()
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.82323, 
    farPlane=1.94801, width=0.667119, height=0.412466, cameraPosition=(
    0.150627, -0.142817, 1.88562), cameraTarget=(0.150627, -0.142817, 0))
s.Line(point1=(0.0, -0.19126), point2=(0.03876, -0.19126))
s.HorizontalConstraint(entity=g[30], addUndoState=False)
s.PerpendicularConstraint(entity1=g[6], entity2=g[30], addUndoState=False)
s.Line(point1=(0.03876, -0.19126), point2=(0.03876, -0.03876))
s.VerticalConstraint(entity=g[31], addUndoState=False)
s.PerpendicularConstraint(entity1=g[30], entity2=g[31], addUndoState=False)
s.CoincidentConstraint(entity1=v[28], entity2=g[3], addUndoState=False)
s.Line(point1=(0.03876, -0.03876), point2=(0.41376, -0.03876))
s.HorizontalConstraint(entity=g[32], addUndoState=False)
s.PerpendicularConstraint(entity1=g[31], entity2=g[32], addUndoState=False)
s.Line(point1=(0.41376, -0.03876), point2=(0.41376, 0.0))
s.VerticalConstraint(entity=g[33], addUndoState=False)
s.PerpendicularConstraint(entity1=g[32], entity2=g[33], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.84926, 
    farPlane=1.92198, width=0.439988, height=0.272036, cameraPosition=(
    0.104745, -0.0955359, 1.88562), cameraTarget=(0.104745, -0.0955359, 0))
s.delete(objectList=(g[6], ))
s.delete(objectList=(g[2], ))
s.delete(objectList=(g[8], ))
s.Line(point1=(0.0, 0.0), point2=(0.0, -0.19126))
s.VerticalConstraint(entity=g[34], addUndoState=False)
s.PerpendicularConstraint(entity1=g[5], entity2=g[34], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.86721, 
    farPlane=1.90403, width=0.222765, height=0.137731, cameraPosition=(
    0.054683, -0.0400255, 1.88562), cameraTarget=(0.054683, -0.0400255, 0))
d[5].setValues(textPoint=(0.05, -0.0304849147796631))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.86123, 
    farPlane=1.91001, width=0.260782, height=0.161236, cameraPosition=(
    0.0504894, -0.149519, 1.88562), cameraTarget=(0.0504894, -0.149519, 0))
d[5].setValues(textPoint=(0.05, -0.0304849147796631))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.83417, 
    farPlane=1.93707, width=0.550194, height=0.340174, cameraPosition=(
    0.163863, -0.090328, 1.88562), cameraTarget=(0.163863, -0.090328, 0))
d[5].setValues(textPoint=(0.05, -0.0304849147796631))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.86873, 
    farPlane=1.90251, width=0.180642, height=0.111687, cameraPosition=(
    0.059467, -0.0289915, 1.88562), cameraTarget=(0.059467, -0.0289915, 0))
s.delete(objectList=(g[5], ))
s.delete(objectList=(g[9], ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.83417, 
    farPlane=1.93707, width=0.622674, height=0.384987, cameraPosition=(
    0.131044, -0.0646566, 1.88562), cameraTarget=(0.131044, -0.0646566, 0))
s.Line(point1=(0.0, 0.0), point2=(0.41376, 0.0))
s.HorizontalConstraint(entity=g[35], addUndoState=False)
s.PerpendicularConstraint(entity1=g[34], entity2=g[35], addUndoState=False)
p = mdb.models['Model-1'].Part(name='Part-10', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-10']
p.BaseSolidExtrude(sketch=s, depth=0.2)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-10']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.785123, 
    farPlane=1.36467, width=0.691702, height=0.427666, viewOffsetX=0.0620059, 
    viewOffsetY=-0.0134533)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.786717, 
    farPlane=1.22126, width=0.693107, height=0.428534, cameraPosition=(
    0.0764072, 0.318585, 1.00584), cameraUpVector=(-0.453126, 0.541385, 
    -0.708223), cameraTarget=(0.209374, -0.157166, 0.0511768), 
    viewOffsetX=0.0621318, viewOffsetY=-0.0134806)
p = mdb.models['Model-1'].parts['Part-10']
s1 = p.features['Solid extrude-1'].sketch
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=s1)
s2 = mdb.models['Model-1'].sketches['__edit__']
g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
s2.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s2, 
    upToFeature=p.features['Solid extrude-1'], filter=COPLANAR_EDGES)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.897174, 
    farPlane=1.14029, width=0.230521, height=0.142526, cameraPosition=(
    0.0756466, -0.0545577, 1.11873), cameraTarget=(0.0756466, -0.0545577, 0))
s2.Line(point1=(0.0, 0.0), point2=(0.01938, -0.01938))
s2.Line(point1=(0.01938, -0.01938), point2=(0.03876, -0.03876))
s2.ParallelConstraint(entity1=g[36], entity2=g[37], addUndoState=False)
s2.setAsConstruction(objectList=(g[36], g[37]))
s2.Line(point1=(0.0, -0.03876), point2=(0.0375, 0.0))
s2.CoincidentConstraint(entity1=v[29], entity2=g[35], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.913206, 
    farPlane=1.12426, width=0.0590913, height=0.036535, cameraPosition=(
    0.0324983, -0.0282067, 1.11873), cameraTarget=(0.0324983, -0.0282067, 0))
s2.setAsConstruction(objectList=(g[38], ))
s2.delete(objectList=(g[37], ))
s2.delete(objectList=(g[36], ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.913849, 
    farPlane=1.12361, width=0.0522131, height=0.0322823, cameraPosition=(
    0.0307997, -0.0271197, 1.11873), cameraTarget=(0.0307997, -0.0271197, 0))
s2.FixedConstraint(entity=v[7])
s2.FixedConstraint(entity=g[38])
s2.undo()
s2.undo()
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.907586, 
    farPlane=1.12988, width=0.134889, height=0.0833993, cameraPosition=(
    0.0475777, -0.0379872, 1.11873), cameraTarget=(0.0475777, -0.0379872, 0))
s2.delete(objectList=(g[18], ))
s2.delete(objectList=(g[19], ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.91459, 
    farPlane=1.12287, width=0.0442873, height=0.0273819, cameraPosition=(
    0.0293131, -0.0261398, 1.11873), cameraTarget=(0.0293131, -0.0261398, 0))
s2.CoincidentConstraint(entity1=g[38], entity2=v[7])
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.907988, 
    farPlane=1.12947, width=0.130015, height=0.0803858, cameraPosition=(
    0.049614, -0.0291549, 1.11873), cameraTarget=(0.049614, -0.0291549, 0))
s2.undo()
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.911765, 
    farPlane=1.1257, width=0.0744981, height=0.0460606, cameraPosition=(
    0.0280663, -0.0329992, 1.11873), cameraTarget=(0.0280663, -0.0329992, 0))
s2.FixedConstraint(entity=v[1])
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.90855, 
    farPlane=1.12891, width=0.108874, height=0.0673145, cameraPosition=(
    0.0457702, -0.0210551, 1.11873), cameraTarget=(0.0457702, -0.0210551, 0))
s2.FixedConstraint(entity=v[29])
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.914177, 
    farPlane=1.12329, width=0.0487064, height=0.0301142, cameraPosition=(
    0.0275184, -0.0205972, 1.11873), cameraTarget=(0.0275184, -0.0205972, 0))
s2.CoincidentConstraint(entity1=v[7], entity2=g[38])
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.911679, 
    farPlane=1.12578, width=0.0754161, height=0.0466283, cameraPosition=(
    0.0325804, -0.0182597, 1.11873), cameraTarget=(0.0325804, -0.0182597, 0))
s2.Line(point1=(0.0, 0.0), point2=(0.03876, -0.03876))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.916555, 
    farPlane=1.12091, width=0.0232752, height=0.0143906, cameraPosition=(
    0.0229, -0.018682, 1.11873), cameraTarget=(0.0229, -0.018682, 0))
s2.CoincidentConstraint(entity1=g[39], entity2=v[7])
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.894914, 
    farPlane=1.14255, width=0.288244, height=0.178216, cameraPosition=(
    0.0828801, -0.0525382, 1.11873), cameraTarget=(0.0828801, -0.0525382, 0))
s2.setAsConstruction(objectList=(g[39], ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.853842, 
    farPlane=1.18362, width=0.785298, height=0.485534, cameraPosition=(
    0.209369, -0.0763051, 1.11873), cameraTarget=(0.209369, -0.0763051, 0))
s2.redo()
#* Nothing to redo.
s2.delete(objectList=(g[7], g[4]))
s2.delete(objectList=(g[30], ))
s2.delete(objectList=(g[33], ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.811407, 
    farPlane=1.22606, width=1.14766, height=0.709575, cameraPosition=(0.342931, 
    -0.134208, 1.11873), cameraTarget=(0.342931, -0.134208, 0))
s2.Line(point1=(0.0, -0.19126), point2=(0.03876, -0.19126))
s2.HorizontalConstraint(entity=g[40], addUndoState=False)
s2.PerpendicularConstraint(entity1=g[34], entity2=g[40], addUndoState=False)
s2.Line(point1=(0.41376, 0.0), point2=(0.41376, -0.03876))
s2.VerticalConstraint(entity=g[41], addUndoState=False)
s2.PerpendicularConstraint(entity1=g[35], entity2=g[41], addUndoState=False)
s2.setAsConstruction(objectList=(g[41], g[40]))
#: Warning: Cannot continue yet--complete the step or cancel the procedure.
s2.copyMirror(mirrorLine=g[41], objectList=(g[3], g[10], g[11], g[12], g[14], 
    g[15], g[20], g[21], g[22], g[23], g[24], g[25], g[26], g[27], g[28], 
    g[29], g[31], g[32], g[34], g[35], g[38], g[39], g[40], g[41]))
s2.copyMirror(mirrorLine=g[40], objectList=(g[3], g[10], g[11], g[12], g[14], 
    g[15], g[20], g[21], g[22], g[23], g[24], g[25], g[26], g[27], g[28], 
    g[29], g[31], g[32], g[34], g[35], g[38], g[39], g[40], g[41], g[42], 
    g[43], g[44], g[45], g[46], g[47], g[48], g[49], g[50], g[51], g[52], 
    g[53], g[54], g[55], g[56], g[57], g[58], g[59], g[60], g[61], g[62], 
    g[63], g[64], g[65]))
s2.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-10']
p.features['Solid extrude-1'].setValues(sketch=s2)
del mdb.models['Model-1'].sketches['__edit__']
p = mdb.models['Model-1'].parts['Part-10']
p.regenerate()
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.5928, 
    farPlane=1.3265, width=0.522264, height=0.322905, cameraPosition=(0.567817, 
    -0.594847, 0.976566), cameraUpVector=(-0.0230793, 0.989665, 0.141532), 
    cameraTarget=(0.211195, -0.113489, 0.0840882), viewOffsetX=0.046817, 
    viewOffsetY=-0.0101578)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.548314, 
    farPlane=1.37099, width=1.2484, height=0.771862, viewOffsetX=-0.0123558, 
    viewOffsetY=-0.0754052)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.724363, 
    farPlane=1.28407, width=1.64923, height=1.01969, cameraPosition=(0.266052, 
    -0.433502, 1.08461), cameraUpVector=(-0.150841, 0.987644, -0.0425007), 
    cameraTarget=(0.213809, -0.122925, 0.0568909), viewOffsetX=-0.0163229, 
    viewOffsetY=-0.0996159)
p = mdb.models['Model-1'].parts['Part-10']
s = p.features['Solid extrude-1'].sketch
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=s)
s1 = mdb.models['Model-1'].sketches['__edit__']
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s1, 
    upToFeature=p.features['Solid extrude-1'], filter=COPLANAR_EDGES)
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__edit__']
p = mdb.models['Model-1'].parts['Part-10']
p.features['Solid extrude-1'].setValues(depth=0.013)
p = mdb.models['Model-1'].parts['Part-10']
p.regenerate()
p = mdb.models['Model-1'].parts['Part-10']
p.regenerate()
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.717753, 
    farPlane=1.77332, width=1.63419, height=1.01039, cameraPosition=(-0.372117, 
    -0.938721, 0.646429), cameraUpVector=(-0.00434404, 0.846735, 0.531997), 
    cameraTarget=(0.192037, -0.185937, 0.126391), viewOffsetX=-0.016174, 
    viewOffsetY=-0.0987069)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.80012, 
    farPlane=1.69096, width=0.981211, height=0.606663, viewOffsetX=0.0143296, 
    viewOffsetY=-0.102392)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.998713, 
    farPlane=1.33151, width=1.22475, height=0.75724, cameraPosition=(0.448077, 
    -0.159058, 1.18746), cameraUpVector=(-0.145421, 0.966432, -0.211809), 
    cameraTarget=(0.312478, -0.0409777, 0.127713), viewOffsetX=0.0178863, 
    viewOffsetY=-0.127806)
p1 = mdb.models['Model-1'].parts['Top_Flange']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
del mdb.models['Model-1'].parts['Top_Flange']
del mdb.models['Model-1'].parts['Top_Flange-Copy']
p = mdb.models['Model-1'].parts['Bottom']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p1 = mdb.models['Model-1'].parts['Cap-Copy']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
del mdb.models['Model-1'].parts['Cap-Copy']
del mdb.models['Model-1'].parts['Cap']
p = mdb.models['Model-1'].parts['Bottom']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p1 = mdb.models['Model-1'].parts['Part-10']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
mdb.models['Model-1'].parts.changeKey(fromName='Part-10', toName='Flange')
#: The contents of viewport "Viewport: 1" have been copied to the clipboard.
p1 = mdb.models['Model-1'].parts['Flange']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].Part(name='Cap', 
    objectToCopy=mdb.models['Model-1'].parts['Flange'])
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.63815, 
    farPlane=2.243, width=0.925128, height=0.571988, cameraPosition=(-0.114383, 
    0.829683, 1.57022), cameraUpVector=(-0.0302453, 0.585275, -0.81027), 
    cameraTarget=(0.446856, -0.206988, -0.0108682))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.75982, 
    farPlane=2.14055, width=0.993838, height=0.61447, cameraPosition=(0.630728, 
    -0.818689, 1.84036), cameraUpVector=(0.0271456, 0.999545, -0.0131798), 
    cameraTarget=(0.434719, -0.180138, -0.0152684))
p = mdb.models['Model-1'].parts['Cap']
s = p.features['Solid extrude-1'].sketch
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=s)
s2 = mdb.models['Model-1'].sketches['__edit__']
g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
s2.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s2, 
    upToFeature=p.features['Solid extrude-1'], filter=COPLANAR_EDGES)
s2.delete(objectList=(g[31], g[3], g[42], g[58]))
s2.delete(objectList=(g[59], ))
s2.delete(objectList=(g[32], ))
s2.delete(objectList=(g[82], ))
s2.delete(objectList=(g[66], ))
s2.delete(objectList=(g[83], ))
s2.delete(objectList=(g[90], ))
s2.delete(objectList=(g[107], ))
s2.delete(objectList=(g[106], ))
s2.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Cap']
p.features['Solid extrude-1'].setValues(sketch=s2)
del mdb.models['Model-1'].sketches['__edit__']
p = mdb.models['Model-1'].parts['Cap']
p.regenerate()
session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.72865, 
    farPlane=2.18261, cameraPosition=(0.962298, -0.0714732, 1.87994), 
    cameraUpVector=(-0.079252, 0.920979, -0.381466), cameraTarget=(0.430979, 
    -0.188567, -0.0157149))
p = mdb.models['Model-1'].parts['Cap']
s = p.features['Solid extrude-1'].sketch
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=s)
s1 = mdb.models['Model-1'].sketches['__edit__']
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s1, 
    upToFeature=p.features['Solid extrude-1'], filter=COPLANAR_EDGES)
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__edit__']
p = mdb.models['Model-1'].parts['Cap']
p.features['Solid extrude-1'].setValues(depth=0.0127)
p = mdb.models['Model-1'].parts['Cap']
p.regenerate()
p = mdb.models['Model-1'].parts['Cap']
p.regenerate()
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.71604, 
    farPlane=2.19551, width=1.34095, height=0.829081, cameraPosition=(1.0218, 
    -0.0778708, 1.86366), cameraTarget=(0.490484, -0.194965, -0.0319978))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.44485, 
    farPlane=2.31681, cameraPosition=(-0.939142, -0.0874982, 1.30938), 
    cameraUpVector=(0.290841, 0.923173, -0.251323), cameraTarget=(0.506937, 
    -0.194884, -0.0273472))
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
#* FeatureError: Regeneration failed
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('Cap-Copy-1', 'Top_Flange-Copy-1', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.47023, 
    farPlane=2.54112, width=0.919715, height=0.568641, cameraPosition=(
    -1.05656, -1.06843, 0.648492), cameraUpVector=(-0.0480636, 0.912158, 
    0.40701), cameraTarget=(0.403647, 0.0879496, -0.120346))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.66005, 
    farPlane=2.31791, width=1.03846, height=0.642058, cameraPosition=(0.248902, 
    1.04125, -1.87226), cameraUpVector=(-0.891741, -0.00638084, 0.452501), 
    cameraTarget=(0.397532, 0.0780674, -0.108538))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.58955, 
    farPlane=2.45997, width=0.994359, height=0.614792, cameraPosition=(1.04704, 
    -1.60466, -0.942524), cameraUpVector=(-0.66861, 0.425855, -0.609597), 
    cameraTarget=(0.387061, 0.112779, -0.120735))
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Flange']
a1.Instance(name='Flange-1', part=p, dependent=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.78297, 
    farPlane=3.06782, width=1.06432, height=0.658049, cameraPosition=(2.23914, 
    -1.11233, -1.28238), cameraUpVector=(-0.864637, -0.435045, -0.251275), 
    cameraTarget=(0.420139, -0.0612273, -0.0644124))
a1 = mdb.models['Model-1'].rootAssembly
e1 = a1.instances['Flange-1'].edges
e2 = a1.instances['Long_Side-2'].edges
a1.EdgeToEdge(movableAxis=e1[68], fixedAxis=e2[2], flip=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.95151, 
    farPlane=2.69685, width=1.16493, height=0.720252, cameraPosition=(0.532562, 
    1.95104, -1.53554), cameraUpVector=(-0.650272, -0.656304, -0.382637), 
    cameraTarget=(0.374711, 0.0203171, -0.0711514))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.01543, 
    farPlane=2.63294, width=0.395001, height=0.244221, viewOffsetX=0.218996, 
    viewOffsetY=-0.0699085)
a1 = mdb.models['Model-1'].rootAssembly
e1 = a1.instances['Short Side With Holes-1'].edges
e2 = a1.instances['Flange-1'].edges
a1.EdgeToEdge(movableAxis=e1[5], fixedAxis=e2[76], flip=OFF)
#* FeatureError: The constraint cannot be applied because it conflicts 
#* with existing position constraints.
a = mdb.models['Model-1'].rootAssembly
del a.features['Edge to Edge-1']
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.98092, 
    farPlane=2.92238, width=0.994258, height=0.614729, viewOffsetX=0.391389, 
    viewOffsetY=-0.0960122)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.13883, 
    farPlane=3.12403, width=1.07351, height=0.663732, cameraPosition=(1.37096, 
    1.26248, -2.20582), cameraUpVector=(-0.968941, -0.232337, -0.0846966), 
    cameraTarget=(0.591125, 0.273817, -0.129418), viewOffsetX=0.422588, 
    viewOffsetY=-0.103666)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.11985, 
    farPlane=3.143, width=1.28101, height=0.792023, viewOffsetX=0.445628, 
    viewOffsetY=-0.108156)
a1 = mdb.models['Model-1'].rootAssembly
e1 = a1.instances['Long_Side-2'].edges
e2 = a1.instances['Flange-1'].edges
a1.EdgeToEdge(movableAxis=e1[2], fixedAxis=e2[66], flip=OFF)
#: Warning: The order of fixed and movable entities was swapped to avoid a dependency cycle.
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.78514, 
    farPlane=2.70819, width=1.07875, height=0.66697, cameraPosition=(-0.264055, 
    1.53725, -1.73393), cameraUpVector=(-0.686674, -0.718671, 0.109498), 
    cameraTarget=(0.389133, 0.0635434, 0.0822669), viewOffsetX=0.375268, 
    viewOffsetY=-0.0910794)
a1 = mdb.models['Model-1'].rootAssembly
e1 = a1.instances['Short Side With Holes-1'].edges
e2 = a1.instances['Flange-1'].edges
a1.EdgeToEdge(movableAxis=e1[5], fixedAxis=e2[76], flip=OFF)
#: Warning: The order of fixed and movable entities was swapped to avoid a dependency cycle.
#: The instance "Flange-1" is fully constrained
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.73908, 
    farPlane=2.73911, width=1.84159, height=1.13862, viewOffsetX=0.551493, 
    viewOffsetY=0.0594207)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.52003, 
    farPlane=2.37854, width=1.60962, height=0.995196, cameraPosition=(0.5449, 
    2.0751, -0.456879), cameraUpVector=(-0.899129, -0.387583, 0.203339), 
    cameraTarget=(0.794158, -0.252229, 0.189995), viewOffsetX=0.482027, 
    viewOffsetY=0.0519362)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.6057, 
    farPlane=2.29287, width=0.809225, height=0.500327, viewOffsetX=0.404615, 
    viewOffsetY=0.0696035)
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('Edge to Edge-2', 'Edge to Edge-1', ))
session.viewports['Viewport: 1'].view.setValues(width=0.872881, 
    height=0.539685, viewOffsetX=0.422115, viewOffsetY=0.0712129)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.97462, 
    farPlane=2.71176, width=1.05867, height=0.654556, cameraPosition=(0.447356, 
    1.10521, -2.21285), cameraUpVector=(-0.901036, -0.248367, 0.355596), 
    cameraTarget=(0.668418, 0.317842, 0.0736817), viewOffsetX=0.511962, 
    viewOffsetY=0.0863706)
a1 = mdb.models['Model-1'].rootAssembly
e1 = a1.instances['Long_Side-2'].edges
e2 = a1.instances['Flange-1'].edges
a1.EdgeToEdge(movableAxis=e1[2], fixedAxis=e2[68], flip=ON)
#: Warning: The order of fixed and movable entities was swapped to avoid a dependency cycle.
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.95729, 
    farPlane=2.71256, width=1.04938, height=0.648812, cameraPosition=(
    -0.254531, 0.437518, -2.34964), cameraUpVector=(-0.69784, -0.434074, 
    0.569737), cameraTarget=(0.51181, 0.363635, -0.0465365), 
    viewOffsetX=0.50747, viewOffsetY=0.0856127)
a1 = mdb.models['Model-1'].rootAssembly
e1 = a1.instances['Short Side With Holes-1'].edges
e2 = a1.instances['Flange-1'].edges
a1.EdgeToEdge(movableAxis=e1[5], fixedAxis=e2[76], flip=OFF)
#* FeatureError: The constraint cannot be applied because it conflicts 
#* with existing position constraints.
a1 = mdb.models['Model-1'].rootAssembly
e1 = a1.instances['Flange-1'].edges
e2 = a1.instances['Short Side With Holes-1'].edges
a1.EdgeToEdge(movableAxis=e1[76], fixedAxis=e2[5], flip=OFF)
#* FeatureError: The constraint cannot be applied because it conflicts 
#* with existing position constraints.
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.92429, 
    farPlane=2.66768, width=1.03169, height=0.637872, cameraPosition=(
    -0.0202517, 0.864502, -2.26006), cameraUpVector=(-0.757534, -0.514924, 
    0.401243), cameraTarget=(0.501193, 0.325079, 0.0495158), 
    viewOffsetX=0.498913, viewOffsetY=0.0841691)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.93444, 
    farPlane=2.65752, width=0.990956, height=0.612688, viewOffsetX=0.511649, 
    viewOffsetY=0.0644342)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.93633, 
    farPlane=2.57273, width=0.991922, height=0.613285, cameraPosition=(
    0.850099, 1.42543, -1.97157), cameraUpVector=(-0.914691, 0.0176268, 
    0.403769), cameraTarget=(0.876757, 0.236137, 0.145482), 
    viewOffsetX=0.512148, viewOffsetY=0.064497)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.93603, 
    farPlane=2.57303, width=0.991769, height=0.61319, cameraPosition=(0.719947, 
    1.45269, -1.95462), cameraUpVector=(-0.939085, -0.164602, 0.301706), 
    cameraTarget=(0.746605, 0.263393, 0.162433), viewOffsetX=0.512069, 
    viewOffsetY=0.064487)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.57591, 
    farPlane=2.38111, width=0.807292, height=0.499132, cameraPosition=(
    -0.0767639, 2.03592, -0.416372), cameraUpVector=(-0.698264, -0.628857, 
    -0.342004), cameraTarget=(0.446624, -0.223647, 0.302992), 
    viewOffsetX=0.41682, viewOffsetY=0.0524919)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.6606, 
    farPlane=2.3776, width=0.850675, height=0.525955, cameraPosition=(0.185605, 
    2.07415, -0.668827), cameraUpVector=(-0.811924, -0.558005, -0.171494), 
    cameraTarget=(0.472132, -0.108473, 0.35641), viewOffsetX=0.439219, 
    viewOffsetY=0.0553127)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.64227, 
    farPlane=2.73292, width=0.841286, height=0.52015, cameraPosition=(2.45346, 
    0.92179, 0.0647905), cameraUpVector=(-0.541772, 0.572505, -0.615403), 
    cameraTarget=(0.123875, 0.244309, 0.170071), viewOffsetX=0.434371, 
    viewOffsetY=0.0547022)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.81785, 
    farPlane=2.83958, width=0.931232, height=0.575762, cameraPosition=(2.26667, 
    0.655508, -1.45745), cameraUpVector=(-0.762745, 0.625765, -0.163213), 
    cameraTarget=(0.548418, 0.29209, 0.21962), viewOffsetX=0.480812, 
    viewOffsetY=0.0605507)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Flange-1'].faces
f2 = a1.instances['Short Side With Holes-1'].faces
a1.FaceToFace(movablePlane=f1[28], fixedPlane=f2[0], flip=OFF, clearance=0.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.09924, 
    farPlane=2.96583, width=1.07538, height=0.664885, cameraPosition=(1.53573, 
    -1.63296, -1.61267), cameraUpVector=(-0.396904, 0.725136, -0.562713), 
    cameraTarget=(0.857284, 0.215188, -0.191017), viewOffsetX=0.555237, 
    viewOffsetY=0.0699234)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.0314, 
    farPlane=3.03367, width=1.81612, height=1.12287, viewOffsetX=0.722088, 
    viewOffsetY=0.0182521)
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Cap']
a1.Instance(name='Cap-1', part=p, dependent=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.81958, 
    farPlane=3.05676, width=1.11427, height=0.688933, cameraPosition=(2.61624, 
    -0.513743, 0.764742), cameraUpVector=(0.0380481, 0.123579, -0.991605))
a1 = mdb.models['Model-1'].rootAssembly
e1 = a1.instances['Flange-1'].edges
e2 = a1.instances['Cap-1'].edges
a1.EdgeToEdge(movableAxis=e1[9], fixedAxis=e2[10], flip=OFF)
#: Warning: The order of fixed and movable entities was swapped to avoid a dependency cycle.
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.83081, 
    farPlane=3.11849, width=1.12115, height=0.693184, cameraPosition=(1.74763, 
    -2.00678, 0.473015), cameraUpVector=(0.017465, 0.146427, -0.989067), 
    cameraTarget=(0.378973, -0.0914116, -0.0827731))
a1 = mdb.models['Model-1'].rootAssembly
e1 = a1.instances['Flange-1'].edges
e2 = a1.instances['Cap-1'].edges
a1.EdgeToEdge(movableAxis=e1[14], fixedAxis=e2[15], flip=OFF)
#: Warning: The order of fixed and movable entities was swapped to avoid a dependency cycle.
#: The instance "Cap-1" is fully constrained
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.04129, 
    farPlane=3.15102, width=1.60109, height=0.989919, viewOffsetX=0.0473549, 
    viewOffsetY=0.0355542)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.82766, 
    farPlane=3.04388, width=1.43353, height=0.88632, cameraPosition=(2.70562, 
    0.68856, 0.279879), cameraUpVector=(-0.410196, 0.605333, -0.682137), 
    cameraTarget=(0.397274, 0.0581313, -0.0734423), viewOffsetX=0.042399, 
    viewOffsetY=0.0318333)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.85916, 
    farPlane=3.02611, width=1.45823, height=0.901597, cameraPosition=(2.13119, 
    0.941408, -1.60174), cameraUpVector=(-0.880796, -0.0114374, -0.473359), 
    cameraTarget=(0.423669, 0.103264, -0.107541), viewOffsetX=0.0431297, 
    viewOffsetY=0.0323819)
p1 = mdb.models['Model-1'].parts['Cap']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=2.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.ConstructionLine(point1=(0.0, -1.0), point2=(0.0, 1.0))
s.FixedConstraint(entity=g[2])
s.Line(point1=(0.0, 0.0), point2=(0.0, 0.143114984035492))
s.VerticalConstraint(entity=g[3], addUndoState=False)
s.ParallelConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
s.CoincidentConstraint(entity1=v[0], entity2=g[2], addUndoState=False)
s.CoincidentConstraint(entity1=v[1], entity2=g[2], addUndoState=False)
s.Line(point1=(0.0, 0.143114984035492), point2=(-0.0375000000465661, 
    0.143114984035492))
s.HorizontalConstraint(entity=g[4], addUndoState=False)
s.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
s.Line(point1=(-0.0375000000465661, 0.143114984035492), point2=(
    -0.0375000000465665, 0.175000000023283))
s.VerticalConstraint(entity=g[5], addUndoState=False)
s.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
s.Line(point1=(-0.0375000000465665, 0.175000000023283), point2=(
    0.0874999999534339, 0.175000000023282))
s.HorizontalConstraint(entity=g[6], addUndoState=False)
s.PerpendicularConstraint(entity1=g[5], entity2=g[6], addUndoState=False)
s.Line(point1=(0.0874999999534339, 0.175000000023282), point2=(
    0.0874999999534335, 0.15))
s.VerticalConstraint(entity=g[7], addUndoState=False)
s.PerpendicularConstraint(entity1=g[6], entity2=g[7], addUndoState=False)
s.Line(point1=(0.0874999999534335, 0.15), point2=(0.0375000000931323, 0.15))
s.HorizontalConstraint(entity=g[8], addUndoState=False)
s.PerpendicularConstraint(entity1=g[7], entity2=g[8], addUndoState=False)
s.Line(point1=(0.0375000000931323, 0.15), point2=(0.0375000000931323, 
    -0.137499999953434))
s.VerticalConstraint(entity=g[9], addUndoState=False)
s.PerpendicularConstraint(entity1=g[8], entity2=g[9], addUndoState=False)
s.Line(point1=(0.0375000000931323, -0.137499999953434), point2=(
    0.0749999999767169, -0.137499999953434))
s.HorizontalConstraint(entity=g[10], addUndoState=False)
s.PerpendicularConstraint(entity1=g[9], entity2=g[10], addUndoState=False)
s.Line(point1=(0.0749999999767169, -0.137499999953434), point2=(
    0.0749999999767176, -0.175000000023283))
s.VerticalConstraint(entity=g[11], addUndoState=False)
s.PerpendicularConstraint(entity1=g[10], entity2=g[11], addUndoState=False)
s.Line(point1=(0.0749999999767176, -0.175000000023283), point2=(
    0.0375000000465661, -0.175000000023282))
s.HorizontalConstraint(entity=g[12], addUndoState=False)
s.PerpendicularConstraint(entity1=g[11], entity2=g[12], addUndoState=False)
s.Line(point1=(0.0375000000465661, -0.175000000023282), point2=(
    0.0375000000465683, -0.2))
s.VerticalConstraint(entity=g[13], addUndoState=False)
s.PerpendicularConstraint(entity1=g[12], entity2=g[13], addUndoState=False)
s.Line(point1=(0.0375000000465683, -0.2), point2=(0.0, -0.2))
s.HorizontalConstraint(entity=g[14], addUndoState=False)
s.PerpendicularConstraint(entity1=g[13], entity2=g[14], addUndoState=False)
s.CoincidentConstraint(entity1=v[12], entity2=g[2], addUndoState=False)
s.Line(point1=(0.0, -0.2), point2=(0.0, -0.170151144266129))
s.VerticalConstraint(entity=g[15], addUndoState=False)
s.PerpendicularConstraint(entity1=g[14], entity2=g[15], addUndoState=False)
s.CoincidentConstraint(entity1=v[13], entity2=g[2], addUndoState=False)
s.Line(point1=(0.0, -0.170151144266129), point2=(-0.0249999999534339, 
    -0.170151144266129))
s.HorizontalConstraint(entity=g[16], addUndoState=False)
s.PerpendicularConstraint(entity1=g[15], entity2=g[16], addUndoState=False)
s.Line(point1=(-0.0249999999534339, -0.170151144266129), point2=(
    -0.0249999999534335, -0.137499999976717))
s.VerticalConstraint(entity=g[17], addUndoState=False)
s.PerpendicularConstraint(entity1=g[16], entity2=g[17], addUndoState=False)
s.Line(point1=(-0.0249999999534335, -0.137499999976717), point2=(0.0, 
    -0.137499999979627))
s.HorizontalConstraint(entity=g[18], addUndoState=False)
s.CoincidentConstraint(entity1=v[16], entity2=g[2], addUndoState=False)
s.Line(point1=(0.0, -0.137499999979627), point2=(0.0, 0.0))
s.VerticalConstraint(entity=g[19], addUndoState=False)
s.PerpendicularConstraint(entity1=g[18], entity2=g[19], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.80296, 
    farPlane=1.96828, width=0.883943, height=0.546524, cameraPosition=(
    0.00622272, 0.0212095, 1.88562), cameraTarget=(0.00622272, 0.0212095, 0))
s.undo()
s.undo()
s.undo()
s.undo()
s.undo()
s.undo()
s.delete(objectList=(g[2], ))
s.delete(objectList=(g[4], ))
s.delete(objectList=(g[3], ))
s.delete(objectList=(g[5], ))
s.delete(objectList=(g[6], ))
s.Line(point1=(0.0874999999534339, 0.175000000023282), point2=(
    0.0124999999767169, 0.175000000023282))
s.HorizontalConstraint(entity=g[14], addUndoState=False)
s.PerpendicularConstraint(entity1=g[7], entity2=g[14], addUndoState=False)
s.Line(point1=(0.0124999999767169, 0.175000000023282), point2=(
    0.0124999999767176, -0.2))
s.VerticalConstraint(entity=g[15], addUndoState=False)
s.PerpendicularConstraint(entity1=g[14], entity2=g[15], addUndoState=False)
s.Line(point1=(0.0124999999767176, -0.2), point2=(0.0375000000465683, -0.2))
s.HorizontalConstraint(entity=g[16], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.81258, 
    farPlane=1.95866, width=0.883944, cameraPosition=(0.1024, -0.0344456, 
    1.88562), cameraTarget=(0.1024, -0.0344456, 0))
s.ObliqueDimension(vertex1=v[13], vertex2=v[11], textPoint=(0.0264678597450256, 
    -0.218685314059258), value=0.01)
s.Line(point1=(0.0375000000931323, 0.15), point2=(0.0124999999650754, 0.15))
s.HorizontalConstraint(entity=g[17], addUndoState=False)
s.ParallelConstraint(entity1=g[8], entity2=g[17], addUndoState=False)
s.CoincidentConstraint(entity1=v[14], entity2=g[15], addUndoState=False)
s.setAsConstruction(objectList=(g[17], ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.83482, 
    farPlane=1.93642, width=0.543242, height=0.335876, cameraPosition=(
    0.104243, -0.0922375, 1.88562), cameraTarget=(0.104243, -0.0922375, 0))
s.undo()
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.83959, 
    farPlane=1.93165, width=0.492196, height=0.304315, cameraPosition=(
    0.0938311, -0.168798, 1.88562), cameraTarget=(0.0938311, -0.168798, 0))
s.EqualLengthConstraint(entity1=g[17], entity2=g[16])
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.82239, 
    farPlane=1.94885, width=0.676153, height=0.418052, cameraPosition=(
    0.140728, -0.202512, 1.88562), cameraTarget=(0.140728, -0.202512, 0))
s.dragEntity(entity=v[8], points=((0.0749999999767169, -0.137499999953434), (
    0.075, -0.1375), (0.0625, -0.1375), (0.05, -0.143015787005424), (0.05, 
    -0.145121827721596), (0.05, -0.15), (0.0450813621282578, -0.15), (0.05, 
    -0.15), (0.05, -0.15), (0.0564452856779099, -0.15)))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.8043, 
    farPlane=1.96694, width=0.869575, height=0.53764, cameraPosition=(0.162533, 
    -0.00885834, 1.88562), cameraTarget=(0.162533, -0.00885834, 0))
s.dragEntity(entity=v[6], points=((0.0224999999650754, 0.15), (0.025, 0.15), (
    0.025, 0.1375), (0.025, 0.1375), (0.0375, 0.1375), (0.0375, 0.1375), (0.05, 
    0.15), (0.0375, 0.15), (0.0375, 0.1375), (0.05, 0.1375), (0.05, 0.1375), (
    0.0375, 0.1375), (0.025, 0.1375), (0.025, 0.1375)))
s.DistanceDimension(entity1=g[8], entity2=g[10], textPoint=(0.129243612289429, 
    -0.00502128899097443), value=0.0254)
s.dragEntity(entity=v[11], points=((0.0250000000116422, -0.2), (0.025, -0.2), (
    0.0375, -0.1125), (0.0375, -0.075), (0.0375, -0.05), (0.025, -0.0125), (
    0.025, -0.0125), (0.025, -0.0312036126852036), (0.0125, -0.0625), (0.0125, 
    -0.05), (0.0125, -0.0375)))
s.dragEntity(entity=v[9], points=((0.0564452856546274, -0.175000000023283), (
    0.0564452856546274, -0.175), (0.05, -0.025), (0.0375, 0.0375), (0.0375, 
    0.05), (0.0375, 0.075), (0.025, 0.0875), (0.025, 0.0875), (0.025, 0.075), (
    0.025, 0.075), (0.0125, 0.05), (0.0125, 0.025), (0.0125, 0.0), (0.0125, 
    -0.0125), (0.025, -0.0125), (0.0375, -0.0125), (0.0375, -0.0125)))
s.dragEntity(entity=v[8], points=((0.0375000000232862, 0.112099999976717), (
    0.0375, 0.1125), (0.0375, 0.0875), (0.0375, 0.075), (0.0375, 0.0625), (
    0.0375, 0.05), (0.0375, 0.05)))
s.dragEntity(entity=v[4], points=((0.0874999999534339, 0.175000000023282), (
    0.0875, 0.175), (0.075, 0.15), (0.075, 0.15), (0.0625, 0.1375), (0.0625, 
    0.125), (0.05, 0.1125), (0.05, 0.1), (0.05, 0.1), (0.05, 0.1), (0.05, 
    0.1)))
s.dragEntity(entity=v[11], points=((0.0125, -0.0375), (0.0125, -0.0375), (
    0.0125, -0.0125), (0.0125, -0.0125), (0.0125, 0.0), (0.0125, 0.0)))
s.dragEntity(entity=v[9], points=((0.0375, -0.0125), (0.0375, -0.0125), (
    0.0375, 0.0125), (0.025, 0.0125), (0.025, 0.025), (0.025, 0.025), (0.025, 
    0.0375), (0.0375, 0.0375)))
s.dragEntity(entity=v[11], points=((0.0125, 0.0), (0.0125, 0.0), (0.0125, 
    0.0125), (0.0125, 0.0125), (0.0125, 0.025)))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.86052, 
    farPlane=1.91072, width=0.268371, height=0.165929, cameraPosition=(
    0.0551724, 0.0494285, 1.88562), cameraTarget=(0.0551724, 0.0494285, 0))
s.dragEntity(entity=v[8], points=((0.0375, 0.05), (0.0375, 0.05), (
    0.0293626226484776, 0.05), (0.025, 0.0468511432409286), (0.025, 
    0.0453186333179474), (0.025, 0.0467118173837662), (0.025, 
    0.0478263720870018), (0.0228475369513035, 0.05), (0.022722240537405, 
    0.05)))
s.dragEntity(entity=v[5], points=((0.05, 0.0754000000232836), (0.05, 0.075), (
    0.0375, 0.0786158069968224), (0.0339983515441418, 0.0784764885902405), (
    0.0302396453917027, 0.0780585333704948), (0.0301143564283848, 
    0.0777798965573311), (0.0276085548102856, 0.0769439786672592), (0.025, 
    0.075), (0.025, 0.0793124064803123), (0.025, 0.0812628641724586), (0.025, 
    0.0825167298316956)))
s.dragEntity(entity=v[10], points=((0.0125000000116539, 0.0374999999767159), (
    0.0125, 0.0375), (0.0125, 0.0419749841094017), (0.0125, 
    0.0432288572192192)))
s.dragEntity(entity=v[11], points=((0.0125, 0.025), (0.0125, 0.025), (0.0125, 
    0.0291576683521271), (0.0125, 0.0305508524179459), (0.0125, 
    0.0309688076376915)))
s.setAsConstruction(objectList=(g[17], ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.84146, 
    farPlane=1.92978, width=0.472206, height=0.291956, cameraPosition=(
    0.0793074, 0.0800185, 1.88562), cameraTarget=(0.0793074, 0.0800185, 0))
s.dragEntity(entity=v[12], points=((0.00250000001164169, 0.1), (0.0, 0.1), (
    0.0, 0.0965651497244835), (0.0, 0.1)))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.86032, 
    farPlane=1.91092, width=0.270572, height=0.167289, cameraPosition=(
    0.048396, 0.0754652, 1.88562), cameraTarget=(0.048396, 0.0754652, 0))
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
p1 = mdb.models['Model-1'].parts['Bottom']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=2.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
s1.ConstructionLine(point1=(0.0, -1.0), point2=(0.0, 1.0))
s1.FixedConstraint(entity=g[2])
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.86689, 
    farPlane=1.90434, width=0.200213, height=0.123788, cameraPosition=(
    0.0035985, -0.000640035, 1.88562), cameraTarget=(0.0035985, -0.000640035, 
    0))
s1.Line(point1=(0.0, 0.0269549936056137), point2=(0.0124999999767169, 
    0.0269549936056137))
s1.HorizontalConstraint(entity=g[3], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
s1.CoincidentConstraint(entity1=v[0], entity2=g[2], addUndoState=False)
s1.Line(point1=(0.0124999999767169, 0.0269549936056137), point2=(
    0.0124999999767169, 0.0224857404828072))
s1.VerticalConstraint(entity=g[4], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
s1.Line(point1=(0.0124999999767169, 0.0224857404828072), point2=(
    0.00546790193766356, 0.0224857404828072))
s1.HorizontalConstraint(entity=g[5], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
s1.Line(point1=(0.00546790193766356, 0.0224857404828072), point2=(
    0.00546790193766356, 0.00949373096227646))
s1.VerticalConstraint(entity=g[6], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[5], entity2=g[6], addUndoState=False)
s1.Line(point1=(0.00546790193766356, 0.00949373096227646), point2=(
    0.0124999999767169, 0.00949373096227646))
s1.HorizontalConstraint(entity=g[7], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[6], entity2=g[7], addUndoState=False)
s1.Line(point1=(0.0124999999767169, 0.00949373096227646), point2=(
    0.0124999999767169, 0.00450479984283447))
s1.VerticalConstraint(entity=g[8], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[7], entity2=g[8], addUndoState=False)
s1.Line(point1=(0.0124999999767169, 0.00450479984283447), point2=(
    0.00556136947125196, 0.00450479984283447))
s1.HorizontalConstraint(entity=g[9], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[8], entity2=g[9], addUndoState=False)
s1.Line(point1=(0.00556136947125196, 0.00450479984283447), point2=(
    0.00556136947125196, 0.0))
s1.VerticalConstraint(entity=g[10], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[9], entity2=g[10], addUndoState=False)
s1.Line(point1=(0.00556136947125196, 0.0), point2=(0.0, 0.0))
s1.HorizontalConstraint(entity=g[11], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[10], entity2=g[11], addUndoState=False)
s1.CoincidentConstraint(entity1=v[9], entity2=g[2], addUndoState=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.87614, 
    farPlane=1.8951, width=0.101368, height=0.0626736, cameraPosition=(
    0.00328652, 0.00770011, 1.88562), cameraTarget=(0.00328652, 0.00770011, 0))
s1.EqualLengthConstraint(entity1=g[5], entity2=g[7])
s1.EqualLengthConstraint(entity1=g[7], entity2=g[9], addUndoState=False)
s1.EqualLengthConstraint(entity1=g[8], entity2=g[4])
s1.Line(point1=(0.00546790193766356, 0.0224857404828072), point2=(0.0, 
    0.0224857404828072))
s1.HorizontalConstraint(entity=g[12], addUndoState=False)
s1.ParallelConstraint(entity1=g[5], entity2=g[12], addUndoState=False)
s1.CoincidentConstraint(entity1=v[10], entity2=g[2], addUndoState=False)
s1.DistanceDimension(entity1=g[5], entity2=g[7], textPoint=(0.0200864914804697, 
    0.0160934273153543), value=0.0254)
s1.dragEntity(entity=g[11], points=((0.00319187133572996, 0.0), (
    0.00319187133572996, 0.0), (0.00309721915982664, -0.00563973933458328), (
    0.0031445452477783, -0.00874447636306286), (0.00309721915982664, 
    -0.0101652890443802), (0.00300257443450391, -0.0125), (0.00304990052245557, 
    -0.0136910080909729)))
s1.setAsConstruction(objectList=(g[12], g[11]))
s1.undo()
s1.EqualLengthConstraint(entity1=g[12], entity2=g[11])
s1.setAsConstruction(objectList=(g[12], ))
s1.ObliqueDimension(vertex1=v[8], vertex2=v[9], textPoint=(0.00347581296227872, 
    -0.0163747649639845), value=0.005)
s1.Line(point1=(0.0, 0.0274746716022492), point2=(0.0, -0.0136910080909729))
s1.VerticalConstraint(entity=g[13], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[3], entity2=g[13], addUndoState=False)
s1.sketchOptions.setValues(constructionGeometry=ON)
s1.assignCenterline(line=g[2])
p = mdb.models['Model-1'].Part(name='Bolt', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Bolt']
p.BaseSolidRevolve(sketch=s1, angle=360.0, flipRevolveDirection=OFF)
s1.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Bolt']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0857011, 
    farPlane=0.157554, width=0.0934849, height=0.0577998, 
    viewOffsetX=0.00474244, viewOffsetY=-0.00167641)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0882397, 
    farPlane=0.145289, width=0.0962541, height=0.059512, cameraPosition=(
    -0.0163901, 0.0375007, 0.11152), cameraUpVector=(-0.441447, 0.663243, 
    -0.604345), cameraTarget=(-0.00119337, 0.00329494, -0.00420436), 
    viewOffsetX=0.00488292, viewOffsetY=-0.00172607)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Bolt']
a1.Instance(name='Bolt-1', part=p, dependent=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.58346, 
    farPlane=2.59231, width=1.08632, height=0.671647, cameraPosition=(
    -0.418275, -1.14625, -1.58672), cameraUpVector=(0.0190332, 0.945057, 
    -0.326352), cameraTarget=(0.393048, 0.0760366, -0.119271))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.48115, 
    farPlane=2.66538, width=1.01613, height=0.628253, cameraPosition=(-1.43931, 
    -0.718504, -0.693106), cameraUpVector=(0.221521, 0.782813, -0.581491), 
    cameraTarget=(0.386747, 0.0786763, -0.113756))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.50973, 
    farPlane=2.64067, width=1.03574, height=0.640375, cameraPosition=(-1.03981, 
    -0.808081, -1.33185), cameraUpVector=(0.243962, 0.896332, -0.370232), 
    cameraTarget=(0.386412, 0.0787514, -0.113221))
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Bolt']
a1.Instance(name='Bolt-2', part=p, dependent=ON)
p1 = a1.instances['Bolt-2']
p1.translate(vector=(0.800010282046925, 0.0, 0.0))
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.55392, 
    farPlane=2.6692, width=0.809762, height=0.50066, cameraPosition=(-1.0802, 
    -0.784187, -1.34779), cameraUpVector=(-0.16944, 0.984293, 0.0495811), 
    cameraTarget=(0.371153, 0.118269, -0.107692))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.66141, 
    farPlane=2.54514, width=0.865775, height=0.535291, cameraPosition=(1.06883, 
    -1.86642, -0.289185), cameraUpVector=(-0.482711, 0.261388, -0.835863), 
    cameraTarget=(0.371153, 0.118269, -0.107692))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.54349, 
    farPlane=2.63996, width=0.804326, height=0.497298, cameraPosition=(2.42416, 
    0.575166, -0.0434154), cameraUpVector=(-0.192423, -0.54566, -0.815616), 
    cameraTarget=(0.365813, 0.108648, -0.10866))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.53184, 
    farPlane=2.66244, width=0.798256, height=0.493546, cameraPosition=(1.86341, 
    -1.26436, 0.433113), cameraUpVector=(0.0399215, 0.161641, -0.986042), 
    cameraTarget=(0.37113, 0.126091, -0.113178))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.56173, 
    farPlane=2.63256, width=0.496087, height=0.30672, viewOffsetX=-0.0805481, 
    viewOffsetY=0.00588581)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.68082, 
    farPlane=2.35641, width=0.533917, height=0.33011, cameraPosition=(0.463994, 
    -1.65904, -1.08264), cameraUpVector=(-0.694765, 0.592356, -0.407941), 
    cameraTarget=(0.383939, 0.165357, -0.0225182), viewOffsetX=-0.0866906, 
    viewOffsetY=0.00633465)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.55638, 
    farPlane=2.54835, width=0.494389, height=0.305671, cameraPosition=(1.36238, 
    -1.30183, -1.24054), cameraUpVector=(-0.730384, 0.424365, -0.535214), 
    cameraTarget=(0.347538, 0.11449, -0.0477126), viewOffsetX=-0.0802726, 
    viewOffsetY=0.00586567)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.50828, 
    farPlane=2.59646, width=1.01911, height=0.630094, viewOffsetX=0.00141342, 
    viewOffsetY=-0.0466339)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-2'].faces
f2 = a1.instances['Cap-1'].faces
a1.Coaxial(movableAxis=f1[3], fixedAxis=f2[6], flip=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.7447, 
    farPlane=2.56257, width=1.17885, height=0.728859, cameraPosition=(0.310257, 
    -1.63457, 1.13277), cameraUpVector=(0.130919, -0.287336, -0.94884), 
    cameraTarget=(0.422437, 0.069213, -0.109497), viewOffsetX=0.00163497, 
    viewOffsetY=-0.0539436)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.74195, 
    farPlane=2.56531, width=1.1109, height=0.686846, viewOffsetX=-0.0295912, 
    viewOffsetY=-0.0578548)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.64239, 
    farPlane=2.58632, width=1.04741, height=0.647591, cameraPosition=(0.827676, 
    -1.29856, -1.62674), cameraUpVector=(-0.466117, 0.779397, -0.418658), 
    cameraTarget=(0.398369, 0.14353, -0.145266), viewOffsetX=-0.0279001, 
    viewOffsetY=-0.0545483)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-2'].faces
f2 = a1.instances['Cap-1'].faces
a1.FaceToFace(movablePlane=f1[2], fixedPlane=f2[37], flip=ON, clearance=0.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.62341, 
    farPlane=2.70998, width=1.0353, height=0.640107, cameraPosition=(1.75157, 
    -1.55191, -0.0104499), cameraUpVector=(-0.124253, 0.232906, -0.964529), 
    cameraTarget=(0.438405, 0.0935901, -0.173667), viewOffsetX=-0.0275776, 
    viewOffsetY=-0.0539178)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.68642, 
    farPlane=2.64698, width=0.312005, height=0.192906, viewOffsetX=-0.0317401, 
    viewOffsetY=0.0482765)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.70851, 
    farPlane=2.65354, width=0.316092, height=0.195433, cameraPosition=(1.7193, 
    -1.58899, -0.319942), cameraUpVector=(-0.21688, 0.331065, -0.918346), 
    cameraTarget=(0.443166, 0.0875488, -0.180592), viewOffsetX=-0.0321559, 
    viewOffsetY=0.0489088)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.70818, 
    farPlane=2.65387, width=0.316032, height=0.195396, cameraPosition=(1.69165, 
    -1.60516, -0.378604), cameraUpVector=(0.390139, 0.759986, -0.51982), 
    cameraTarget=(0.415512, 0.0713751, -0.239254), viewOffsetX=-0.0321498, 
    viewOffsetY=0.0488994)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.64761, 
    farPlane=2.57647, width=0.304826, height=0.188468, cameraPosition=(1.2588, 
    -1.62302, 0.689538), cameraUpVector=(0.721935, 0.56068, -0.405521), 
    cameraTarget=(0.400679, 0.0758422, -0.224901), viewOffsetX=-0.0310098, 
    viewOffsetY=0.0471655)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.64858, 
    farPlane=2.5755, width=0.305005, height=0.188579, cameraPosition=(1.25224, 
    -1.6157, 0.709297), cameraUpVector=(0.656895, 0.40315, -0.637149), 
    cameraTarget=(0.394116, 0.0831631, -0.205142), viewOffsetX=-0.031028, 
    viewOffsetY=0.0471932)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.63851, 
    farPlane=2.58557, width=0.394893, height=0.244154, viewOffsetX=0.0672407, 
    viewOffsetY=0.141257)
a = mdb.models['Model-1'].rootAssembly
p1 = a.instances['Flange-1']
p1.getPosition()
#: 
#: The instance position relative to the Assembly CS is: -0.04251, 0.306885, -0.268125
#: The instance 'Flange-1' is partially constrained with 0 unconstrained translations and 1 unconstrained rotations
#: Constraints: Edge to Edge-1, Face to Face-1
#: Instance: "Flange-1", Modeling space: 3D,  Type: Deformable, Dependent
#: 
#: Point 1: 578.13E-03, -75.635E-03, -255.125E-03  Point 2: 578.13E-03, -75.635E-03, -280.825E-03
#:    Distance: 25.7E-03  Components: 0., 0., -25.7E-03
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.56527, 
    farPlane=2.65881, width=1.32177, height=0.817222, viewOffsetX=0.186482, 
    viewOffsetY=0.126537)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.03974, 
    farPlane=2.88623, width=1.72242, height=1.06494, cameraPosition=(0.396259, 
    -1.81148, -1.66341), cameraUpVector=(0.894472, 0.44654, 0.0228401), 
    cameraTarget=(0.358623, -0.23152, -0.26304), viewOffsetX=0.243009, 
    viewOffsetY=0.164893)
p1 = mdb.models['Model-1'].parts['Bolt']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['Bolt']
s = p.features['Solid revolve-1'].sketch
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=s)
s2 = mdb.models['Model-1'].sketches['__edit__']
g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
s2.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s2, 
    upToFeature=p.features['Solid revolve-1'], filter=COPLANAR_EDGES)
d[0].setValues(value=0.0258, )
s2.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Bolt']
p.features['Solid revolve-1'].setValues(sketch=s2)
del mdb.models['Model-1'].sketches['__edit__']
p = mdb.models['Model-1'].parts['Bolt']
p.regenerate()
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0795152, 
    farPlane=0.149006, width=0.0867372, height=0.0536279, cameraPosition=(
    -0.0775865, -0.0446476, 0.0663759), cameraUpVector=(-0.411746, 0.777387, 
    -0.475536), cameraTarget=(0.00472086, 0.00587162, -0.00755933), 
    viewOffsetX=0.00440013, viewOffsetY=-0.00155541)
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.89132, 
    farPlane=2.80237, width=1.59709, height=0.987448, cameraPosition=(0.769347, 
    -2.20355, -0.0942663), cameraUpVector=(0.828605, 0.495472, -0.260616), 
    cameraTarget=(0.416845, -0.125611, 0.0348059), viewOffsetX=0.225326, 
    viewOffsetY=0.152894)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.03289, 
    farPlane=2.88881, width=1.71664, height=1.06136, cameraPosition=(0.477872, 
    -1.37514, -2.09604), cameraUpVector=(0.78398, 0.620628, 0.0140059), 
    cameraTarget=(0.468103, -0.269321, -0.297199), viewOffsetX=0.242192, 
    viewOffsetY=0.164338)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.87601, 
    farPlane=3.0532, width=1.58416, height=0.979456, cameraPosition=(-1.13993, 
    0.282353, -2.07849), cameraUpVector=(0.943446, 0.202051, -0.262842), 
    cameraTarget=(0.137942, -0.0600992, -0.432726), viewOffsetX=0.223502, 
    viewOffsetY=0.151656)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p1 = mdb.models['Model-1'].parts['Bolt']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['Bolt']
p.seedPart(size=0.0035, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Bolt']
c = p.cells
pickedRegions = c.getSequenceFromMask(mask=('[#1 ]', ), )
p.setMeshControls(regions=pickedRegions, elemShape=HEX_DOMINATED, 
    technique=SYSTEM_ASSIGN)
p = mdb.models['Model-1'].parts['Bolt']
c = p.cells
pickedRegions = c.getSequenceFromMask(mask=('[#1 ]', ), )
p.setMeshControls(regions=pickedRegions, elemShape=TET, technique=FREE)
elemType1 = mesh.ElemType(elemCode=C3D20R)
elemType2 = mesh.ElemType(elemCode=C3D15)
elemType3 = mesh.ElemType(elemCode=C3D10)
p = mdb.models['Model-1'].parts['Bolt']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
pickedRegions =(cells, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
    elemType3))
p = mdb.models['Model-1'].parts['Bolt']
p.generateMesh()
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0784881, 
    farPlane=0.150845, width=0.0856168, height=0.0530342, cameraPosition=(
    0.0112162, 0.0960029, 0.0713587), cameraUpVector=(-0.00698936, 0.324208, 
    -0.94596), cameraTarget=(-0.00401748, 0.00156216, -0.00375451), 
    viewOffsetX=0.00434329, viewOffsetY=-0.00153532)
p = mdb.models['Model-1'].parts['Bolt']
p.deleteMesh()
p = mdb.models['Model-1'].parts['Bolt']
p.seedPart(size=0.007, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Bolt']
p.generateMesh()
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0841714, 
    farPlane=0.152945, width=0.0918164, height=0.0568744, cameraPosition=(
    0.0498847, -0.0500312, 0.0914026), cameraUpVector=(-0.281138, 0.910875, 
    0.302108), cameraTarget=(-0.00600985, 0.00754122, 5.98142e-07), 
    viewOffsetX=0.00465779, viewOffsetY=-0.00164649)
p1 = mdb.models['Model-1'].parts['Cap']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['Cap']
p.seedPart(size=0.021, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Cap']
p.generateMesh()
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.28032, 
    farPlane=2.36665)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.56864, 
    farPlane=2.07832, cameraPosition=(0.736654, 0.464508, 1.67692), 
    cameraUpVector=(0.415836, 0.602895, -0.68088), cameraTarget=(0.41376, 
    -0.19126, 0.00634998))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.64443, 
    farPlane=2.00254, cameraPosition=(0.575809, -0.468351, 1.80136), 
    cameraUpVector=(0.385036, 0.892313, -0.235637), cameraTarget=(0.41376, 
    -0.19126, 0.00634995))
p = mdb.models['Model-1'].parts['Cap']
c = p.cells
pickedRegions = c.getSequenceFromMask(mask=('[#1 ]', ), )
p.deleteMesh(regions=pickedRegions)
p = mdb.models['Model-1'].parts['Cap']
c = p.cells
pickedRegions = c.getSequenceFromMask(mask=('[#1 ]', ), )
p.setMeshControls(regions=pickedRegions, elemShape=HEX_DOMINATED)
p = mdb.models['Model-1'].parts['Cap']
p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Cap']
p.generateMesh()
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.54, 
    farPlane=2.10697, cameraPosition=(0.839506, -0.899103, 1.63202), 
    cameraUpVector=(0.204663, 0.978832, -0.0012942), cameraTarget=(0.41376, 
    -0.19126, 0.00634994))
p1 = mdb.models['Model-1'].parts['Flange']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['Flange']
p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Flange']
c = p.cells
pickedRegions = c.getSequenceFromMask(mask=('[#1 ]', ), )
p.setMeshControls(regions=pickedRegions, elemShape=HEX_DOMINATED)
p = mdb.models['Model-1'].parts['Flange']
p.generateMesh()
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.69978, 
    farPlane=2.0248, width=0.99946, height=0.619102, viewOffsetX=0.0354692, 
    viewOffsetY=0.00456831)
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.85929, 
    farPlane=2.81609, width=1.57005, height=0.970729, cameraPosition=(0.400916, 
    -2.07603, 0.789727), cameraUpVector=(0.0112016, 0.0160242, -0.999809), 
    cameraTarget=(0.717829, -0.0983669, 0.121005), viewOffsetX=0.221511, 
    viewOffsetY=0.150305)
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('Edge to Edge-7', 'Edge to Edge-4', 'Edge to Edge-5', 
    'Edge to Edge-6', ))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
del mdb.models['Model-1'].constraints['Cap to flange']
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.68009, 
    farPlane=2.85747, width=1.41873, height=0.877172, cameraPosition=(-1.36821, 
    -0.0878839, -1.60496), cameraUpVector=(0.862744, 0.222429, -0.45409), 
    cameraTarget=(0.212522, -0.207049, -0.210025), viewOffsetX=0.200162, 
    viewOffsetY=0.135819)
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'Short Side With Holes-1', 'Long_Side-1', 'Short Side-1', 'Long_Side-2', 
    'Bottom-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'Bolt-2', 'Cap-1', 'Bolt-1', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.68555, 
    farPlane=2.81344, width=1.42334, height=0.880023, cameraPosition=(-1.18746, 
    1.1623, -1.41527), cameraUpVector=(0.889244, -0.0618939, -0.453227), 
    cameraTarget=(0.0999292, -0.0629339, -0.275004), viewOffsetX=0.200813, 
    viewOffsetY=0.13626)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.72045, 
    farPlane=2.77856, width=1.00225, height=0.619671, viewOffsetX=0.169422, 
    viewOffsetY=0.123995)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.88126, 
    farPlane=2.77347, width=1.09593, height=0.677593, cameraPosition=(
    -0.358883, -1.89359, -1.089), cameraUpVector=(0.788318, 0.386397, 
    -0.478803), cameraTarget=(0.344508, -0.203326, -0.0368529), 
    viewOffsetX=0.185259, viewOffsetY=0.135585)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.9254, 
    farPlane=2.74815, width=1.12165, height=0.693492, cameraPosition=(0.914271, 
    -2.0794, -0.774893), cameraUpVector=(0.679858, 0.667251, -0.304253), 
    cameraTarget=(0.438414, -0.179687, 0.0146813), viewOffsetX=0.189606, 
    viewOffsetY=0.138766)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.75018, 
    farPlane=2.8888, width=1.01957, height=0.630382, cameraPosition=(-1.46552, 
    -1.18122, -0.756657), cameraUpVector=(0.72, 0.00738062, -0.693935), 
    cameraTarget=(0.217844, -0.1456, -0.0133188), viewOffsetX=0.172351, 
    viewOffsetY=0.126138)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Flange-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#78000000 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Flange_Bottom_Edge')
#: The surface 'Flange_Bottom_Edge' has been edited (4 faces).
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.89441, 
    farPlane=2.7976, width=1.1036, height=0.682331, cameraPosition=(-0.914127, 
    0.744674, -2.01135), cameraUpVector=(0.839293, -0.483963, -0.247722), 
    cameraTarget=(0.0477979, 0.0620458, -0.259925), viewOffsetX=0.186554, 
    viewOffsetY=0.136533)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'Long_Side-1', 'Short Side-1', 'Long_Side-2', 'Bottom-1', 
    'Short Side With Holes-1', 'Flange-1', 'Cap-1', 'Bolt-1', 'Bolt-2', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.74608, 
    farPlane=2.9098, width=1.01719, height=0.628907, cameraPosition=(-1.53524, 
    -1.18047, 0.306151), cameraUpVector=(0.403038, -0.182347, -0.896833), 
    cameraTarget=(0.284622, -0.125045, 0.124605), viewOffsetX=0.171947, 
    viewOffsetY=0.125842)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.78027, 
    farPlane=2.87561, width=0.721336, height=0.445987, viewOffsetX=0.296206, 
    viewOffsetY=0.197345)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-1'].faces
f2 = a1.instances['Flange-1'].faces
a1.Coaxial(movableAxis=f1[5], fixedAxis=f2[18], flip=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.81708, 
    farPlane=2.8388, width=0.507918, height=0.314035, viewOffsetX=0.288578, 
    viewOffsetY=0.159995)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.1316, 
    farPlane=2.7451, width=0.595832, height=0.368391, cameraPosition=(
    -0.295177, -0.0100179, -2.50016), cameraUpVector=(0.966199, -0.181094, 
    0.183479), cameraTarget=(0.0166342, -0.119979, -0.414619), 
    viewOffsetX=0.338527, viewOffsetY=0.187688)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.04585, 
    farPlane=2.83086, width=1.57167, height=0.971733, viewOffsetX=0.610811, 
    viewOffsetY=0.205675)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.63839, 
    farPlane=2.83111, width=1.25865, height=0.778197, cameraPosition=(-1.3136, 
    -0.88825, -1.31651), cameraUpVector=(0.945331, -0.242841, -0.217662), 
    cameraTarget=(-0.0269203, -0.103395, 0.162427), viewOffsetX=0.489159, 
    viewOffsetY=0.164711)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-1'].faces
f2 = a1.instances['Cap-1'].faces
a1.FaceToFace(movablePlane=f1[2], fixedPlane=f2[37], flip=ON, clearance=0.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.88507, 
    farPlane=2.9107, width=1.44816, height=0.895367, cameraPosition=(-1.13094, 
    0.135674, -2.05519), cameraUpVector=(0.966495, -0.160176, -0.200577), 
    cameraTarget=(-0.0827707, -0.192264, -0.251696), viewOffsetX=0.562809, 
    viewOffsetY=0.189511)
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Bolt']
a1.Instance(name='Bolt-3', part=p, dependent=ON)
p1 = a1.instances['Bolt-3']
p1.translate(vector=(0.800010295153912, 0.0, 0.0))
session.viewports['Viewport: 1'].view.fitView()
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Bolt']
a1.Instance(name='Bolt-4', part=p, dependent=ON)
p1 = a1.instances['Bolt-4']
p1.translate(vector=(0.827510295563694, 0.0, 0.0))
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.67758, 
    farPlane=2.9448, width=1.25496, height=0.775915, cameraPosition=(-1.4297, 
    -1.26191, -0.442395), cameraUpVector=(0.291069, 0.384259, -0.876141))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.86094, 
    farPlane=2.79072, width=1.39213, height=0.860724, cameraPosition=(1.06844, 
    -2.11018, -0.207578), cameraUpVector=(-0.534715, 0.223004, -0.815076), 
    cameraTarget=(0.417155, 0.0673121, -0.114785))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.69874, 
    farPlane=2.96793, width=1.27079, height=0.785704, cameraPosition=(1.89245, 
    -1.29714, 0.979042), cameraUpVector=(0.0691874, -0.141363, -0.987537), 
    cameraTarget=(0.435269, 0.0851848, -0.0887002))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.7842, 
    farPlane=2.88247, width=0.387212, height=0.239405, viewOffsetX=-0.140634, 
    viewOffsetY=0.0192422)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.93912, 
    farPlane=3.07169, width=0.420832, height=0.260192, cameraPosition=(2.62444, 
    0.927312, -0.950217), cameraUpVector=(-0.618763, -0.178674, -0.764989), 
    cameraTarget=(0.66152, 0.0936146, -0.158916), viewOffsetX=-0.152845, 
    viewOffsetY=0.020913)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.90503, 
    farPlane=3.10578, width=0.823275, height=0.509014, viewOffsetX=-0.144124, 
    viewOffsetY=0.0583743)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-4'].faces
f2 = a1.instances['Cap-1'].faces
a1.Coaxial(movableAxis=f1[3], fixedAxis=f2[26], flip=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.91003, 
    farPlane=3.03339, width=0.825436, height=0.510351, cameraPosition=(2.70522, 
    -0.70838, 0.143541), cameraUpVector=(-0.245826, 0.0768955, -0.966259), 
    cameraTarget=(0.528699, -0.0723944, -0.0367988), viewOffsetX=-0.144502, 
    viewOffsetY=0.0585275)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.90966, 
    farPlane=3.03375, width=0.885153, height=0.547272, viewOffsetX=-0.126384, 
    viewOffsetY=0.0557477)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.02964, 
    farPlane=2.93954, width=0.940763, height=0.581655, cameraPosition=(
    0.062392, 1.79997, -1.93246), cameraUpVector=(-0.0965579, -0.933099, 
    -0.346415), cameraTarget=(0.522005, 0.321242, -0.266219), 
    viewOffsetX=-0.134324, viewOffsetY=0.05925)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.01414, 
    farPlane=2.95503, width=1.12401, height=0.69495, viewOffsetX=-0.138517, 
    viewOffsetY=0.108691)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.00096, 
    farPlane=2.95082, width=1.11665, height=0.690401, cameraPosition=(1.05114, 
    1.94518, -1.66669), cameraUpVector=(-0.340468, -0.796281, -0.500018), 
    cameraTarget=(0.615963, 0.259637, -0.20251), viewOffsetX=-0.13761, 
    viewOffsetY=0.10798)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-3'].faces
f2 = a1.instances['Cap-1'].faces
a1.Coaxial(movableAxis=f1[3], fixedAxis=f2[34], flip=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.9373, 
    farPlane=2.9541, width=1.08112, height=0.668437, cameraPosition=(-0.69957, 
    2.26631, 0.37636), cameraUpVector=(-0.24568, -0.337095, -0.90885), 
    cameraTarget=(0.459164, 0.358968, -0.0636865), viewOffsetX=-0.133232, 
    viewOffsetY=0.104545)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.97396, 
    farPlane=2.91744, width=0.763056, height=0.471782, viewOffsetX=-0.250603, 
    viewOffsetY=0.111806)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.95164, 
    farPlane=2.8754, width=0.75443, height=0.466449, cameraPosition=(-0.379423, 
    2.21651, -1.07218), cameraUpVector=(0.229887, -0.679504, -0.696726), 
    cameraTarget=(0.463036, 0.356965, -0.0688761), viewOffsetX=-0.24777, 
    viewOffsetY=0.110542)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-3'].faces
f2 = a1.instances['Cap-1'].faces
a1.FaceToFace(movablePlane=f1[2], fixedPlane=f2[37], flip=ON, clearance=0.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.90478, 
    farPlane=2.92227, width=1.37264, height=0.848678, viewOffsetX=-0.146062, 
    viewOffsetY=0.178918)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.95176, 
    farPlane=2.82247, width=1.40651, height=0.869614, cameraPosition=(1.13648, 
    2.37358, -0.395756), cameraUpVector=(-0.12727, -0.475404, -0.870513), 
    cameraTarget=(0.593494, 0.200291, -0.000486597), viewOffsetX=-0.149665, 
    viewOffsetY=0.183332)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.02983, 
    farPlane=2.7444, width=0.451445, height=0.279119, viewOffsetX=0.0478669, 
    viewOffsetY=0.0260927)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.05698, 
    farPlane=2.90636, width=0.457483, height=0.282853, cameraPosition=(1.71238, 
    2.18183, 0.244728), cameraUpVector=(0.0759506, -0.315543, -0.945867), 
    cameraTarget=(0.618755, 0.200401, 0.0163211), viewOffsetX=0.0485071, 
    viewOffsetY=0.0264417)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.0386, 
    farPlane=2.92473, width=0.702032, height=0.434052, viewOffsetX=0.0432037, 
    viewOffsetY=0.0151164)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.99736, 
    farPlane=2.73118, width=0.68783, height=0.425271, cameraPosition=(0.890352, 
    0.843008, -2.32026), cameraUpVector=(-0.214345, -0.976481, -0.0232642), 
    cameraTarget=(0.550959, 0.090539, -0.20063), viewOffsetX=0.0423297, 
    viewOffsetY=0.0148106)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.94907, 
    farPlane=2.77947, width=1.3257, height=0.819653, viewOffsetX=0.0650954, 
    viewOffsetY=0.011899)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.84944, 
    farPlane=2.67592, width=1.25793, height=0.777756, cameraPosition=(0.333673, 
    2.1388, -1.15254), cameraUpVector=(-0.52514, -0.692667, -0.494408), 
    cameraTarget=(0.548688, 0.132128, -0.103126), viewOffsetX=0.061768, 
    viewOffsetY=0.0112907)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.84056, 
    farPlane=2.6848, width=1.50725, height=0.931899, viewOffsetX=0.0931394, 
    viewOffsetY=0.0546443)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-4'].faces
f2 = a1.instances['Cap-1'].faces
a1.FaceToFace(movablePlane=f1[2], fixedPlane=f2[37], flip=ON, clearance=0.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.4953, 
    farPlane=2.67259, width=1.22451, height=0.757092, cameraPosition=(-1.17351, 
    1.49558, -0.357539), cameraUpVector=(0.120661, -0.513337, -0.849662), 
    cameraTarget=(0.544766, 0.0245297, -0.11713), viewOffsetX=0.0756682, 
    viewOffsetY=0.044394)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.5642, 
    farPlane=2.68731, width=1.28094, height=0.791979, cameraPosition=(
    -0.898542, 1.67763, -0.808342), cameraUpVector=(0.268408, -0.56799, 
    -0.778039), cameraTarget=(0.488356, 0.0215698, -0.0954309), 
    viewOffsetX=0.079155, viewOffsetY=0.0464397)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.46748, 
    farPlane=2.65405, width=1.20173, height=0.743008, cameraPosition=(-1.46692, 
    0.978945, -0.475193), cameraUpVector=(0.347783, -0.38219, -0.856141), 
    cameraTarget=(0.569242, 0.0324899, -0.111163), viewOffsetX=0.0742606, 
    viewOffsetY=0.0435682)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.44968, 
    farPlane=2.53724, width=1.18716, height=0.733995, cameraPosition=(-1.59427, 
    -0.221512, -0.203482), cameraUpVector=(0.276333, 0.397184, -0.875149), 
    cameraTarget=(0.656216, 0.109427, -0.209058), viewOffsetX=0.0733598, 
    viewOffsetY=0.0430397)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.47423, 
    farPlane=2.5635, width=1.20726, height=0.746427, cameraPosition=(-1.60745, 
    0.053181, -0.534599), cameraUpVector=(0.455011, 0.461656, -0.761472), 
    cameraTarget=(0.639223, 0.0678538, -0.178938), viewOffsetX=0.0746021, 
    viewOffsetY=0.0437686)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.51252, 
    farPlane=2.52521, width=0.709724, height=0.438808, viewOffsetX=-0.0255707, 
    viewOffsetY=-0.0293517)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.43116, 
    farPlane=2.51817, width=0.671549, height=0.415205, cameraPosition=(
    -1.08833, 1.24033, -0.845474), cameraUpVector=(0.622157, -0.173003, 
    -0.763539), cameraTarget=(0.608763, -0.105555, -0.150696), 
    viewOffsetX=-0.0241953, viewOffsetY=-0.0277728)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.50352, 
    farPlane=2.49229, width=0.705504, height=0.436199, cameraPosition=(-1.6181, 
    -0.0986557, -0.188351), cameraUpVector=(0.286971, 0.219387, -0.932479), 
    cameraTarget=(0.645829, 0.112105, -0.255152), viewOffsetX=-0.0254187, 
    viewOffsetY=-0.029177)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.49651, 
    farPlane=2.60831, width=0.702215, height=0.434165, cameraPosition=(
    -1.35246, -0.561255, -1.01688), cameraUpVector=(0.600412, 0.304058, 
    -0.739631), cameraTarget=(0.614477, 0.174543, -0.142811), 
    viewOffsetX=-0.0253002, viewOffsetY=-0.029041)
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'Cap-1', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.44777, 
    farPlane=2.55147, width=0.679346, height=0.420026, cameraPosition=(
    -1.45685, -0.485027, 0.426224), cameraUpVector=(-0.0539824, 0.28047, 
    -0.958344), cameraTarget=(0.601453, 0.166329, -0.290258), 
    viewOffsetX=-0.0244762, viewOffsetY=-0.0280952)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.45688, 
    farPlane=2.51608, width=0.843959, height=0.521803, viewOffsetX=-0.110702, 
    viewOffsetY=0.035261)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.67663, 
    farPlane=2.52962, width=0.971255, height=0.600507, cameraPosition=(0.98695, 
    -1.85987, 0.264297), cameraUpVector=(-0.920424, -0.0544212, -0.387116), 
    cameraTarget=(0.224815, 0.237402, -0.177066), viewOffsetX=-0.1274, 
    viewOffsetY=0.0405794)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.64796, 
    farPlane=2.55828, width=1.2378, height=0.765306, viewOffsetX=-0.109756, 
    viewOffsetY=-0.116611)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.62895, 
    farPlane=2.78592, width=1.22352, height=0.75648, cameraPosition=(2.46924, 
    -0.469665, -0.517704), cameraUpVector=(-0.555956, -0.76912, -0.315226), 
    cameraTarget=(0.272598, -0.0287954, -0.12451), viewOffsetX=-0.10849, 
    viewOffsetY=-0.115266)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.69581, 
    farPlane=2.71906, width=0.444894, height=0.275069, viewOffsetX=-0.17883, 
    viewOffsetY=-0.248204)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.67381, 
    farPlane=2.69216, width=0.43912, height=0.271499, cameraPosition=(2.48162, 
    -0.309772, 0.303624), cameraUpVector=(-0.220085, -0.634193, -0.741189), 
    cameraTarget=(0.306067, -0.0406442, -0.303619), viewOffsetX=-0.176509, 
    viewOffsetY=-0.244983)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.68074, 
    farPlane=2.68522, width=0.389613, height=0.24089, viewOffsetX=-0.184914, 
    viewOffsetY=-0.215996)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Cap-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#0 #20 ]', ), )
region1=a.Surface(side1Faces=side1Faces1, name='Cap_Top_Surface')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Bolt-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#4 ]', ), )
s2 = a.instances['Bolt-3'].faces
side1Faces2 = s2.getSequenceFromMask(mask=('[#4 ]', ), )
s3 = a.instances['Bolt-2'].faces
side1Faces3 = s3.getSequenceFromMask(mask=('[#4 ]', ), )
s4 = a.instances['Bolt-4'].faces
side1Faces4 = s4.getSequenceFromMask(mask=('[#4 ]', ), )
region2=a.Surface(side1Faces=side1Faces1+side1Faces2+side1Faces3+side1Faces4, 
    name='Bolts_Top_Constraint_Surface')
mdb.models['Model-1'].Tie(name='Constraint-6', master=region1, slave=region2, 
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.66892, 
    farPlane=2.69705, width=0.531465, height=0.328594, viewOffsetX=-0.13749, 
    viewOffsetY=-0.206547)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.76629, 
    farPlane=2.83442, width=0.562473, height=0.347766, cameraPosition=(2.479, 
    0.828074, -0.75347), cameraUpVector=(-0.152995, -0.81554, -0.558111), 
    cameraTarget=(0.450681, -0.0680789, -0.246473), viewOffsetX=-0.145512, 
    viewOffsetY=-0.218598)
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'Cap-1', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.75716, 
    farPlane=2.84355, width=0.673704, height=0.416537, viewOffsetX=-0.101936, 
    viewOffsetY=-0.217)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.73698, 
    farPlane=2.81919, width=0.665967, height=0.411754, cameraPosition=(2.58839, 
    0.664534, 0.111656), cameraUpVector=(-0.0763426, -0.160772, -0.984035), 
    cameraTarget=(0.454716, 0.0600641, -0.394564), viewOffsetX=-0.100765, 
    viewOffsetY=-0.214508)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.73311, 
    farPlane=2.82587, width=0.664485, height=0.410837, cameraPosition=(2.55915, 
    0.715167, 0.239548), cameraUpVector=(-0.016691, -0.158492, -0.987219), 
    cameraTarget=(0.472266, 0.0635682, -0.388585), viewOffsetX=-0.100541, 
    viewOffsetY=-0.21403)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.73326, 
    farPlane=2.82573, width=0.664542, height=0.410873, viewOffsetX=-0.10055, 
    viewOffsetY=-0.214048)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.72933, 
    farPlane=2.82908, width=0.663036, height=0.409942, cameraPosition=(2.52382, 
    0.724943, 0.396926), cameraUpVector=(0.054307, -0.155901, -0.986279), 
    cameraTarget=(0.490177, 0.0648443, -0.379469), viewOffsetX=-0.100322, 
    viewOffsetY=-0.213563)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.72946, 
    farPlane=2.82896, width=0.663087, height=0.409973, viewOffsetX=-0.10033, 
    viewOffsetY=-0.213579)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.69156, 
    farPlane=2.81833, width=1.20904, height=0.747528, viewOffsetX=0.0174489, 
    viewOffsetY=-0.120225)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.67386, 
    farPlane=2.7927, width=1.19639, height=0.739704, cameraPosition=(2.30196, 
    1.24085, -0.373736), cameraUpVector=(0.0186259, -0.64486, -0.764074), 
    cameraTarget=(0.431018, -0.0518087, -0.320695), viewOffsetX=0.0172663, 
    viewOffsetY=-0.118967)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.68229, 
    farPlane=2.79906, width=1.20242, height=0.743429, cameraPosition=(1.66986, 
    1.33779, -1.50727), cameraUpVector=(0.0630107, -0.917004, -0.393869), 
    cameraTarget=(0.427065, -0.107565, -0.266052), viewOffsetX=0.0173533, 
    viewOffsetY=-0.119566)
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'Flange-1', 'Cap-1', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.71961, 
    farPlane=2.76174, width=0.913155, height=0.564585, viewOffsetX=0.0921271, 
    viewOffsetY=0.00373174)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Flange-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#0 #100 ]', ), )
region1=a.Surface(side1Faces=side1Faces1, name='Flange_Bolt_Master_Surface')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Bolt-4'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#10 ]', ), )
s2 = a.instances['Bolt-3'].faces
side1Faces2 = s2.getSequenceFromMask(mask=('[#10 ]', ), )
s3 = a.instances['Bolt-1'].faces
side1Faces3 = s3.getSequenceFromMask(mask=('[#10 ]', ), )
s4 = a.instances['Bolt-2'].faces
side1Faces4 = s4.getSequenceFromMask(mask=('[#10 ]', ), )
region2=a.Surface(side1Faces=side1Faces1+side1Faces2+side1Faces3+side1Faces4, 
    name='Bolt_Flange_Slave_Surface')
mdb.models['Model-1'].Tie(name='Constraint-7', master=region1, slave=region2, 
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.65893, 
    farPlane=2.82242, width=1.64225, height=1.01537, viewOffsetX=0.279334, 
    viewOffsetY=0.0244036)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.38163, 
    farPlane=2.39916, width=1.36773, height=0.845637, cameraPosition=(
    -0.213394, 1.40329, -1.39622), cameraUpVector=(0.258126, -0.790679, 
    -0.555155), cameraTarget=(0.400927, -0.31161, -0.0338914), 
    viewOffsetX=0.23264, viewOffsetY=0.0203242)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON, mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
p1 = mdb.models['Model-1'].parts['Flange']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
mdb.models['Model-1'].HomogeneousSolidSection(name='Solid_Steel', 
    material='Steel', thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(name='Solid_Aluminum', 
    material='Aluminum-6061', thickness=None)
p1 = mdb.models['Model-1'].parts['Cap']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.5329, 
    farPlane=2.11406, width=1.38046, height=0.853513, cameraPosition=(0.984663, 
    -0.882564, 1.6012), cameraTarget=(0.558918, -0.174722, -0.0244645))
p = mdb.models['Model-1'].parts['Cap']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(cells=cells, name='Cap')
p = mdb.models['Model-1'].parts['Cap']
p.SectionAssignment(region=region, sectionName='Solid_Steel', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON, mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
p1 = mdb.models['Model-1'].parts['Bolt']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['Bolt']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(cells=cells, name='All_Bolt')
p = mdb.models['Model-1'].parts['Bolt']
p.SectionAssignment(region=region, sectionName='Solid_Steel', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0967328, 
    farPlane=0.166699, width=0.0981797, height=0.0607025, 
    viewOffsetX=0.00936678, viewOffsetY=0.000482237)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
p1 = mdb.models['Model-1'].parts['Flange']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.69465, 
    farPlane=2.02993, width=1.06005, height=0.656633, viewOffsetX=0.0881533, 
    viewOffsetY=0.00573495)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON, mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
p = mdb.models['Model-1'].parts['Flange']
c = p.cells
cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
region = p.Set(cells=cells, name='All_Flange')
p = mdb.models['Model-1'].parts['Flange']
p.SectionAssignment(region=region, sectionName='Solid_Steel', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p1 = mdb.models['Model-1'].parts['Cap']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
mdb.models['Model-1'].parts['Cap'].sectionAssignments[0].setValues(
    sectionName='Solid_Aluminum')
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
mdb.models['Model-1'].loads['Cap_Pressure'].suppress()
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
del mdb.models['Model-1'].constraints['Cap to sides']
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
mdb.jobs['Pressure_Box_With_Holes'].submit(consistencyChecking=OFF)
#: The job input file "Pressure_Box_With_Holes.inp" has been submitted for analysis.
#: Job Pressure_Box_With_Holes: Analysis Input File Processor completed successfully.
#: Job Pressure_Box_With_Holes: Abaqus/Standard completed successfully.
#: Job Pressure_Box_With_Holes completed successfully. 
o3 = session.openOdb(
    name='C:/Users/chs17004/Desktop/Abaqus Pressure Vessel/Pressure Box with Bolts/Pressure_Box_With_Holes.odb')
#: Model: C:/Users/chs17004/Desktop/Abaqus Pressure Vessel/Pressure Box with Bolts/Pressure_Box_With_Holes.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     11
#: Number of Meshes:             11
#: Number of Element Sets:       31
#: Number of Node Sets:          33
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.56324, 
    farPlane=2.70366, width=0.990048, height=0.612126, cameraPosition=(1.46132, 
    -1.20083, -1.38429), cameraUpVector=(-0.838147, 0.300956, -0.454901), 
    cameraTarget=(0.405197, 0.0989098, -0.117299))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.53761, 
    farPlane=2.72929, width=1.34952, height=0.834384, viewOffsetX=0.0210397, 
    viewOffsetY=0.00408134)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.55782, 
    farPlane=2.67232, width=1.36726, height=0.845351, cameraPosition=(1.88063, 
    0.0014891, -1.59344), cameraUpVector=(-0.881115, 0.212911, -0.422262), 
    cameraTarget=(0.402854, 0.122866, -0.106353), viewOffsetX=0.0213162, 
    viewOffsetY=0.00413499)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Bolt']
a1.Instance(name='Bolt-5', part=p, dependent=ON)
p1 = a1.instances['Bolt-5']
p1.translate(vector=(0.800010295153912, 0.0, 0.0))
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.60029, 
    farPlane=2.72484, width=0.902134, height=0.557771, cameraPosition=(1.57239, 
    1.56412, -1.20932), cameraUpVector=(-0.303542, -0.727453, -0.615366), 
    cameraTarget=(0.397595, 0.133563, -0.10599))
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'Flange-1', 'Cap-1', ))
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Bolt']
a1.Instance(name='Bolt-6', part=p, dependent=ON)
p1 = a1.instances['Bolt-6']
p1.translate(vector=(0.827510295563694, 0.0, 0.0))
session.viewports['Viewport: 1'].view.fitView()
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Bolt']
a1.Instance(name='Bolt-7', part=p, dependent=ON)
p1 = a1.instances['Bolt-7']
p1.translate(vector=(0.855010295973476, 0.0, 0.0))
session.viewports['Viewport: 1'].view.fitView()
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Bolt']
a1.Instance(name='Bolt-8', part=p, dependent=ON)
p1 = a1.instances['Bolt-8']
p1.translate(vector=(0.882510296383258, 0.0, 0.0))
session.viewports['Viewport: 1'].view.fitView()
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Bolt']
a1.Instance(name='Bolt-9', part=p, dependent=ON)
p1 = a1.instances['Bolt-9']
p1.translate(vector=(0.91001029679304, 0.0, 0.0))
session.viewports['Viewport: 1'].view.fitView()
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Bolt']
a1.Instance(name='Bolt-10', part=p, dependent=ON)
p1 = a1.instances['Bolt-10']
p1.translate(vector=(0.937510297202822, 0.0, 0.0))
session.viewports['Viewport: 1'].view.fitView()
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Bolt']
a1.Instance(name='Bolt-11', part=p, dependent=ON)
p1 = a1.instances['Bolt-11']
p1.translate(vector=(0.965010297612604, 0.0, 0.0))
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.86219, 
    farPlane=3.08532, width=0.920035, height=0.568839, cameraPosition=(1.8253, 
    1.776, -1.35747), cameraUpVector=(-0.414058, -0.651986, -0.635192))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.91152, 
    farPlane=3.03599, width=0.350917, height=0.216965, viewOffsetX=0.187187, 
    viewOffsetY=-0.0539978)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-5'].faces
f2 = a1.instances['Cap-1'].faces
a1.Coaxial(movableAxis=f1[3], fixedAxis=f2[23], flip=OFF)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-6'].faces
f2 = a1.instances['Cap-1'].faces
a1.Coaxial(movableAxis=f1[3], fixedAxis=f2[25], flip=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.89367, 
    farPlane=3.05384, width=0.611684, height=0.378192, viewOffsetX=0.182866, 
    viewOffsetY=-0.0108811)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-7'].faces
f2 = a1.instances['Cap-1'].faces
a1.Coaxial(movableAxis=f1[3], fixedAxis=f2[24], flip=OFF)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-8'].faces
f2 = a1.instances['Cap-1'].faces
a1.Coaxial(movableAxis=f1[3], fixedAxis=f2[8], flip=OFF)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-9'].faces
f2 = a1.instances['Cap-1'].faces
a1.Coaxial(movableAxis=f1[3], fixedAxis=f2[9], flip=OFF)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-10'].faces
f2 = a1.instances['Cap-1'].faces
a1.Coaxial(movableAxis=f1[3], fixedAxis=f2[10], flip=OFF)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-11'].faces
f2 = a1.instances['Cap-1'].faces
a1.Coaxial(movableAxis=f1[3], fixedAxis=f2[7], flip=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.99753, 
    farPlane=3.05492, width=0.826426, height=0.510962, viewOffsetX=0.153936, 
    viewOffsetY=0.0298151)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.70009, 
    farPlane=2.68404, width=0.966503, height=0.597569, cameraPosition=(1.23168, 
    1.3157, 1.4958), cameraUpVector=(0.536825, 0.129757, -0.833656), 
    cameraTarget=(0.398351, 0.12724, -0.0834211))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.73047, 
    farPlane=2.62043, width=0.983776, height=0.608249, cameraPosition=(
    -0.128554, 1.69174, -1.53812), cameraUpVector=(-0.359007, -0.871769, 
    -0.333366), cameraTarget=(0.369116, 0.135322, -0.148627))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.63878, 
    farPlane=2.71945, width=0.931653, height=0.576022, cameraPosition=(1.56989, 
    1.47863, -1.33021), cameraUpVector=(-0.6369, -0.494585, -0.591392), 
    cameraTarget=(0.39293, 0.132334, -0.145712))
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-5'].faces
f2 = a1.instances['Cap-1'].faces
a1.FaceToFace(movablePlane=f1[2], fixedPlane=f2[37], flip=ON, clearance=0.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.64318, 
    farPlane=2.71882, width=0.934155, height=0.577569, cameraPosition=(2.51536, 
    0.454982, 0.0864678), cameraUpVector=(-0.191999, -0.347101, -0.917964), 
    cameraTarget=(0.407755, 0.116283, -0.123498))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.67736, 
    farPlane=2.68465, width=0.513616, height=0.317559, viewOffsetX=-0.00433249, 
    viewOffsetY=-0.0413991)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.66698, 
    farPlane=2.71092, width=0.510439, height=0.315594, cameraPosition=(2.452, 
    0.498371, 0.437336), cameraUpVector=(-0.0352192, -0.306939, -0.951077), 
    cameraTarget=(0.414766, 0.119541, -0.116704), viewOffsetX=-0.00430568, 
    viewOffsetY=-0.041143)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.66446, 
    farPlane=2.71343, width=0.576809, height=0.35663, viewOffsetX=0.0020227, 
    viewOffsetY=-0.054526)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.65858, 
    farPlane=2.59828, width=0.574768, height=0.355368, cameraPosition=(1.65133, 
    0.241014, -1.82079), cameraUpVector=(-0.873289, -0.388726, -0.293698), 
    cameraTarget=(0.327302, 0.105378, -0.138723), viewOffsetX=0.00201555, 
    viewOffsetY=-0.054333)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.64021, 
    farPlane=2.61664, width=0.830682, height=0.513594, viewOffsetX=0.0205574, 
    viewOffsetY=-0.0215759)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-6'].faces
f2 = a1.instances['Cap-1'].faces
a1.FaceToFace(movablePlane=f1[2], fixedPlane=f2[37], flip=ON, clearance=0.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.57018, 
    farPlane=2.66812, width=0.795218, height=0.491667, cameraPosition=(2.31638, 
    0.370142, 0.677897), cameraUpVector=(0.0787225, -0.142248, -0.986696), 
    cameraTarget=(0.361026, 0.114146, -0.165808), viewOffsetX=0.0196798, 
    viewOffsetY=-0.0206547)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.5807, 
    farPlane=2.65759, width=0.752512, height=0.465263, viewOffsetX=0.0263633, 
    viewOffsetY=-0.0233831)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.58252, 
    farPlane=2.65272, width=0.753381, height=0.4658, cameraPosition=(2.14477, 
    0.308188, -1.26586), cameraUpVector=(-0.759372, -0.193134, -0.621333), 
    cameraTarget=(0.330516, 0.112652, -0.138454), viewOffsetX=0.0263937, 
    viewOffsetY=-0.0234101)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.57378, 
    farPlane=2.66147, width=0.902039, height=0.557712, viewOffsetX=0.049232, 
    viewOffsetY=0.0114214)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.55479, 
    farPlane=2.62602, width=0.891154, height=0.550983, cameraPosition=(2.42935, 
    0.379035, 0.131071), cameraUpVector=(-0.188596, -0.143294, -0.971544), 
    cameraTarget=(0.320648, 0.1111, -0.155974), viewOffsetX=0.0486379, 
    viewOffsetY=0.0112836)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-7'].faces
f2 = a1.instances['Cap-1'].faces
a1.FaceToFace(movablePlane=f1[2], fixedPlane=f2[37], flip=ON, clearance=0.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.5441, 
    farPlane=2.63039, width=0.885028, height=0.547195, cameraPosition=(2.31576, 
    0.219641, 0.627402), cameraUpVector=(0.0419923, -0.0720425, -0.996517), 
    cameraTarget=(0.325827, 0.115224, -0.166365), viewOffsetX=0.0483035, 
    viewOffsetY=0.011206)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.56414, 
    farPlane=2.61035, width=0.702818, height=0.434538, viewOffsetX=0.0435957, 
    viewOffsetY=-0.0272757)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.55314, 
    farPlane=2.59185, width=0.697875, height=0.431482, cameraPosition=(2.08171, 
    0.187974, -1.2927), cameraUpVector=(-0.798801, -0.0323044, -0.600727), 
    cameraTarget=(0.296679, 0.117594, -0.105471), viewOffsetX=0.0432891, 
    viewOffsetY=-0.0270839)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-8'].faces
f2 = a1.instances['Cap-1'].faces
a1.FaceToFace(movablePlane=f1[2], fixedPlane=f2[37], flip=ON, clearance=0.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.54101, 
    farPlane=2.60398, width=0.890501, height=0.550579, viewOffsetX=0.0708777, 
    viewOffsetY=0.0219451)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.46891, 
    farPlane=2.56949, width=0.848836, height=0.524818, cameraPosition=(2.14999, 
    0.311646, 0.811), cameraUpVector=(0.138222, 0.0118323, -0.990331), 
    cameraTarget=(0.257047, 0.110725, -0.177539), viewOffsetX=0.0675614, 
    viewOffsetY=0.0209183)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.4758, 
    farPlane=2.5626, width=0.856309, height=0.529438, viewOffsetX=0.0662202, 
    viewOffsetY=0.00839573)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.49524, 
    farPlane=2.56537, width=0.867586, height=0.536411, cameraPosition=(2.2016, 
    0.157078, -1.00235), cameraUpVector=(-0.714733, 0.124971, -0.688142), 
    cameraTarget=(0.27924, 0.11879, -0.051629), viewOffsetX=0.0670922, 
    viewOffsetY=0.0085063)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-9'].faces
f2 = a1.instances['Cap-1'].faces
a1.FaceToFace(movablePlane=f1[2], fixedPlane=f2[37], flip=ON, clearance=0.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.47915, 
    farPlane=2.58145, width=1.09926, height=0.679653, viewOffsetX=0.0884115, 
    viewOffsetY=0.050883)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.42819, 
    farPlane=2.60528, width=1.06139, height=0.656238, cameraPosition=(2.14265, 
    -0.450214, 0.656401), cameraUpVector=(0.0507126, -0.00437911, -0.998704), 
    cameraTarget=(0.2565, 0.166264, -0.157964), viewOffsetX=0.0853656, 
    viewOffsetY=0.0491299)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.44466, 
    farPlane=2.5888, width=0.960908, height=0.595222, viewOffsetX=0.0716224, 
    viewOffsetY=-0.00142698)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.43713, 
    farPlane=2.5928, width=0.955899, height=0.592119, cameraPosition=(1.97442, 
    -0.669118, -1.05938), cameraUpVector=(-0.728096, 0.159974, -0.666546), 
    cameraTarget=(0.270811, 0.176911, -0.0680378), viewOffsetX=0.071249, 
    viewOffsetY=-0.00141954)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.48181, 
    farPlane=2.57821, width=0.985617, height=0.610527, cameraPosition=(2.09977, 
    -0.942146, -0.245102), cameraUpVector=(-0.348733, 0.184946, -0.918793), 
    cameraTarget=(0.281544, 0.187215, -0.105801), viewOffsetX=0.073464, 
    viewOffsetY=-0.00146367)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-10'].faces
f2 = a1.instances['Cap-1'].faces
a1.FaceToFace(movablePlane=f1[2], fixedPlane=f2[37], flip=OFF, clearance=0.0)
#* FeatureError: The constraint cannot be applied because it conflicts 
#* with existing position constraints.
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.44622, 
    farPlane=2.60717, width=0.961942, height=0.595862, cameraPosition=(2.10255, 
    -0.687576, 0.558398), cameraUpVector=(0.0513144, 0.147194, -0.987776), 
    cameraTarget=(0.266078, 0.179658, -0.13158), viewOffsetX=0.0716993, 
    viewOffsetY=-0.00142851)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.45205, 
    farPlane=2.60133, width=0.969774, height=0.600713, viewOffsetX=0.0776231, 
    viewOffsetY=-0.00470418)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.44178, 
    farPlane=2.59333, width=0.96291, height=0.596462, cameraPosition=(2.11078, 
    -0.757713, -0.655511), cameraUpVector=(-0.521957, 0.238431, -0.81897), 
    cameraTarget=(0.269955, 0.181938, -0.0817257), viewOffsetX=0.0770737, 
    viewOffsetY=-0.00467089)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-10'].faces
f2 = a1.instances['Cap-1'].faces
a1.FaceToFace(movablePlane=f1[2], fixedPlane=f2[37], flip=ON, clearance=0.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.47573, 
    farPlane=2.61452, width=0.985588, height=0.610509, cameraPosition=(1.85268, 
    -1.01286, 0.721381), cameraUpVector=(0.182725, 0.131709, -0.974302), 
    cameraTarget=(0.299691, 0.189228, -0.141189), viewOffsetX=0.0788888, 
    viewOffsetY=-0.00478089)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.48635, 
    farPlane=2.6039, width=0.888457, height=0.550343, viewOffsetX=0.0497018, 
    viewOffsetY=-0.00805775)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.50001, 
    farPlane=2.5781, width=0.896619, height=0.555398, cameraPosition=(1.81579, 
    -1.26276, -0.538246), cameraUpVector=(-0.387647, 0.347166, -0.853935), 
    cameraTarget=(0.306478, 0.196111, -0.0972385), viewOffsetX=0.0501583, 
    viewOffsetY=-0.00813177)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-11'].faces
f2 = a1.instances['Cap-1'].faces
a1.FaceToFace(movablePlane=f1[2], fixedPlane=f2[37], flip=ON, clearance=0.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.48367, 
    farPlane=2.59444, width=1.1359, height=0.703615, viewOffsetX=0.11616, 
    viewOffsetY=0.0388646)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.47928, 
    farPlane=2.62189, width=1.13254, height=0.701536, cameraPosition=(1.69045, 
    -1.12331, -1.08887), cameraUpVector=(-0.630366, 0.392037, -0.670034), 
    cameraTarget=(0.31809, 0.192014, -0.0952089), viewOffsetX=0.115816, 
    viewOffsetY=0.0387498)
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Bolt']
a1.Instance(name='Bolt-12', part=p, dependent=ON)
p1 = a1.instances['Bolt-12']
p1.translate(vector=(0.800010295153912, 0.0, 0.0))
session.viewports['Viewport: 1'].view.fitView()
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Bolt']
a1.Instance(name='Bolt-13', part=p, dependent=ON)
p1 = a1.instances['Bolt-13']
p1.translate(vector=(0.827510295563694, 0.0, 0.0))
session.viewports['Viewport: 1'].view.fitView()
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Bolt']
a1.Instance(name='Bolt-14', part=p, dependent=ON)
p1 = a1.instances['Bolt-14']
p1.translate(vector=(0.855010295973476, 0.0, 0.0))
session.viewports['Viewport: 1'].view.fitView()
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Bolt']
a1.Instance(name='Bolt-15', part=p, dependent=ON)
p1 = a1.instances['Bolt-15']
p1.translate(vector=(0.882510296383258, 0.0, 0.0))
session.viewports['Viewport: 1'].view.fitView()
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Bolt']
a1.Instance(name='Bolt-16', part=p, dependent=ON)
p1 = a1.instances['Bolt-16']
p1.translate(vector=(0.91001029679304, 0.0, 0.0))
session.viewports['Viewport: 1'].view.fitView()
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Bolt']
a1.Instance(name='Bolt-17', part=p, dependent=ON)
p1 = a1.instances['Bolt-17']
p1.translate(vector=(0.937510297202822, 0.0, 0.0))
session.viewports['Viewport: 1'].view.fitView()
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Bolt']
a1.Instance(name='Bolt-18', part=p, dependent=ON)
p1 = a1.instances['Bolt-18']
p1.translate(vector=(0.965010297612604, 0.0, 0.0))
session.viewports['Viewport: 1'].view.fitView()
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Bolt']
a1.Instance(name='Bolt-19', part=p, dependent=ON)
p1 = a1.instances['Bolt-19']
p1.translate(vector=(0.992510298022386, 0.0, 0.0))
session.viewports['Viewport: 1'].view.fitView()
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Bolt']
a1.Instance(name='Bolt-20', part=p, dependent=ON)
p1 = a1.instances['Bolt-20']
p1.translate(vector=(1.02001029843217, 0.0, 0.0))
session.viewports['Viewport: 1'].view.fitView()
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Bolt']
a1.Instance(name='Bolt-21', part=p, dependent=ON)
p1 = a1.instances['Bolt-21']
p1.translate(vector=(1.04751029884195, 0.0, 0.0))
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.15806, 
    farPlane=3.46239, width=0.738836, height=0.457662, viewOffsetX=-0.00780573, 
    viewOffsetY=-0.0775306)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-21'].faces
f2 = a1.instances['Cap-1'].faces
a1.Coaxial(movableAxis=f1[3], fixedAxis=f2[5], flip=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.16515, 
    farPlane=3.4729, width=0.957211, height=0.592932, viewOffsetX=0.133613, 
    viewOffsetY=0.108914)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-20'].faces
f2 = a1.instances['Cap-1'].faces
a1.Coaxial(movableAxis=f1[3], fixedAxis=f2[4], flip=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.20251, 
    farPlane=3.45313, width=0.639591, height=0.396186, viewOffsetX=0.122715, 
    viewOffsetY=0.113251)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-12'].faces
f2 = a1.instances['Cap-1'].faces
a1.Coaxial(movableAxis=f1[3], fixedAxis=f2[35], flip=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.18, 
    farPlane=3.47565, width=0.880879, height=0.545649, viewOffsetX=0.123112, 
    viewOffsetY=0.0193964)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-13'].faces
f2 = a1.instances['Cap-1'].faces
a1.Coaxial(movableAxis=f1[5], fixedAxis=f2[11], flip=OFF)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-14'].faces
f2 = a1.instances['Cap-1'].faces
a1.Coaxial(movableAxis=f1[3], fixedAxis=f2[12], flip=OFF)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-15'].faces
f2 = a1.instances['Cap-1'].faces
a1.Coaxial(movableAxis=f1[5], fixedAxis=f2[13], flip=OFF)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-16'].faces
f2 = a1.instances['Cap-1'].faces
a1.Coaxial(movableAxis=f1[3], fixedAxis=f2[14], flip=OFF)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-17'].faces
f2 = a1.instances['Cap-1'].faces
a1.Coaxial(movableAxis=f1[3], fixedAxis=f2[15], flip=OFF)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-18'].faces
f2 = a1.instances['Cap-1'].faces
a1.Coaxial(movableAxis=f1[3], fixedAxis=f2[22], flip=OFF)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-19'].faces
f2 = a1.instances['Cap-1'].faces
a1.Coaxial(movableAxis=f1[3], fixedAxis=f2[21], flip=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.31464, 
    farPlane=3.48176, width=1.19793, height=0.742045, viewOffsetX=0.192381, 
    viewOffsetY=0.0182234)
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Bolt']
a1.Instance(name='Bolt-22', part=p, dependent=ON)
p1 = a1.instances['Bolt-22']
p1.translate(vector=(0.800010295153912, 0.0, 0.0))
session.viewports['Viewport: 1'].view.fitView()
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Bolt']
a1.Instance(name='Bolt-23', part=p, dependent=ON)
p1 = a1.instances['Bolt-23']
p1.translate(vector=(0.827510295563694, 0.0, 0.0))
session.viewports['Viewport: 1'].view.fitView()
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Bolt']
a1.Instance(name='Bolt-24', part=p, dependent=ON)
p1 = a1.instances['Bolt-24']
p1.translate(vector=(0.855010295973476, 0.0, 0.0))
session.viewports['Viewport: 1'].view.fitView()
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Bolt']
a1.Instance(name='Bolt-25', part=p, dependent=ON)
p1 = a1.instances['Bolt-25']
p1.translate(vector=(0.882510296383258, 0.0, 0.0))
session.viewports['Viewport: 1'].view.fitView()
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Bolt']
a1.Instance(name='Bolt-26', part=p, dependent=ON)
p1 = a1.instances['Bolt-26']
p1.translate(vector=(0.91001029679304, 0.0, 0.0))
session.viewports['Viewport: 1'].view.fitView()
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Bolt']
a1.Instance(name='Bolt-27', part=p, dependent=ON)
p1 = a1.instances['Bolt-27']
p1.translate(vector=(0.937510297202822, 0.0, 0.0))
session.viewports['Viewport: 1'].view.fitView()
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Bolt']
a1.Instance(name='Bolt-28', part=p, dependent=ON)
p1 = a1.instances['Bolt-28']
p1.translate(vector=(0.965010297612604, 0.0, 0.0))
session.viewports['Viewport: 1'].view.fitView()
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-22'].faces
f2 = a1.instances['Cap-1'].faces
a1.Coaxial(movableAxis=f1[3], fixedAxis=f2[20], flip=OFF)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-23'].faces
f2 = a1.instances['Cap-1'].faces
a1.Coaxial(movableAxis=f1[3], fixedAxis=f2[19], flip=OFF)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-24'].faces
f2 = a1.instances['Cap-1'].faces
a1.Coaxial(movableAxis=f1[3], fixedAxis=f2[27], flip=OFF)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-25'].faces
f2 = a1.instances['Cap-1'].faces
a1.Coaxial(movableAxis=f1[3], fixedAxis=f2[28], flip=OFF)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-26'].faces
f2 = a1.instances['Cap-1'].faces
a1.Coaxial(movableAxis=f1[5], fixedAxis=f2[29], flip=OFF)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-27'].faces
f2 = a1.instances['Cap-1'].faces
a1.Coaxial(movableAxis=f1[3], fixedAxis=f2[30], flip=OFF)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-28'].faces
f2 = a1.instances['Cap-1'].faces
a1.Coaxial(movableAxis=f1[5], fixedAxis=f2[31], flip=OFF)
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Bolt']
a1.Instance(name='Bolt-29', part=p, dependent=ON)
p1 = a1.instances['Bolt-29']
p1.translate(vector=(0.800010295153912, 0.0, 0.0))
session.viewports['Viewport: 1'].view.fitView()
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Bolt']
a1.Instance(name='Bolt-30', part=p, dependent=ON)
p1 = a1.instances['Bolt-30']
p1.translate(vector=(0.827510295563694, 0.0, 0.0))
session.viewports['Viewport: 1'].view.fitView()
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Bolt']
a1.Instance(name='Bolt-31', part=p, dependent=ON)
p1 = a1.instances['Bolt-31']
p1.translate(vector=(0.855010295973476, 0.0, 0.0))
session.viewports['Viewport: 1'].view.fitView()
a1 = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['Bolt']
a1.Instance(name='Bolt-32', part=p, dependent=ON)
p1 = a1.instances['Bolt-32']
p1.translate(vector=(0.882510296383258, 0.0, 0.0))
session.viewports['Viewport: 1'].view.fitView()
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-32'].faces
f2 = a1.instances['Cap-1'].faces
a1.Coaxial(movableAxis=f1[3], fixedAxis=f2[33], flip=OFF)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-31'].faces
f2 = a1.instances['Cap-1'].faces
a1.Coaxial(movableAxis=f1[3], fixedAxis=f2[32], flip=OFF)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-30'].faces
f2 = a1.instances['Cap-1'].faces
a1.Coaxial(movableAxis=f1[3], fixedAxis=f2[16], flip=OFF)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-29'].faces
f2 = a1.instances['Cap-1'].faces
a1.Coaxial(movableAxis=f1[3], fixedAxis=f2[17], flip=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.99983, 
    farPlane=3.04585, width=0.54911, height=0.340139, viewOffsetX=0.072013, 
    viewOffsetY=-0.0456934)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.17667, 
    farPlane=3.06425, width=0.597668, height=0.370217, cameraPosition=(1.4725, 
    -2.02032, 0.925816), cameraUpVector=(-0.183976, -0.14835, -0.971671), 
    cameraTarget=(0.515937, 0.052334, -0.0628731), viewOffsetX=0.0783811, 
    viewOffsetY=-0.0497341)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.1785, 
    farPlane=3.06242, width=0.56228, height=0.348297, viewOffsetX=0.0664689, 
    viewOffsetY=-0.048744)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.17565, 
    farPlane=3.06527, width=0.561545, height=0.347842, viewOffsetX=0.0663821, 
    viewOffsetY=-0.0486803)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.17565, 
    farPlane=3.06527, width=0.561546, height=0.347842, viewOffsetX=0.0663821, 
    viewOffsetY=-0.0486803)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.37152, 
    farPlane=3.00832, width=0.612102, height=0.379158, cameraPosition=(
    0.105637, -0.129852, 2.54411), cameraUpVector=(0.259784, -0.884593, 
    -0.387307), cameraTarget=(0.46567, 0.111059, 0.0944656), 
    viewOffsetX=0.0723585, viewOffsetY=-0.053063)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.15895, 
    farPlane=3.10127, width=0.557236, height=0.345172, cameraPosition=(
    -0.690833, -1.77109, -1.62299), cameraUpVector=(-0.278603, 0.882776, 
    -0.378269), cameraTarget=(0.355463, 0.0623659, -0.306889), 
    viewOffsetX=0.0658726, viewOffsetY=-0.0483066)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-21'].faces
f2 = a1.instances['Cap-1'].faces
a1.FaceToFace(movablePlane=f1[2], fixedPlane=f2[37], flip=ON, clearance=0.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.13241, 
    farPlane=3.12781, width=0.968419, height=0.599874, viewOffsetX=0.184001, 
    viewOffsetY=0.00726205)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.16471, 
    farPlane=2.92151, width=0.983087, height=0.60896, cameraPosition=(1.02471, 
    -2.32779, 0.167232), cameraUpVector=(0.0431667, 0.265121, -0.963248), 
    cameraTarget=(0.481578, 0.0898805, -0.0525034), viewOffsetX=0.186788, 
    viewOffsetY=0.00737205)
session.graphicsOptions.setValues(dragMode=FAST, translucencyMode=1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.13347, 
    farPlane=2.97741, width=0.968899, height=0.600171, cameraPosition=(
    0.953345, -2.04801, 1.11354), cameraUpVector=(0.360615, -0.0071156, 
    -0.932688), cameraTarget=(0.455888, 0.128088, 0.0155662), 
    viewOffsetX=0.184092, viewOffsetY=0.00726565)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.13695, 
    farPlane=2.97393, width=1.00105, height=0.62009, viewOffsetX=0.178754, 
    viewOffsetY=-0.00512338)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.04869, 
    farPlane=2.96095, width=0.959709, height=0.594479, cameraPosition=(1.15354, 
    -1.89969, -1.39342), cameraUpVector=(-0.379723, 0.668462, -0.639507), 
    cameraTarget=(0.465546, 0.1411, -0.148326), viewOffsetX=0.171371, 
    viewOffsetY=-0.00491178)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-20'].faces
f2 = a1.instances['Cap-1'].faces
a1.FaceToFace(movablePlane=f1[2], fixedPlane=f2[37], flip=ON, clearance=0.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.1002, 
    farPlane=2.95843, width=0.98384, height=0.609427, cameraPosition=(1.03072, 
    -2.05328, 1.00207), cameraUpVector=(-0.0711165, -0.149653, -0.986178), 
    cameraTarget=(0.479826, 0.0948871, -0.125005), viewOffsetX=0.17568, 
    viewOffsetY=-0.00503528)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.11629, 
    farPlane=2.94234, width=0.826792, height=0.512145, viewOffsetX=0.167921, 
    viewOffsetY=-0.0218662)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.03997, 
    farPlane=2.95293, width=0.796976, height=0.493676, cameraPosition=(1.26895, 
    -1.86762, -1.35173), cameraUpVector=(-0.498092, 0.575654, -0.64848), 
    cameraTarget=(0.448296, 0.172669, -0.18891), viewOffsetX=0.161865, 
    viewOffsetY=-0.0210776)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-12'].faces
f2 = a1.instances['Cap-1'].faces
a1.FaceToFace(movablePlane=f1[2], fixedPlane=f2[37], flip=ON, clearance=0.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.11885, 
    farPlane=2.91235, width=0.827792, height=0.512765, cameraPosition=(1.0212, 
    -2.21471, 0.575098), cameraUpVector=(-0.204144, -0.00841206, -0.978905), 
    cameraTarget=(0.477381, 0.0928707, -0.178387), viewOffsetX=0.168124, 
    viewOffsetY=-0.0218926)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.12391, 
    farPlane=2.90729, width=0.786379, height=0.487112, viewOffsetX=0.176055, 
    viewOffsetY=-0.0260235)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.06436, 
    farPlane=2.93791, width=0.764329, height=0.473453, cameraPosition=(1.13172, 
    -1.8272, -1.50885), cameraUpVector=(-0.355545, 0.706088, -0.612395), 
    cameraTarget=(0.465026, 0.165861, -0.177814), viewOffsetX=0.171119, 
    viewOffsetY=-0.0252938)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-13'].faces
f2 = a1.instances['Cap-1'].faces
a1.FaceToFace(movablePlane=f1[2], fixedPlane=f2[37], flip=ON, clearance=0.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.15329, 
    farPlane=2.87959, width=0.797255, height=0.493849, cameraPosition=(
    0.855503, -2.30668, 0.37592), cameraUpVector=(-0.394986, 0.0496177, 
    -0.917346), cameraTarget=(0.460492, 0.0737187, -0.229155), 
    viewOffsetX=0.17849, viewOffsetY=-0.0263834)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.16523, 
    farPlane=2.86765, width=0.668585, height=0.414146, viewOffsetX=0.191745, 
    viewOffsetY=-0.0389665)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.04166, 
    farPlane=2.92857, width=0.630426, height=0.390509, cameraPosition=(1.31334, 
    -1.8903, -1.25731), cameraUpVector=(-0.429456, 0.575407, -0.696042), 
    cameraTarget=(0.45808, 0.19235, -0.199223), viewOffsetX=0.180801, 
    viewOffsetY=-0.0367425)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-14'].faces
f2 = a1.instances['Cap-1'].faces
a1.FaceToFace(movablePlane=f1[2], fixedPlane=f2[37], flip=ON, clearance=0.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.20443, 
    farPlane=2.86038, width=0.680685, height=0.421641, cameraPosition=(
    0.184887, -2.38419, 0.27254), cameraUpVector=(-0.348278, 0.18534, 
    -0.918886), cameraTarget=(0.462084, 0.0326773, -0.247433), 
    viewOffsetX=0.195215, viewOffsetY=-0.0396717)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.21847, 
    farPlane=2.84634, width=0.44422, height=0.275166, viewOffsetX=0.234786, 
    viewOffsetY=-0.0539745)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.17118, 
    farPlane=2.93617, width=0.434751, height=0.269301, cameraPosition=(
    -0.142295, -2.23229, 0.755843), cameraUpVector=(-0.351069, 0.0524542, 
    -0.934879), cameraTarget=(0.441144, -0.0223974, -0.226215), 
    viewOffsetX=0.229782, viewOffsetY=-0.052824)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.14731, 
    farPlane=2.96004, width=0.760081, height=0.470822, viewOffsetX=0.211581, 
    viewOffsetY=-0.0575073)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.14353, 
    farPlane=2.96382, width=0.758741, height=0.469992, viewOffsetX=0.211208, 
    viewOffsetY=-0.0574059)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.14352, 
    farPlane=2.96383, width=0.758739, height=0.469991, viewOffsetX=0.211207, 
    viewOffsetY=-0.0574057)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.14352, 
    farPlane=2.96383, width=0.758741, height=0.469992, viewOffsetX=0.211207, 
    viewOffsetY=-0.0574058)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.15042, 
    farPlane=2.95156, width=0.761183, height=0.471504, cameraPosition=(
    -0.109255, -2.27921, 0.631376), cameraUpVector=(-0.337595, 0.0918809, 
    -0.936796), cameraTarget=(0.446251, -0.0131572, -0.2317), 
    viewOffsetX=0.211887, viewOffsetY=-0.0575905)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.1609, 
    farPlane=2.93412, width=0.764894, height=0.473803, cameraPosition=(
    -0.0670239, -2.33265, 0.452719), cameraUpVector=(-0.315978, 0.148643, 
    -0.93705), cameraTarget=(0.453304, -1.86814e-05, -0.237616), 
    viewOffsetX=0.21292, viewOffsetY=-0.0578713)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.15356, 
    farPlane=2.91086, width=0.762295, height=0.472193, cameraPosition=(
    0.0816153, -2.21894, -1.07581), cameraUpVector=(-0.0814682, 0.649198, 
    -0.756244), cameraTarget=(0.495721, 0.0864405, -0.237831), 
    viewOffsetX=0.212196, viewOffsetY=-0.0576746)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-15'].faces
f2 = a1.instances['Cap-1'].faces
a1.FaceToFace(movablePlane=f1[2], fixedPlane=f2[37], flip=ON, clearance=0.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.07812, 
    farPlane=3.08065, width=0.735593, height=0.455653, cameraPosition=(
    -0.895031, -1.98835, 0.686993), cameraUpVector=(-0.204863, 0.11439, 
    -0.972083), cameraTarget=(0.406514, -0.0695677, -0.214519), 
    viewOffsetX=0.204763, viewOffsetY=-0.0556543)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.08029, 
    farPlane=3.07848, width=0.783365, height=0.485245, viewOffsetX=0.202788, 
    viewOffsetY=-0.0551322)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.1205, 
    farPlane=3.00476, width=0.798506, height=0.494624, cameraPosition=(
    -0.193091, -1.928, -1.57564), cameraUpVector=(0.208984, 0.758057, 
    -0.617799), cameraTarget=(0.514414, 0.0530283, -0.247705), 
    viewOffsetX=0.206708, viewOffsetY=-0.0561978)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-16'].faces
f2 = a1.instances['Cap-1'].faces
a1.FaceToFace(movablePlane=f1[2], fixedPlane=f2[37], flip=ON, clearance=0.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.05639, 
    farPlane=3.14813, width=0.774363, height=0.479669, cameraPosition=(-1.6355, 
    -1.52264, 0.205871), cameraUpVector=(-0.0904033, 0.387433, -0.917454), 
    cameraTarget=(0.326999, -0.0728591, -0.279073), viewOffsetX=0.200458, 
    viewOffsetY=-0.0544986)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.08938, 
    farPlane=3.11513, width=0.398348, height=0.246751, viewOffsetX=0.215853, 
    viewOffsetY=-0.0933376)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.08627, 
    farPlane=3.13205, width=0.397755, height=0.246384, cameraPosition=(
    -1.66736, -1.40395, 0.501014), cameraUpVector=(-0.154665, 0.322234, 
    -0.93394), cameraTarget=(0.300908, -0.0854365, -0.257859), 
    viewOffsetX=0.215532, viewOffsetY=-0.0931987)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.07667, 
    farPlane=3.14165, width=0.539478, height=0.334172, viewOffsetX=0.220429, 
    viewOffsetY=-0.0917024)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.06815, 
    farPlane=3.08545, width=0.537265, height=0.332801, cameraPosition=(
    -0.974115, -1.07781, -1.98634), cameraUpVector=(0.310721, 0.865429, 
    -0.393046), cameraTarget=(0.494807, 0.0934672, -0.355753), 
    viewOffsetX=0.219524, viewOffsetY=-0.0913261)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-17'].faces
f2 = a1.instances['Cap-1'].faces
a1.FaceToFace(movablePlane=f1[2], fixedPlane=f2[37], flip=ON, clearance=0.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.05527, 
    farPlane=3.09833, width=0.727504, height=0.450642, viewOffsetX=0.2257, 
    viewOffsetY=-0.0349831)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.00572, 
    farPlane=3.12219, width=0.709965, height=0.439778, cameraPosition=(
    -1.77575, -0.935391, 0.83017), cameraUpVector=(-0.242176, 0.375595, 
    -0.894583), cameraTarget=(0.265881, -0.0395458, -0.2733), 
    viewOffsetX=0.220259, viewOffsetY=-0.0341397)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.99341, 
    farPlane=3.1345, width=0.919167, height=0.569366, viewOffsetX=0.255886, 
    viewOffsetY=-0.0682698)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.95615, 
    farPlane=3.10586, width=0.901985, height=0.558723, cameraPosition=(
    -1.53025, -0.956182, -1.43527), cameraUpVector=(0.217078, 0.844027, 
    -0.490403), cameraTarget=(0.454495, 0.121674, -0.392454), 
    viewOffsetX=0.251103, viewOffsetY=-0.0669937)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.05418, 
    farPlane=3.12432, width=0.947186, height=0.586721, cameraPosition=(
    -2.18431, -0.329579, 0.0506801), cameraUpVector=(0.171504, 0.31443, 
    -0.93366), cameraTarget=(0.263187, -0.0456167, -0.292209), 
    viewOffsetX=0.263686, viewOffsetY=-0.0703508)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-29'].faces
f2 = a1.instances['Cap-1'].faces
a1.FaceToFace(movablePlane=f1[2], fixedPlane=f2[37], flip=OFF, clearance=0.0)
#* FeatureError: The constraint cannot be applied because it conflicts 
#* with existing position constraints.
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.04064, 
    farPlane=3.14625, width=0.940943, height=0.582854, cameraPosition=(
    -2.08947, -0.277504, 0.627972), cameraUpVector=(-0.0191873, 0.165677, 
    -0.985994), cameraTarget=(0.238664, -0.0677623, -0.223052), 
    viewOffsetX=0.261948, viewOffsetY=-0.0698871)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.04515, 
    farPlane=3.14174, width=0.946882, height=0.586533, viewOffsetX=0.263374, 
    viewOffsetY=-0.097019)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.02396, 
    farPlane=3.12164, width=0.937068, height=0.580454, cameraPosition=(-1.8902, 
    -0.0891339, -1.36302), cameraUpVector=(0.588329, 0.539751, -0.60211), 
    cameraTarget=(0.396573, 0.0378029, -0.39193), viewOffsetX=0.260644, 
    viewOffsetY=-0.0960134)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-29'].faces
f2 = a1.instances['Cap-1'].faces
a1.FaceToFace(movablePlane=f1[2], fixedPlane=f2[37], flip=OFF, clearance=0.0)
#* FeatureError: The constraint cannot be applied because it conflicts 
#* with existing position constraints.
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.0546, 
    farPlane=3.13927, width=0.951254, height=0.589242, cameraPosition=(
    -2.06737, -0.072894, 0.782677), cameraUpVector=(-0.0794808, 0.280528, 
    -0.95655), cameraTarget=(0.190836, -0.032909, -0.260086), 
    viewOffsetX=0.26459, viewOffsetY=-0.097467)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.05809, 
    farPlane=3.13577, width=0.952872, height=0.590244, viewOffsetX=0.276476, 
    viewOffsetY=-0.103259)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.0222, 
    farPlane=3.1179, width=0.936256, height=0.579951, cameraPosition=(-1.74552, 
    0.0460926, -1.61964), cameraUpVector=(0.529989, 0.766622, -0.362495), 
    cameraTarget=(0.454239, 0.153869, -0.46297), viewOffsetX=0.271654, 
    viewOffsetY=-0.101458)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-30'].faces
f2 = a1.instances['Cap-1'].faces
a1.FaceToFace(movablePlane=f1[2], fixedPlane=f2[37], flip=ON, clearance=0.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.00644, 
    farPlane=3.13366, width=1.1947, height=0.740041, viewOffsetX=0.28661, 
    viewOffsetY=-0.051621)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.02618, 
    farPlane=3.19727, width=1.20646, height=0.747322, cameraPosition=(-2.13366, 
    0.450176, 0.560939), cameraUpVector=(0.0407194, 0.00914535, -0.999129), 
    cameraTarget=(0.195878, -0.0137823, -0.178275), viewOffsetX=0.28943, 
    viewOffsetY=-0.0521289)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.06046, 
    farPlane=3.163, width=0.849844, height=0.526425, viewOffsetX=0.188408, 
    viewOffsetY=-0.084131)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.05103, 
    farPlane=3.13502, width=0.845956, height=0.524016, cameraPosition=(
    -1.97583, 0.194476, -1.24471), cameraUpVector=(0.641117, 0.398113, 
    -0.656106), cameraTarget=(0.338204, 0.0313402, -0.346331), 
    viewOffsetX=0.187546, viewOffsetY=-0.0837461)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-29'].faces
f2 = a1.instances['Cap-1'].faces
a1.FaceToFace(movablePlane=f1[2], fixedPlane=f2[37], flip=ON, clearance=0.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.03644, 
    farPlane=3.14962, width=1.07581, height=0.666397, viewOffsetX=0.233976, 
    viewOffsetY=-0.0444047)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.02822, 
    farPlane=3.15978, width=1.07147, height=0.663707, cameraPosition=(-2.13423, 
    0.272608, 0.555284), cameraUpVector=(0.0593523, 0.251558, -0.966021), 
    cameraTarget=(0.212773, 0.0114096, -0.226888), viewOffsetX=0.233032, 
    viewOffsetY=-0.0442255)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.05222, 
    farPlane=3.13578, width=0.849909, height=0.526465, viewOffsetX=0.212015, 
    viewOffsetY=-0.0520342)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.04802, 
    farPlane=3.13998, width=0.848171, height=0.525388, viewOffsetX=0.211582, 
    viewOffsetY=-0.0519278)
session.viewports['Viewport: 1'].view.setValues(farPlane=3.13998)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-31'].faces
f2 = a1.instances['Cap-1'].faces
a1.FaceToFace(movablePlane=f1[2], fixedPlane=f2[37], flip=ON, clearance=0.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.05022, 
    farPlane=3.16675, width=0.84908, height=0.525951, cameraPosition=(-2.09573, 
    0.485429, 0.657372), cameraUpVector=(0.0265734, 0.12783, -0.99144), 
    cameraTarget=(0.198207, 0.0090503, -0.178912), viewOffsetX=0.211809, 
    viewOffsetY=-0.0519835)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.0588, 
    farPlane=3.15817, width=0.85612, height=0.530312, viewOffsetX=0.216294, 
    viewOffsetY=-0.066688)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.04064, 
    farPlane=3.14692, width=0.848572, height=0.525636, cameraPosition=(
    -2.06229, 0.438322, -0.981806), cameraUpVector=(0.609619, 0.134742, 
    -0.781159), cameraTarget=(0.286345, 0.0061299, -0.284959), 
    viewOffsetX=0.214387, viewOffsetY=-0.0661001)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-32'].faces
f2 = a1.instances['Cap-1'].faces
a1.FaceToFace(movablePlane=f1[2], fixedPlane=f2[37], flip=ON, clearance=0.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.14086, 
    farPlane=3.20242, width=0.890248, height=0.551452, cameraPosition=(
    -1.38283, 1.89777, 0.838698), cameraUpVector=(-0.0783473, 0.0129087, 
    -0.996843), cameraTarget=(0.0968549, 0.149438, -0.132055), 
    viewOffsetX=0.224916, viewOffsetY=-0.0693465)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.15368, 
    farPlane=3.18961, width=0.746897, height=0.462655, viewOffsetX=0.195659, 
    viewOffsetY=-0.0736555)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.11575, 
    farPlane=3.21671, width=0.733742, height=0.454507, cameraPosition=(
    -1.52004, 1.40503, -1.51162), cameraUpVector=(0.805809, -0.0477401, 
    -0.590248), cameraTarget=(0.251523, 0.0666597, -0.389647), 
    viewOffsetX=0.192213, viewOffsetY=-0.0723583)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-28'].faces
f2 = a1.instances['Cap-1'].faces
a1.FaceToFace(movablePlane=f1[2], fixedPlane=f2[37], flip=ON, clearance=0.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.17915, 
    farPlane=3.16415, width=0.75573, height=0.468127, cameraPosition=(-1.01244, 
    1.88278, 1.34145), cameraUpVector=(-0.0627328, 0.298243, -0.952426), 
    cameraTarget=(0.10076, 0.210753, -0.126058), viewOffsetX=0.197973, 
    viewOffsetY=-0.0745266)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.16621, 
    farPlane=3.17509, width=0.751243, height=0.465347, cameraPosition=(
    -1.60406, 1.89682, -0.457416), cameraUpVector=(0.512139, -0.0260426, 
    -0.858508), cameraTarget=(0.154234, 0.142309, -0.32114), 
    viewOffsetX=0.196798, viewOffsetY=-0.0740841)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-27'].faces
f2 = a1.instances['Cap-1'].faces
a1.FaceToFace(movablePlane=f1[2], fixedPlane=f2[37], flip=ON, clearance=0.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.20788, 
    farPlane=3.1426, width=0.765694, height=0.474299, cameraPosition=(
    -0.776936, 1.95166, 1.46225), cameraUpVector=(-0.0686756, 0.341966, 
    -0.937199), cameraTarget=(0.108149, 0.240585, -0.111702), 
    viewOffsetX=0.200584, viewOffsetY=-0.0755092)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.20778, 
    farPlane=3.16078, width=0.76566, height=0.474277, cameraPosition=(-1.20131, 
    2.24128, -0.642886), cameraUpVector=(0.546187, -0.160675, -0.822109), 
    cameraTarget=(0.166913, 0.185756, -0.340758), viewOffsetX=0.200575, 
    viewOffsetY=-0.0755058)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-26'].faces
f2 = a1.instances['Cap-1'].faces
a1.FaceToFace(movablePlane=f1[2], fixedPlane=f2[37], flip=ON, clearance=0.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.28934, 
    farPlane=3.10194, width=0.793943, height=0.491797, cameraPosition=(
    -0.540422, 2.61504, 0.365923), cameraUpVector=(0.229186, -0.0392331, 
    -0.972592), cameraTarget=(0.147764, 0.300205, -0.231094), 
    viewOffsetX=0.207984, viewOffsetY=-0.078295)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.29375, 
    farPlane=3.09752, width=0.809036, height=0.501147, viewOffsetX=0.20206, 
    viewOffsetY=-0.0813863)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.27808, 
    farPlane=3.13318, width=0.803509, height=0.497723, cameraPosition=(
    -0.439201, 2.31668, -1.49261), cameraUpVector=(0.492393, -0.579537, 
    -0.649374), cameraTarget=(0.199488, 0.184227, -0.382115), 
    viewOffsetX=0.200679, viewOffsetY=-0.0808302)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-25'].faces
f2 = a1.instances['Cap-1'].faces
a1.FaceToFace(movablePlane=f1[2], fixedPlane=f2[37], flip=ON, clearance=0.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.32847, 
    farPlane=3.10524, width=0.821283, height=0.508732, cameraPosition=(
    0.587478, 2.5806, 1.01818), cameraUpVector=(-0.13308, 0.139266, -0.981272), 
    cameraTarget=(0.210145, 0.384275, -0.0873804), viewOffsetX=0.205118, 
    viewOffsetY=-0.0826181)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.33505, 
    farPlane=3.09866, width=0.774187, height=0.47956, viewOffsetX=0.202316, 
    viewOffsetY=-0.0893852)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.3306, 
    farPlane=3.11845, width=0.772711, height=0.478645, cameraPosition=(
    0.628983, 2.41993, -1.57221), cameraUpVector=(-0.0334149, -0.755229, 
    -0.654608), cameraTarget=(0.223694, 0.28712, -0.357576), 
    viewOffsetX=0.20193, viewOffsetY=-0.0892147)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-24'].faces
f2 = a1.instances['Cap-1'].faces
a1.FaceToFace(movablePlane=f1[2], fixedPlane=f2[37], flip=ON, clearance=0.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.28507, 
    farPlane=3.1739, width=0.757616, height=0.469295, cameraPosition=(1.19887, 
    2.60874, 0.652135), cameraUpVector=(0.28014, -0.114142, -0.953149), 
    cameraTarget=(0.342504, 0.437885, -0.209546), viewOffsetX=0.197985, 
    viewOffsetY=-0.0874719)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.31099, 
    farPlane=3.14741, width=0.76621, height=0.474619, cameraPosition=(0.868196, 
    2.39363, -1.56212), cameraUpVector=(0.158768, -0.770785, -0.616995), 
    cameraTarget=(0.276331, 0.271359, -0.407079), viewOffsetX=0.200231, 
    viewOffsetY=-0.0884642)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-23'].faces
f2 = a1.instances['Cap-1'].faces
a1.FaceToFace(movablePlane=f1[2], fixedPlane=f2[37], flip=ON, clearance=0.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.25549, 
    farPlane=3.21088, width=0.747811, height=0.463221, cameraPosition=(1.43002, 
    2.42085, 0.919969), cameraUpVector=(0.349185, -0.0802357, -0.933612), 
    cameraTarget=(0.392476, 0.449304, -0.186805), viewOffsetX=0.195422, 
    viewOffsetY=-0.0863397)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.26055, 
    farPlane=3.20582, width=0.752554, height=0.46616, viewOffsetX=0.202715, 
    viewOffsetY=-0.0924037)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.29098, 
    farPlane=3.15824, width=0.762684, height=0.472434, cameraPosition=(0.91228, 
    2.17892, -1.83632), cameraUpVector=(0.0513164, -0.84072, -0.539033), 
    cameraTarget=(0.26205, 0.242554, -0.416412), viewOffsetX=0.205444, 
    viewOffsetY=-0.0936475)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-22'].faces
f2 = a1.instances['Cap-1'].faces
a1.FaceToFace(movablePlane=f1[2], fixedPlane=f2[37], flip=ON, clearance=0.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.24261, 
    farPlane=3.2213, width=0.746581, height=0.462459, cameraPosition=(1.54807, 
    1.83977, 1.65601), cameraUpVector=(0.557075, 0.0270848, -0.83002), 
    cameraTarget=(0.476568, 0.450378, -0.107488), viewOffsetX=0.201106, 
    viewOffsetY=-0.0916702)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.27047, 
    farPlane=3.19563, width=0.755855, height=0.468204, cameraPosition=(1.29032, 
    2.39287, -1.34872), cameraUpVector=(0.0336313, -0.726168, -0.686694), 
    cameraTarget=(0.308772, 0.311646, -0.403456), viewOffsetX=0.203604, 
    viewOffsetY=-0.0928089)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-19'].faces
f2 = a1.instances['Cap-1'].faces
a1.FaceToFace(movablePlane=f1[2], fixedPlane=f2[37], flip=ON, clearance=0.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.20581, 
    farPlane=3.27812, width=0.73433, height=0.454871, cameraPosition=(2.059, 
    2.04972, 0.869243), cameraUpVector=(0.175236, -0.056112, -0.982926), 
    cameraTarget=(0.45937, 0.451876, -0.168326), viewOffsetX=0.197806, 
    viewOffsetY=-0.090166)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.21132, 
    farPlane=3.27262, width=0.736164, height=0.456007, viewOffsetX=0.200679, 
    viewOffsetY=-0.0897196)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.28075, 
    farPlane=3.18831, width=0.759279, height=0.470325, cameraPosition=(1.11635, 
    2.41016, -1.43259), cameraUpVector=(-0.410507, -0.604042, -0.683094), 
    cameraTarget=(0.24495, 0.365667, -0.314917), viewOffsetX=0.20698, 
    viewOffsetY=-0.0925367)
a1 = mdb.models['Model-1'].rootAssembly
f1 = a1.instances['Bolt-18'].faces
f2 = a1.instances['Cap-1'].faces
a1.FaceToFace(movablePlane=f1[2], fixedPlane=f2[37], flip=ON, clearance=0.0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.23713, 
    farPlane=3.23193, width=1.30508, height=0.808415, viewOffsetX=0.23309, 
    viewOffsetY=-0.0225939)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.24518, 
    farPlane=3.35596, width=1.30977, height=0.811322, cameraPosition=(1.64357, 
    1.30786, -2.33022), cameraUpVector=(-0.546618, -0.759736, -0.352151), 
    cameraTarget=(0.32464, 0.305227, -0.47452), viewOffsetX=0.233929, 
    viewOffsetY=-0.0226751)
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'Flange-1', 'Long_Side-1', 'Short Side-1', 'Long_Side-2', 'Bottom-1', 
    'Short Side With Holes-1', ))
session.viewports['Viewport: 1'].assemblyDisplay.hideInstances(instances=(
    'Cap-1', ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.29962, 
    farPlane=3.27093, width=1.05169, height=0.651454, viewOffsetX=0.242318, 
    viewOffsetY=-0.0603568)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Bolt-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#10 ]', ), )
s2 = a.instances['Bolt-2'].faces
side1Faces2 = s2.getSequenceFromMask(mask=('[#10 ]', ), )
s3 = a.instances['Bolt-3'].faces
side1Faces3 = s3.getSequenceFromMask(mask=('[#10 ]', ), )
s4 = a.instances['Bolt-4'].faces
side1Faces4 = s4.getSequenceFromMask(mask=('[#10 ]', ), )
s5 = a.instances['Bolt-28'].faces
side1Faces5 = s5.getSequenceFromMask(mask=('[#10 ]', ), )
s6 = a.instances['Bolt-27'].faces
side1Faces6 = s6.getSequenceFromMask(mask=('[#10 ]', ), )
s7 = a.instances['Bolt-26'].faces
side1Faces7 = s7.getSequenceFromMask(mask=('[#10 ]', ), )
s8 = a.instances['Bolt-25'].faces
side1Faces8 = s8.getSequenceFromMask(mask=('[#10 ]', ), )
s9 = a.instances['Bolt-24'].faces
side1Faces9 = s9.getSequenceFromMask(mask=('[#10 ]', ), )
s10 = a.instances['Bolt-23'].faces
side1Faces10 = s10.getSequenceFromMask(mask=('[#10 ]', ), )
s11 = a.instances['Bolt-22'].faces
side1Faces11 = s11.getSequenceFromMask(mask=('[#10 ]', ), )
s12 = a.instances['Bolt-19'].faces
side1Faces12 = s12.getSequenceFromMask(mask=('[#10 ]', ), )
s13 = a.instances['Bolt-18'].faces
side1Faces13 = s13.getSequenceFromMask(mask=('[#10 ]', ), )
s14 = a.instances['Bolt-12'].faces
side1Faces14 = s14.getSequenceFromMask(mask=('[#10 ]', ), )
s15 = a.instances['Bolt-13'].faces
side1Faces15 = s15.getSequenceFromMask(mask=('[#10 ]', ), )
s16 = a.instances['Bolt-14'].faces
side1Faces16 = s16.getSequenceFromMask(mask=('[#10 ]', ), )
s17 = a.instances['Bolt-15'].faces
side1Faces17 = s17.getSequenceFromMask(mask=('[#10 ]', ), )
s18 = a.instances['Bolt-16'].faces
side1Faces18 = s18.getSequenceFromMask(mask=('[#10 ]', ), )
s19 = a.instances['Bolt-17'].faces
side1Faces19 = s19.getSequenceFromMask(mask=('[#10 ]', ), )
s20 = a.instances['Bolt-29'].faces
side1Faces20 = s20.getSequenceFromMask(mask=('[#10 ]', ), )
s21 = a.instances['Bolt-30'].faces
side1Faces21 = s21.getSequenceFromMask(mask=('[#10 ]', ), )
s22 = a.instances['Bolt-31'].faces
side1Faces22 = s22.getSequenceFromMask(mask=('[#10 ]', ), )
s23 = a.instances['Bolt-32'].faces
side1Faces23 = s23.getSequenceFromMask(mask=('[#10 ]', ), )
s24 = a.instances['Bolt-20'].faces
side1Faces24 = s24.getSequenceFromMask(mask=('[#10 ]', ), )
s25 = a.instances['Bolt-21'].faces
side1Faces25 = s25.getSequenceFromMask(mask=('[#10 ]', ), )
s26 = a.instances['Bolt-5'].faces
side1Faces26 = s26.getSequenceFromMask(mask=('[#10 ]', ), )
s27 = a.instances['Bolt-6'].faces
side1Faces27 = s27.getSequenceFromMask(mask=('[#10 ]', ), )
s28 = a.instances['Bolt-7'].faces
side1Faces28 = s28.getSequenceFromMask(mask=('[#10 ]', ), )
s29 = a.instances['Bolt-8'].faces
side1Faces29 = s29.getSequenceFromMask(mask=('[#10 ]', ), )
s30 = a.instances['Bolt-9'].faces
side1Faces30 = s30.getSequenceFromMask(mask=('[#10 ]', ), )
s31 = a.instances['Bolt-10'].faces
side1Faces31 = s31.getSequenceFromMask(mask=('[#10 ]', ), )
s32 = a.instances['Bolt-11'].faces
side1Faces32 = s32.getSequenceFromMask(mask=('[#10 ]', ), )
a.Surface(side1Faces=side1Faces1+side1Faces2+side1Faces3+side1Faces4+\
    side1Faces5+side1Faces6+side1Faces7+side1Faces8+side1Faces9+side1Faces10+\
    side1Faces11+side1Faces12+side1Faces13+side1Faces14+side1Faces15+\
    side1Faces16+side1Faces17+side1Faces18+side1Faces19+side1Faces20+\
    side1Faces21+side1Faces22+side1Faces23+side1Faces24+side1Faces25+\
    side1Faces26+side1Faces27+side1Faces28+side1Faces29+side1Faces30+\
    side1Faces31+side1Faces32, name='Bolt_Flange_Slave_Surface')
#: The surface 'Bolt_Flange_Slave_Surface' has been edited (32 faces).
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.34254, 
    farPlane=3.27881, width=1.07131, height=0.663611, cameraPosition=(2.0417, 
    0.256845, 2.12321), cameraUpVector=(0.076621, 0.855893, -0.511445), 
    cameraTarget=(0.427984, 0.238848, 0.230047), viewOffsetX=0.246841, 
    viewOffsetY=-0.0614832)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.33859, 
    farPlane=3.28275, width=1.16124, height=0.719314, viewOffsetX=0.184387, 
    viewOffsetY=0.0553205)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Bolt-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#4 ]', ), )
s2 = a.instances['Bolt-2'].faces
side1Faces2 = s2.getSequenceFromMask(mask=('[#4 ]', ), )
s3 = a.instances['Bolt-3'].faces
side1Faces3 = s3.getSequenceFromMask(mask=('[#4 ]', ), )
s4 = a.instances['Bolt-4'].faces
side1Faces4 = s4.getSequenceFromMask(mask=('[#4 ]', ), )
s5 = a.instances['Bolt-11'].faces
side1Faces5 = s5.getSequenceFromMask(mask=('[#4 ]', ), )
s6 = a.instances['Bolt-9'].faces
side1Faces6 = s6.getSequenceFromMask(mask=('[#4 ]', ), )
s7 = a.instances['Bolt-10'].faces
side1Faces7 = s7.getSequenceFromMask(mask=('[#4 ]', ), )
s8 = a.instances['Bolt-21'].faces
side1Faces8 = s8.getSequenceFromMask(mask=('[#4 ]', ), )
s9 = a.instances['Bolt-20'].faces
side1Faces9 = s9.getSequenceFromMask(mask=('[#4 ]', ), )
s10 = a.instances['Bolt-12'].faces
side1Faces10 = s10.getSequenceFromMask(mask=('[#4 ]', ), )
s11 = a.instances['Bolt-13'].faces
side1Faces11 = s11.getSequenceFromMask(mask=('[#4 ]', ), )
s12 = a.instances['Bolt-14'].faces
side1Faces12 = s12.getSequenceFromMask(mask=('[#4 ]', ), )
s13 = a.instances['Bolt-15'].faces
side1Faces13 = s13.getSequenceFromMask(mask=('[#4 ]', ), )
s14 = a.instances['Bolt-16'].faces
side1Faces14 = s14.getSequenceFromMask(mask=('[#4 ]', ), )
s15 = a.instances['Bolt-8'].faces
side1Faces15 = s15.getSequenceFromMask(mask=('[#4 ]', ), )
s16 = a.instances['Bolt-7'].faces
side1Faces16 = s16.getSequenceFromMask(mask=('[#4 ]', ), )
s17 = a.instances['Bolt-6'].faces
side1Faces17 = s17.getSequenceFromMask(mask=('[#4 ]', ), )
s18 = a.instances['Bolt-5'].faces
side1Faces18 = s18.getSequenceFromMask(mask=('[#4 ]', ), )
s19 = a.instances['Bolt-18'].faces
side1Faces19 = s19.getSequenceFromMask(mask=('[#4 ]', ), )
s20 = a.instances['Bolt-19'].faces
side1Faces20 = s20.getSequenceFromMask(mask=('[#4 ]', ), )
s21 = a.instances['Bolt-22'].faces
side1Faces21 = s21.getSequenceFromMask(mask=('[#4 ]', ), )
s22 = a.instances['Bolt-23'].faces
side1Faces22 = s22.getSequenceFromMask(mask=('[#4 ]', ), )
s23 = a.instances['Bolt-24'].faces
side1Faces23 = s23.getSequenceFromMask(mask=('[#4 ]', ), )
s24 = a.instances['Bolt-25'].faces
side1Faces24 = s24.getSequenceFromMask(mask=('[#4 ]', ), )
s25 = a.instances['Bolt-26'].faces
side1Faces25 = s25.getSequenceFromMask(mask=('[#4 ]', ), )
s26 = a.instances['Bolt-27'].faces
side1Faces26 = s26.getSequenceFromMask(mask=('[#4 ]', ), )
s27 = a.instances['Bolt-28'].faces
side1Faces27 = s27.getSequenceFromMask(mask=('[#4 ]', ), )
s28 = a.instances['Bolt-32'].faces
side1Faces28 = s28.getSequenceFromMask(mask=('[#4 ]', ), )
s29 = a.instances['Bolt-31'].faces
side1Faces29 = s29.getSequenceFromMask(mask=('[#4 ]', ), )
s30 = a.instances['Bolt-30'].faces
side1Faces30 = s30.getSequenceFromMask(mask=('[#4 ]', ), )
s31 = a.instances['Bolt-29'].faces
side1Faces31 = s31.getSequenceFromMask(mask=('[#4 ]', ), )
s32 = a.instances['Bolt-17'].faces
side1Faces32 = s32.getSequenceFromMask(mask=('[#4 ]', ), )
a.Surface(side1Faces=side1Faces1+side1Faces2+side1Faces3+side1Faces4+\
    side1Faces5+side1Faces6+side1Faces7+side1Faces8+side1Faces9+side1Faces10+\
    side1Faces11+side1Faces12+side1Faces13+side1Faces14+side1Faces15+\
    side1Faces16+side1Faces17+side1Faces18+side1Faces19+side1Faces20+\
    side1Faces21+side1Faces22+side1Faces23+side1Faces24+side1Faces25+\
    side1Faces26+side1Faces27+side1Faces28+side1Faces29+side1Faces30+\
    side1Faces31+side1Faces32, name='Bolts_Top_Constraint_Surface')
#: The surface 'Bolts_Top_Constraint_Surface' has been edited (32 faces).
mdb.jobs['Pressure_Box_With_Holes'].submit(consistencyChecking=OFF)
#: The job input file "Pressure_Box_With_Holes.inp" has been submitted for analysis.
#: Job Pressure_Box_With_Holes: Analysis Input File Processor completed successfully.
#: Job Pressure_Box_With_Holes: Abaqus/Standard completed successfully.
#: Job Pressure_Box_With_Holes completed successfully. 
o3 = session.openOdb(
    name='C:/Users/chs17004/Desktop/Abaqus Pressure Vessel/Pressure Box with Bolts/Pressure_Box_With_Holes.odb')
#: Model: C:/Users/chs17004/Desktop/Abaqus Pressure Vessel/Pressure Box with Bolts/Pressure_Box_With_Holes.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     39
#: Number of Meshes:             39
#: Number of Element Sets:       59
#: Number of Node Sets:          61
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.56853, 
    farPlane=2.7132, width=0.991538, height=0.614195, cameraPosition=(1.87543, 
    -1.29004, -0.704939), cameraUpVector=(-0.794548, -0.0876609, -0.60084), 
    cameraTarget=(0.403988, 0.0917637, -0.125748))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.55654, 
    farPlane=2.72666, width=0.983961, height=0.609501, cameraPosition=(2.08028, 
    -0.573628, -1.20868), cameraUpVector=(-0.826328, -0.143401, -0.544627), 
    cameraTarget=(0.407898, 0.10544, -0.135364))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
mdb.models['Model-1'].loads['Cap_Pressure'].resume()
session.viewports['Viewport: 1'].assemblyDisplay.showInstances(instances=(
    'Cap-1', ))
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Cap-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#0 #10 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Cap Bottom Surface')
#: The surface 'Cap Bottom Surface' has been edited (1 face).
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.jobs['Pressure_Box_With_Holes'].submit(consistencyChecking=OFF)
#: The job input file "Pressure_Box_With_Holes.inp" has been submitted for analysis.
#: Job Pressure_Box_With_Holes: Analysis Input File Processor completed successfully.
#: Job Pressure_Box_With_Holes: Abaqus/Standard completed successfully.
#: Job Pressure_Box_With_Holes completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/chs17004/Desktop/Abaqus Pressure Vessel/Pressure Box with Bolts/Pressure_Box_With_Holes.odb'])
#: Warning: The output database 'C:/Users/chs17004/Desktop/Abaqus Pressure Vessel/Pressure Box with Bolts/Pressure_Box_With_Holes.odb' disk file has changed.
#: 
#: The current plot operation has been canceled, re-open the file to view the results
o3 = session.openOdb(
    name='C:/Users/chs17004/Desktop/Abaqus Pressure Vessel/Pressure Box with Bolts/Pressure_Box_With_Holes.odb')
#: Model: C:/Users/chs17004/Desktop/Abaqus Pressure Vessel/Pressure Box with Bolts/Pressure_Box_With_Holes.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     39
#: Number of Meshes:             39
#: Number of Element Sets:       59
#: Number of Node Sets:          61
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.59529, 
    farPlane=2.64922, width=1.00846, height=0.624675, cameraPosition=(1.8889, 
    0.0431051, -1.64567), cameraUpVector=(-0.71217, 0.65514, -0.252201), 
    cameraTarget=(0.407322, 0.0738259, -0.15773))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.60371, 
    farPlane=2.71736, width=1.01378, height=0.627973, cameraPosition=(2.06819, 
    -1.19882, -0.411405), cameraUpVector=(-0.208533, 0.463378, -0.861275), 
    cameraTarget=(0.409203, 0.0607994, -0.144784))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.57045, 
    farPlane=2.72725, width=0.992758, height=0.61495, cameraPosition=(1.88811, 
    -0.936139, -1.26377), cameraUpVector=(-0.507128, 0.610761, -0.608106), 
    cameraTarget=(0.404157, 0.0681596, -0.168667))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.58823, 
    farPlane=2.6849, width=1.004, height=0.621914, cameraPosition=(2.26437, 
    1.10372, -0.0883776), cameraUpVector=(-0.586465, 0.427408, -0.688027), 
    cameraTarget=(0.412712, 0.114541, -0.141942))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.60334, 
    farPlane=2.66674, width=1.01355, height=0.627831, cameraPosition=(1.44987, 
    -0.903367, -1.69849), cameraUpVector=(-0.874474, 0.329942, -0.355574), 
    cameraTarget=(0.398769, 0.080184, -0.169504))
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
p1 = mdb.models['Model-1'].parts['Cap']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['Cap']
p.deleteMesh()
p = mdb.models['Model-1'].parts['Cap']
p.seedPart(size=0.1, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Cap']
p.generateMesh()
p1 = mdb.models['Model-1'].parts['Long_Side']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['Long_Side']
p.deleteMesh()
p = mdb.models['Model-1'].parts['Long_Side']
p.seedPart(size=0.025, deviationFactor=0.1, minSizeFactor=0.1)
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
p1 = mdb.models['Model-1'].parts['Long_Side']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['Long_Side']
p.generateMesh()
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.jobs['Pressure_Box_With_Holes'].submit(consistencyChecking=OFF)
#: The job input file "Pressure_Box_With_Holes.inp" has been submitted for analysis.
#: Error in job Pressure_Box_With_Holes: Normal cannot be computed in 22 elements. The nodal coordinates may be incorrect or the element aspect ratio may exceed 1000 to 1. The elements have been identified in element set ErrElemNormal.
#: Error in job Pressure_Box_With_Holes: The geometry of 8 elements is too distorted. Check the nodal coordinates or node numbering on elements identified in element set ErrElemDistorted.
#: Error in job Pressure_Box_With_Holes: The area of 6 elements is zero, small, or negative. Check coordinates or node numbering, or modify the mesh seed. The elements have been identified in element set ErrElemAreaSmallNegZero.
#: Error in job Pressure_Box_With_Holes: Error in defining normal to the element surface at a node in 22 elements. The elements have been identified in element set ErrElemShellNormal.
#: Job Pressure_Box_With_Holes: Analysis Input File Processor aborted due to errors.
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/chs17004/Desktop/Abaqus Pressure Vessel/Pressure Box with Bolts/Pressure_Box_With_Holes.odb'])
o3 = session.openOdb(
    name='C:/Users/chs17004/Desktop/Abaqus Pressure Vessel/Pressure Box with Bolts/Pressure_Box_With_Holes.odb')
#* OdbError: The .lck file for the output database 
#* C:/Users/chs17004/Desktop/Abaqus Pressure Vessel/Pressure Box with 
#* Bolts/Pressure_Box_With_Holes.odb indicates that the Analysis Input File 
#* Processor is currently modifying the database.  The database cannot be 
#* opened at this time.
#: Warning: The output database 'C:/Users/chs17004/Desktop/Abaqus Pressure Vessel/Pressure Box with Bolts/Pressure_Box_With_Holes.odb' disk file has changed.
#: 
#: The current plot operation has been canceled, re-open the file to view the results
#: Error in job Pressure_Box_With_Holes: Analysis Input File Processor exited with an error.
#: Job Pressure_Box_With_Holes aborted due to errors.
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
p1 = mdb.models['Model-1'].parts['Long_Side']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['Long_Side']
p.deleteMesh()
p = mdb.models['Model-1'].parts['Long_Side']
p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
p1 = mdb.models['Model-1'].parts['Long_Side']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
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
f = p.faces
pickedRegions = f.getSequenceFromMask(mask=('[#2 ]', ), )
p.generateMesh(regions=pickedRegions)
p = mdb.models['Model-1'].parts['Bottom']
f = p.faces
pickedRegions = f.getSequenceFromMask(mask=('[#1 ]', ), )
p.generateMesh(regions=pickedRegions)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.66014, 
    farPlane=1.84077, width=1.08551, height=0.673666, viewOffsetX=0.101504, 
    viewOffsetY=0.029367)
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.jobs['Pressure_Box_With_Holes'].submit(consistencyChecking=OFF)
#: The job input file "Pressure_Box_With_Holes.inp" has been submitted for analysis.
#: Job Pressure_Box_With_Holes: Analysis Input File Processor completed successfully.
#: Job Pressure_Box_With_Holes: Abaqus/Standard completed successfully.
#: Job Pressure_Box_With_Holes completed successfully. 
o3 = session.openOdb(
    name='C:/Users/chs17004/Desktop/Abaqus Pressure Vessel/Pressure Box with Bolts/Pressure_Box_With_Holes.odb')
#: Model: C:/Users/chs17004/Desktop/Abaqus Pressure Vessel/Pressure Box with Bolts/Pressure_Box_With_Holes.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     39
#: Number of Meshes:             39
#: Number of Element Sets:       59
#: Number of Node Sets:          61
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.62264, 
    farPlane=2.69633, width=1.02575, height=0.635385, cameraPosition=(1.64094, 
    -1.5282, -0.754945), cameraUpVector=(-0.146033, 0.621969, -0.769304), 
    cameraTarget=(0.404712, 0.0572898, -0.148352))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.646, 
    farPlane=2.6427, width=1.04052, height=0.644536, cameraPosition=(1.14888, 
    -1.201, -1.66672), cameraUpVector=(-0.261969, 0.875122, -0.406858), 
    cameraTarget=(0.391156, 0.0663037, -0.17347))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.73737, 
    farPlane=2.5255, width=1.09828, height=0.680316, cameraPosition=(0.669056, 
    -0.529648, -2.17272), cameraUpVector=(-0.166558, 0.985699, 0.0256181), 
    cameraTarget=(0.381231, 0.0801898, -0.183936))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.76903, 
    farPlane=2.49385, width=0.640778, height=0.396921, viewOffsetX=-0.0720495, 
    viewOffsetY=0.0730231)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p1 = mdb.models['Model-1'].parts['Bolt']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['Bolt']
s = p.features['Solid revolve-1'].sketch
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=s)
s1 = mdb.models['Model-1'].sketches['__edit__']
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s1, 
    upToFeature=p.features['Solid revolve-1'], filter=COPLANAR_EDGES)
s1.ObliqueDimension(vertex1=v[1], vertex2=v[2], textPoint=(0.0172356441617012, 
    0.0245458353310823), value=0.04)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0695115, 
    farPlane=0.134479, width=0.213294, height=0.132122, cameraPosition=(
    -0.000506867, 0.0139789, 0.101995), cameraTarget=(-0.000506867, 0.0139789, 
    0))
s1.DistanceDimension(entity1=g[4], entity2=g[2], textPoint=(
    0.00398248061537743, 0.0784868448972702), value=0.1)
session.viewports['Viewport: 1'].view.setValues(width=0.200496, 
    height=0.124195, cameraPosition=(0.0051249, -0.00302685, 0.101995), 
    cameraTarget=(0.0051249, -0.00302685, 0))
s1.dragEntity(entity=v[9], points=((0.0, -0.0136910080909729), (0.0, -0.0125), 
    (0.0, -0.025), (0.0, -0.0331109762191772), (0.0, -0.0353008136153221), (
    0.0, -0.0375), (0.0, -0.0389505326747894), (0.0, -0.0413489192724228), (
    0.0, -0.0429130867123604)))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0605277, 
    farPlane=0.143463, width=0.34991, height=0.216747, cameraPosition=(
    0.000266981, 0.0156832, 0.101995), cameraTarget=(0.000266981, 0.0156832, 
    0))
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__edit__']
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.30133, 
    farPlane=3.32002, width=1.55706, height=0.964502, viewOffsetX=0.201197, 
    viewOffsetY=0.0630645)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.26472, 
    farPlane=3.31907, width=1.53229, height=0.949159, cameraPosition=(-1.21323, 
    1.23317, 1.88356), cameraUpVector=(0.703431, 0.6601, -0.263539), 
    cameraTarget=(0.0462469, 0.364138, -0.0778067), viewOffsetX=0.197997, 
    viewOffsetY=0.0620613)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.44358, 
    farPlane=3.31702, width=1.65331, height=1.02412, cameraPosition=(-0.278391, 
    2.51131, -1.61992), cameraUpVector=(0.66789, -0.552993, -0.498118), 
    cameraTarget=(0.122417, 0.387056, -0.388919), viewOffsetX=0.213634, 
    viewOffsetY=0.0669627)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.44795, 
    farPlane=3.30864, width=1.65627, height=1.02595, cameraPosition=(-0.144646, 
    2.30158, -1.95627), cameraUpVector=(0.647142, -0.64842, -0.400947), 
    cameraTarget=(0.138123, 0.359627, -0.427434), viewOffsetX=0.214016, 
    viewOffsetY=0.0670825)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.55396, 
    farPlane=3.20264, width=0.416374, height=0.257917, viewOffsetX=0.232029, 
    viewOffsetY=0.089367)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.57828, 
    farPlane=3.2024, width=0.420339, height=0.260373, cameraPosition=(0.457106, 
    2.05039, -2.30006), cameraUpVector=(0.551966, -0.80415, -0.220626), 
    cameraTarget=(0.216619, 0.35824, -0.492498), viewOffsetX=0.234238, 
    viewOffsetY=0.090218)
p1 = mdb.models['Model-1'].parts['Cap']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
#: 
#: Point 1: 239.262E-03, -363.46E-03, 12.7E-03  Point 2: 229.262E-03, -363.46E-03, 12.7E-03
#:    Distance: 10.E-03  Components: -10.E-03, 0., 0.
#: 
#: Point 1: 229.262E-03, -363.46E-03, 12.7E-03  Point 2: 239.262E-03, -363.46E-03, 12.7E-03
#:    Distance: 10.E-03  Components: 10.E-03, 0., 0.
#: 
#: Point 1: 229.262E-03, -363.46E-03, 12.7E-03  Point 2: 239.262E-03, -363.46E-03, 12.7E-03
#:    Distance: 10.E-03  Components: 10.E-03, 0., 0.
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.64075, 
    farPlane=2.00622, width=0.0664475, height=0.04116, cameraPosition=(0.66841, 
    -1.05124, 1.61058), cameraTarget=(0.242665, -0.343398, -0.0150855))
p1 = mdb.models['Model-1'].parts['Bolt']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['Bolt']
s = p.features['Solid revolve-1'].sketch
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=s)
s2 = mdb.models['Model-1'].sketches['__edit__']
g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
s2.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s2, 
    upToFeature=p.features['Solid revolve-1'], filter=COPLANAR_EDGES)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0804663, 
    farPlane=0.123524, width=0.109064, height=0.0626234, cameraPosition=(
    0.0144468, 0.0010375, 0.101995), cameraTarget=(0.0144468, 0.0010375, 0))
s2.ObliqueDimension(vertex1=v[1], vertex2=v[2], textPoint=(0.019650099799037, 
    0.0249183420091867), value=0.00381)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0786246, 
    farPlane=0.125366, width=0.13131, height=0.0753969, cameraPosition=(
    0.0170065, 0.00494868, 0.101995), cameraTarget=(0.0170065, 0.00494868, 0))
s2.ObliqueDimension(vertex1=v[0], vertex2=v[1], textPoint=(0.00662695243954659, 
    0.0343834981322289), value=0.006)
d[3].setValues(value=0.0285, )
d[2].setValues(value=0.0127, )
s2.dragEntity(entity=v[9], points=((0.0, -0.0136910080909729), (0.0, 
    -0.0136910080909729), (0.0, -0.0216860733926296), (0.0, -0.025), (
    0.000915132462978363, -0.0282423235476017), (0.000976551324129105, 
    -0.0296082086861134), (0.0, -0.0309057980775833)))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0746226, 
    farPlane=0.129368, width=0.158741, height=0.0911471, cameraPosition=(
    0.0255759, -0.0132186, 0.101995), cameraTarget=(0.0255759, -0.0132186, 0))
s2.dragEntity(entity=v[9], points=((0.0, -0.0309057980775833), (0.0, 
    -0.0309057980775833), (0.0, -0.0339413061738014), (0.0, 
    -0.0353448390960693), (0.0, -0.0375), (0.0, -0.0375)))
s2.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Bolt']
p.features['Solid revolve-1'].setValues(sketch=s2)
del mdb.models['Model-1'].sketches['__edit__']
p = mdb.models['Model-1'].parts['Bolt']
p.regenerate()
#: Warning: Failed to attach mesh to part geometry.
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0651264, 
    farPlane=0.186398, width=0.0965881, height=0.0554597, 
    viewOffsetX=0.0109137, viewOffsetY=-0.00201618)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0788818, 
    farPlane=0.202206, width=0.116989, height=0.0671734, cameraPosition=(
    0.080336, 0.0630186, 0.092863), cameraUpVector=(-0.638348, 0.66763, 
    -0.383122), cameraTarget=(0.000799038, 0.00321364, 0.00657111), 
    viewOffsetX=0.0132188, viewOffsetY=-0.00244201)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0684797, 
    farPlane=0.173141, width=0.101562, height=0.0583156, cameraPosition=(
    -0.0857939, 0.00683206, 0.08704), cameraUpVector=(-0.0290698, 0.865315, 
    -0.500385), cameraTarget=(-0.0119294, -0.00276641, -0.0215922), 
    viewOffsetX=0.0114757, viewOffsetY=-0.00211998)
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.54963, 
    farPlane=3.22368, width=0.611011, height=0.350835, viewOffsetX=0.271026, 
    viewOffsetY=0.118721)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.2674, 
    farPlane=3.32107, width=0.543377, height=0.312, cameraPosition=(-1.79927, 
    1.78065, -0.773645), cameraUpVector=(0.410648, -0.409248, -0.814791), 
    cameraTarget=(-0.0166469, 0.185196, -0.091553), viewOffsetX=0.241025, 
    viewOffsetY=0.105579)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.29445, 
    farPlane=3.3079, width=0.549859, height=0.315722, cameraPosition=(-1.58125, 
    1.92136, -1.06508), cameraUpVector=(0.472154, -0.459823, -0.752086), 
    cameraTarget=(-0.0179007, 0.218899, -0.145283), viewOffsetX=0.2439, 
    viewOffsetY=0.106838)
p1 = mdb.models['Model-1'].parts['Bolt']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['Bolt']
s = p.features['Solid revolve-1'].sketch
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=s)
s1 = mdb.models['Model-1'].sketches['__edit__']
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s1, 
    upToFeature=p.features['Solid revolve-1'], filter=COPLANAR_EDGES)
d[2].setValues(value=0.01288, )
d[3].setValues(value=0.015, )
s1.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Bolt']
p.features['Solid revolve-1'].setValues(sketch=s1)
del mdb.models['Model-1'].sketches['__edit__']
p = mdb.models['Model-1'].parts['Bolt']
p.regenerate()
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0777081, 
    farPlane=0.165485, width=0.115249, height=0.0661744, cameraPosition=(
    0.0334423, 0.0510507, 0.105095), cameraUpVector=(-0.108563, 0.743774, 
    -0.659557), cameraTarget=(-0.0238923, 0.00486156, -0.00412202), 
    viewOffsetX=0.0130222, viewOffsetY=-0.00240567)
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0720697, 
    farPlane=0.179598, width=0.106887, height=0.0613731, cameraPosition=(
    0.0139258, 0.108531, 0.0559331), cameraUpVector=(-0.403616, 0.194555, 
    -0.894004), cameraTarget=(-0.0237855, -0.00425254, -0.000696076), 
    viewOffsetX=0.0120773, viewOffsetY=-0.00223112)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Model-1'].parts['Bolt']
p.seedPart(size=0.01, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Bolt']
p.generateMesh()
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0890727, 
    farPlane=0.15617, width=0.132104, height=0.0759948, cameraPosition=(
    -0.0342242, 0.0226256, 0.116732), cameraUpVector=(-0.166659, 0.826763, 
    -0.537297), cameraTarget=(-0.0226732, -0.00526271, -0.0114784), 
    viewOffsetX=0.0149266, viewOffsetY=-0.0027575)
p = mdb.models['Model-1'].parts['Bolt']
p.deleteMesh()
p = mdb.models['Model-1'].parts['Bolt']
p.seedPart(size=0.005, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Bolt']
p.generateMesh()
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.0740558, 
    farPlane=0.173233, width=0.109833, height=0.0631827, cameraPosition=(
    -0.00212269, 0.07108, 0.099416), cameraUpVector=(-0.652468, 0.387184, 
    -0.65144), cameraTarget=(-0.0219614, -0.0143289, 0.00112639), 
    viewOffsetX=0.0124101, viewOffsetY=-0.00229261)
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.jobs['Pressure_Box_With_Holes'].submit(consistencyChecking=OFF)
#: The job input file "Pressure_Box_With_Holes.inp" has been submitted for analysis.
#: Job Pressure_Box_With_Holes: Analysis Input File Processor completed successfully.
#: Job Pressure_Box_With_Holes: Abaqus/Standard completed successfully.
#: Job Pressure_Box_With_Holes completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/chs17004/Desktop/Abaqus Pressure Vessel/Pressure Box with Bolts/Pressure_Box_With_Holes.odb'])
o3 = session.openOdb(
    name='C:/Users/chs17004/Desktop/Abaqus Pressure Vessel/Pressure Box with Bolts/Pressure_Box_With_Holes.odb')
#: Model: C:/Users/chs17004/Desktop/Abaqus Pressure Vessel/Pressure Box with Bolts/Pressure_Box_With_Holes.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     39
#: Number of Meshes:             39
#: Number of Element Sets:       59
#: Number of Node Sets:          61
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.57473, 
    farPlane=2.74367, width=1.07598, height=0.617816, cameraPosition=(2.12944, 
    -1.03876, -0.65254), cameraUpVector=(-0.575392, 0.108759, -0.810614), 
    cameraTarget=(0.409168, 0.0647064, -0.148958))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.58295, 
    farPlane=2.73547, width=0.955698, height=0.54875, viewOffsetX=-0.0019147, 
    viewOffsetY=0.00822067)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.57487, 
    farPlane=2.72975, width=0.950822, height=0.545951, cameraPosition=(1.99563, 
    -0.747665, -1.28095), cameraUpVector=(-0.779713, 0.167365, -0.603355), 
    cameraTarget=(0.408761, 0.0706434, -0.166144), viewOffsetX=-0.00190493, 
    viewOffsetY=0.00817873)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.55443, 
    farPlane=2.71572, width=0.938484, height=0.538866, cameraPosition=(2.1037, 
    0.861111, -1.16418), cameraUpVector=(-0.810507, 0.130618, -0.57098), 
    cameraTarget=(0.412568, 0.103688, -0.165709), viewOffsetX=-0.00188021, 
    viewOffsetY=0.00807259)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.54492, 
    farPlane=2.72523, width=1.12299, height=0.64481, viewOffsetX=0.0111233, 
    viewOffsetY=-0.0059927)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.57695, 
    farPlane=2.69367, width=1.14628, height=0.65818, cameraPosition=(1.82493, 
    0.522015, -1.67369), cameraUpVector=(-0.921992, 0.109276, -0.371469), 
    cameraTarget=(0.409642, 0.0992699, -0.174089), viewOffsetX=0.011354, 
    viewOffsetY=-0.00611696)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.71519, 
    farPlane=2.49162, width=1.24677, height=0.71588, cameraPosition=(0.729331, 
    2.15679, 0.198018), cameraUpVector=(-0.664978, -0.107529, -0.739081), 
    cameraTarget=(0.383459, 0.108562, -0.142125), viewOffsetX=0.0123494, 
    viewOffsetY=-0.00665321)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.49501, 
    farPlane=2.65544, width=1.08672, height=0.623982, cameraPosition=(-1.52283, 
    0.943238, 0.022952), cameraUpVector=(0.0680301, -0.498686, -0.864109), 
    cameraTarget=(0.394595, 0.0915977, -0.146576), viewOffsetX=0.0107641, 
    viewOffsetY=-0.00579913)
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
mdb.jobs['Pressure_Box_With_Holes'].submit(consistencyChecking=OFF)
#: The job input file "Pressure_Box_With_Holes.inp" has been submitted for analysis.
#: Job Pressure_Box_With_Holes: Analysis Input File Processor completed successfully.
#: Job Pressure_Box_With_Holes: Abaqus/Standard completed successfully.
#: Job Pressure_Box_With_Holes completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/chs17004/Desktop/Abaqus Pressure Vessel/Pressure Box with Bolts/Pressure_Box_With_Holes.odb'])
#: Warning: The output database 'C:/Users/chs17004/Desktop/Abaqus Pressure Vessel/Pressure Box with Bolts/Pressure_Box_With_Holes.odb' disk file has changed.
#: 
#: The current plot operation has been canceled, re-open the file to view the results
o3 = session.openOdb(
    name='C:/Users/chs17004/Desktop/Abaqus Pressure Vessel/Pressure Box with Bolts/Pressure_Box_With_Holes.odb')
#: Model: C:/Users/chs17004/Desktop/Abaqus Pressure Vessel/Pressure Box with Bolts/Pressure_Box_With_Holes.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     39
#: Number of Meshes:             39
#: Number of Element Sets:       59
#: Number of Node Sets:          61
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.76333, 
    farPlane=2.51995, width=1.20485, height=0.691808, cameraPosition=(0.373959, 
    -1.48776, -1.58357), cameraUpVector=(-0.468857, 0.801222, -0.371775), 
    cameraTarget=(0.392662, 0.0604957, -0.157703))
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p1 = mdb.models['Model-1'].parts['Cap']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.33151, 
    farPlane=2.31545, cameraPosition=(1.77837, -0.983239, -0.907817), 
    cameraUpVector=(0.323367, 0.282025, 0.90327), cameraTarget=(0.41376, 
    -0.19126, 0.00634983))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.38765, 
    farPlane=2.25931, cameraPosition=(1.41018, 0.855439, -1.1057), 
    cameraUpVector=(0.494515, -0.140106, 0.857803), cameraTarget=(0.41376, 
    -0.19126, 0.0063498))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.52239, 
    farPlane=2.12458, cameraPosition=(0.31746, 1.5359, -0.570474), 
    cameraUpVector=(0.810137, -0.11475, 0.574901), cameraTarget=(0.41376, 
    -0.19126, 0.00634982))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.28055, 
    farPlane=2.36642, cameraPosition=(-1.3595, -0.614, -0.0374335), 
    cameraUpVector=(0.215191, 0.445135, 0.869222), cameraTarget=(0.41376, 
    -0.19126, 0.00634989))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.55627, 
    farPlane=2.09069, cameraPosition=(0.0499767, -0.982677, 1.60835), 
    cameraUpVector=(0.0160311, 0.993247, 0.114907), cameraTarget=(0.41376, 
    -0.19126, 0.00634953))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.62875, 
    farPlane=2.01821, cameraPosition=(0.669321, -0.520003, 1.78165), 
    cameraUpVector=(-0.009825, 0.98737, -0.158126), cameraTarget=(0.41376, 
    -0.19126, 0.00634952))
p = mdb.models['Model-1'].parts['Cap']
f, e = p.faces, p.edges
t = p.MakeSketchTransform(sketchPlane=f[36], sketchUpEdge=e[10], 
    sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.41376, -0.19126, 
    0.0127))
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1.82, 
    gridSpacing=0.04, transform=t)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['Cap']
p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
s.rectangle(point1=(-0.37, 0.15), point2=(0.37, -0.15))
s.ObliqueDimension(vertex1=v[75], vertex2=v[72], textPoint=(-0.25847419453621, 
    0.207878981957435), value=0.75)
s.ObliqueDimension(vertex1=v[72], vertex2=v[73], textPoint=(-0.42916470123291, 
    0.0863149811124789), value=0.305)
s.Line(point1=(-0.38, 0.19126), point2=(-0.38, 0.155))
s.VerticalConstraint(entity=g[46], addUndoState=False)
s.PerpendicularConstraint(entity1=g[3], entity2=g[46], addUndoState=False)
s.CoincidentConstraint(entity1=v[76], entity2=g[3], addUndoState=False)
s.Line(point1=(-0.38, 0.155), point2=(-0.413759999954254, 0.155))
s.HorizontalConstraint(entity=g[47], addUndoState=False)
s.PerpendicularConstraint(entity1=g[46], entity2=g[47], addUndoState=False)
s.CoincidentConstraint(entity1=v[77], entity2=g[8], addUndoState=False)
s.Line(point1=(0.41376, -0.15), point2=(0.37, -0.15))
s.HorizontalConstraint(entity=g[48], addUndoState=False)
s.PerpendicularConstraint(entity1=g[4], entity2=g[48], addUndoState=False)
s.CoincidentConstraint(entity1=v[78], entity2=g[4], addUndoState=False)
s.Line(point1=(0.37, -0.15), point2=(0.37, -0.191259999996162))
s.VerticalConstraint(entity=g[49], addUndoState=False)
s.PerpendicularConstraint(entity1=g[48], entity2=g[49], addUndoState=False)
s.CoincidentConstraint(entity1=v[79], entity2=g[7], addUndoState=False)
s.EqualLengthConstraint(entity1=g[47], entity2=g[48])
s.EqualLengthConstraint(entity1=g[46], entity2=g[49])
s.setAsConstruction(objectList=(g[46], g[47], g[48], g[49]))
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.985011, 
    farPlane=2.37918, cameraPosition=(-1.39951, -0.297384, 0.405734), 
    cameraUpVector=(0.201724, 0.915339, -0.348515), cameraTarget=(0.369326, 
    -0.186479, -0.0232022))
p = mdb.models['Model-1'].parts['Cap']
f1, e1 = p.faces, p.edges
p.ShellExtrude(sketchPlane=f1[36], sketchUpEdge=e1[10], sketchPlaneSide=SIDE1, 
    sketchOrientation=RIGHT, sketch=s, depth=0.1, flipExtrudeDirection=ON)
#: Warning: Failed to attach mesh to part geometry.
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.34637, 
    farPlane=2.39506, cameraPosition=(-1.41067, -0.324946, -0.428783), 
    cameraUpVector=(0.241764, 0.963215, 0.117329), cameraTarget=(0.36639, 
    -0.186818, -0.0439912))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.45118, 
    farPlane=2.29592, cameraPosition=(-0.843339, -0.296832, 1.34791), 
    cameraUpVector=(0.224993, 0.959788, -0.167885), cameraTarget=(0.380716, 
    -0.186108, 0.000873834))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.35713, 
    farPlane=2.38865, cameraPosition=(-1.36507, -0.294245, 0.539714), 
    cameraUpVector=(0.29571, 0.95518, 0.0136618), cameraTarget=(0.366773, 
    -0.186039, -0.0207243))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.36162, 
    farPlane=2.38439, cameraPosition=(-1.45894, -0.175174, -0.00610038), 
    cameraUpVector=(0.339596, 0.929584, 0.143346), cameraTarget=(0.364297, 
    -0.182898, -0.0351238))
p = mdb.models['Model-1'].parts['Cap']
p.features['Shell extrude-1'].setValues(flipExtrudeDirection=False)
p = mdb.models['Model-1'].parts['Cap']
p.regenerate()
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.3534, 
    farPlane=2.38776, cameraPosition=(-1.45766, -0.245662, 0.0067369), 
    cameraUpVector=(0.305349, 0.941543, 0.142337), cameraTarget=(0.36433, 
    -0.184707, -0.0347943))
p = mdb.models['Model-1'].parts['Cap']
p.features['Shell extrude-1'].restore()
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.35976, 
    farPlane=2.24164, cameraPosition=(-0.705375, -0.728135, 1.3623), 
    cameraUpVector=(0.219113, 0.969805, 0.107084), cameraTarget=(0.38327, 
    -0.196854, -0.000665963))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.47566, 
    farPlane=2.05063, cameraPosition=(0.640193, -0.943264, 1.63564), 
    cameraUpVector=(0.0929763, 0.99337, 0.0676135), cameraTarget=(0.366245, 
    -0.194132, -0.00412452))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.18287, 
    farPlane=2.28963, cameraPosition=(1.99703, -0.831575, 0.371592), 
    cameraUpVector=(-0.047593, 0.966215, 0.253306), cameraTarget=(0.319809, 
    -0.197954, 0.0391355))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.28941, 
    farPlane=2.1666, cameraPosition=(1.65733, -0.265045, -1.1418), 
    cameraUpVector=(-0.0292084, 0.904686, 0.425078), cameraTarget=(0.336875, 
    -0.226416, 0.115168))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.18623, 
    farPlane=2.26652, cameraPosition=(2.0389, -0.576831, 0.494655), 
    cameraUpVector=(-0.202167, 0.959088, 0.198191), cameraTarget=(0.315793, 
    -0.209189, 0.0247502))
p = mdb.models['Model-1'].parts['Cap']
p.regenerate()
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.20129, 
    farPlane=2.2386, cameraPosition=(2.12174, -0.181507, -0.149434), 
    cameraUpVector=(-0.329617, 0.905519, 0.267185), cameraTarget=(0.311133, 
    -0.231425, 0.0609782))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.22747, 
    farPlane=2.22681, cameraPosition=(1.71508, -0.74944, 1.046), 
    cameraUpVector=(-0.163925, 0.975249, 0.148385), cameraTarget=(0.335613, 
    -0.197237, -0.0109844))
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].partDisplay.displayGroup.replace(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.31829, 
    farPlane=2.14242, cameraPosition=(1.49002, -0.107869, -1.29651), 
    cameraUpVector=(-0.096324, 0.897278, 0.43083), cameraTarget=(0.348167, 
    -0.233023, 0.119679))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.26089, 
    farPlane=2.15036, cameraPosition=(1.14992, 1.05688, -0.843731), 
    cameraUpVector=(-0.55181, 0.38415, 0.740226), cameraTarget=(0.36647, 
    -0.295707, 0.0953114))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.15473, 
    farPlane=2.25029, cameraPosition=(-1.19168, 0.236009, -0.316914), 
    cameraUpVector=(0.146285, 0.0323404, 0.988714), cameraTarget=(0.528272, 
    -0.238986, 0.0589089))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.31961, 
    farPlane=2.11866, cameraPosition=(-0.0683916, -1.83757, -0.0581034), 
    cameraUpVector=(0.138831, 0.252955, 0.957465), cameraTarget=(0.448458, 
    -0.0916509, 0.0405195))
p = mdb.models['Model-1'].parts['Cap']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1f0 #600 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces)
session.viewports['Viewport: 1'].partDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.26792, 
    farPlane=2.13283, cameraPosition=(-0.793077, -0.046889, 1.24551), 
    cameraUpVector=(0.720295, -0.614814, 0.321215), cameraTarget=(0.492446, 
    -0.200345, -0.0386097))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.26792, 
    farPlane=2.13283, cameraPosition=(-0.793077, -0.046889, 1.24551), 
    cameraUpVector=(0.882838, -0.183421, 0.432382), cameraTarget=(0.492446, 
    -0.200345, -0.0386097))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.19651, 
    farPlane=2.22029, cameraPosition=(-1.28662, -0.0274173, 0.0804694), 
    cameraUpVector=(0.331507, -0.21844, 0.917816), cameraTarget=(0.528179, 
    -0.201755, 0.0457406))
p = mdb.models['Model-1'].parts['Cap']
p.features['Shell extrude-1'].setValues(flipExtrudeDirection=True)
p = mdb.models['Model-1'].parts['Cap']
p.regenerate()
#: Warning: Due to changes in the part (for example, adding, deleting, or suppressing features, or partitioning the part), the expression used to evaluate this display group is no longer valid.
#: 
#: The display will revert to the entire part.
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.19768, 
    farPlane=2.23524, cameraPosition=(-1.28644, -0.134476, 0.206744), 
    cameraUpVector=(0.413399, -0.158449, 0.896658), cameraTarget=(0.528167, 
    -0.194663, 0.0373752))
p = mdb.models['Model-1'].parts['Cap']
p.features['Shell extrude-1'].setValues(keepInternalBoundaries=True)
p = mdb.models['Model-1'].parts['Cap']
p.regenerate()
p = mdb.models['Model-1'].parts['Cap']
p.regenerate()
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.223, 
    farPlane=2.26013, cameraPosition=(-1.14904, 0.031136, 0.702857), 
    cameraUpVector=(0.592098, -0.419437, 0.688109), cameraTarget=(0.5196, 
    -0.204989, 0.00644116))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.18011, 
    farPlane=2.22359, cameraPosition=(-1.28239, -0.108801, -0.169901), 
    cameraUpVector=(0.21305, -0.136891, 0.967404), cameraTarget=(0.525873, 
    -0.198406, 0.0474964))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.19463, 
    farPlane=2.22651, cameraPosition=(-1.29571, -0.137847, 0.0392178), 
    cameraUpVector=(0.333438, -0.108894, 0.936462), cameraTarget=(0.526825, 
    -0.19633, 0.0325499))
p = mdb.models['Model-1'].parts['Cap']
f = p.faces
p.RemoveFaces(faceList = f[1:2]+f[3:4]+f[6:8], deleteCells=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.29465, 
    farPlane=2.16029, cameraPosition=(-0.607705, 0.571014, 1.17259), 
    cameraUpVector=(0.86451, -0.245036, 0.43884), cameraTarget=(0.481342, 
    -0.243192, -0.0423756))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.23247, 
    farPlane=2.22247, width=1.91169, height=1.09767, cameraPosition=(-0.600181, 
    0.380231, 1.30719), cameraTarget=(0.488866, -0.433975, 0.0922213))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.22529, 
    farPlane=2.28058, cameraPosition=(-0.83214, 0.0844257, 1.23378), 
    cameraUpVector=(0.873843, 0.00966565, 0.486112), cameraTarget=(0.501758, 
    -0.417534, 0.0963016))
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.3714, 
    farPlane=3.26816, width=0.5683, height=0.326311, cameraPosition=(-0.975507, 
    1.7125, 1.76116), cameraUpVector=(-0.29355, 0.199992, -0.93479), 
    cameraTarget=(0.126168, 0.129835, 0.189556), viewOffsetX=0.25208, 
    viewOffsetY=0.110421)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Cap-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#10 ]', ), )
a.Surface(side1Faces=side1Faces1, name='Cap Bottom Surface')
#: The surface 'Cap Bottom Surface' has been edited (1 face).
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p1 = mdb.models['Model-1'].parts['Cap']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['Cap']
p.seedPart(size=0.01, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Cap']
p.generateMesh()
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.52503, 
    farPlane=2.1866, cameraPosition=(-0.175812, -0.320866, 1.77585), 
    cameraUpVector=(0.987133, 0.159369, 0.0130177), cameraTarget=(0.475344, 
    -0.401223, 0.0744858))
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.jobs['Pressure_Box_With_Holes'].submit(consistencyChecking=OFF)
#: The job input file "Pressure_Box_With_Holes.inp" has been submitted for analysis.
#: Job Pressure_Box_With_Holes: Analysis Input File Processor completed successfully.
#: Job Pressure_Box_With_Holes: Abaqus/Standard completed successfully.
#: Job Pressure_Box_With_Holes completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/chs17004/Desktop/Abaqus Pressure Vessel/Pressure Box with Bolts/Pressure_Box_With_Holes.odb'])
o3 = session.openOdb(
    name='C:/Users/chs17004/Desktop/Abaqus Pressure Vessel/Pressure Box with Bolts/Pressure_Box_With_Holes.odb')
#: Model: C:/Users/chs17004/Desktop/Abaqus Pressure Vessel/Pressure Box with Bolts/Pressure_Box_With_Holes.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     39
#: Number of Meshes:             39
#: Number of Element Sets:       59
#: Number of Node Sets:          61
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.63836, 
    farPlane=2.66339, width=1.11946, height=0.64278, cameraPosition=(1.21782, 
    -1.43235, -1.39399), cameraUpVector=(-0.787862, 0.415524, -0.454548), 
    cameraTarget=(0.400588, 0.0609642, -0.155968))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.58583, 
    farPlane=2.68884, width=1.08357, height=0.622171, cameraPosition=(1.78979, 
    -0.297599, -1.70798), cameraUpVector=(-0.897226, 0.198258, -0.394561), 
    cameraTarget=(0.412818, 0.0852279, -0.162682))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Max. In-Plane Principal (Abs)'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Max. Principal (Abs)'), )
mdb.save()
#: The model database has been saved to "C:\Users\chs17004\Desktop\Abaqus Pressure Vessel\Pressure Box with Bolts\Pressure_Box With Bolts.cae".
