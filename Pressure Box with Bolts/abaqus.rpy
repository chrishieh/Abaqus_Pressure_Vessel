# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2019 replay file
# Internal Version: 2018_09_24-14.41.51 157541
# Run by chs17004 on Thu Oct  8 08:44:52 2020
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
openMdb('Pressure_Box With Bolts.cae')
#: The model database "C:\Users\chs17004\Desktop\Abaqus Pressure Vessel\Pressure Box with Bolts\Pressure_Box With Bolts.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['Bottom']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
#: The contents of viewport "Viewport: 1" have been copied to the clipboard.
p1 = mdb.models['Model-1'].parts['Top_Flange-Copy']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.39152, 
    farPlane=2.25509, width=0.663129, height=0.409999, cameraPosition=(
    -1.20986, -1.03826, 1.08208), cameraUpVector=(-0.186489, 0.842045, 
    0.506145), cameraTarget=(-0.0554921, -0.132174, 1.63913e-07))
p = mdb.models['Model-1'].parts['Top_Flange-Copy']
f = p.faces
p.AddCells(faceList = f[0:1], flipped=True)
#* Solid from shell failed.
p = mdb.models['Model-1'].parts['Top_Flange-Copy']
f1 = p.faces
p.AddCells(faceList = f1[0:1], flipped=True)
#* Solid from shell failed.
p = mdb.models['Model-1'].parts['Top_Flange-Copy']
f = p.faces
p.AddCells(faceList = f[0:1], flipped=False)
#* Solid from shell failed.
p = mdb.models['Model-1'].parts['Top_Flange-Copy']
s = p.features['Shell planar-1'].sketch
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=s)
s1 = mdb.models['Model-1'].sketches['__edit__']
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s1, 
    upToFeature=p.features['Shell planar-1'], filter=COPLANAR_EDGES)
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__edit__']
p1 = mdb.models['Model-1'].parts['Top_Flange']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
#: The contents of viewport "Viewport: 1" have been copied to the clipboard.
#: The contents of viewport "Viewport: 1" have been copied to the clipboard.
p1 = mdb.models['Model-1'].parts['Top_Flange-Copy']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.80867, 
    farPlane=2.05155, width=0.754671, height=0.466597, cameraPosition=(
    -0.16669, -0.575602, 1.87542), cameraUpVector=(0.0209657, 0.970533, 
    0.240056), cameraTarget=(-0.078365, -0.111816, -0.00735431))
p1 = mdb.models['Model-1'].parts['Cap-Copy']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['Cap-Copy']
f1, e = p.faces, p.edges
t = p.MakeSketchTransform(sketchPlane=f1[0], sketchUpEdge=e[37], 
    sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(-0.055492, 
    -0.132174, 0.0))
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1.82, 
    gridSpacing=0.04, transform=t)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['Cap-Copy']
p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.74375, 
    farPlane=1.90286, width=1.00458, height=0.621108, viewOffsetX=0.0513127, 
    viewOffsetY=0.0119328)
p = mdb.models['Model-1'].parts['Cap-Copy']
f = p.faces
p.AddCells(faceList = f[0:1], flipped=True)
#* Solid from shell failed.
p = mdb.models['Model-1'].parts['Cap-Copy']
f1, e1 = p.faces, p.edges
t = p.MakeSketchTransform(sketchPlane=f1[0], sketchUpEdge=e1[37], 
    sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(-0.055492, 
    -0.132174, 0.0))
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=1.82, gridSpacing=0.04, transform=t)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['Cap-Copy']
p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
s1.rectangle(point1=(-0.413760138881737, 0.19126031463867), point2=(
    0.413759861118263, -0.19125968536133))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.76725, 
    farPlane=1.87936, width=0.599425, height=0.370612, cameraPosition=(
    -0.176641, -0.0797851, 1.82331), cameraTarget=(-0.176641, -0.0797851, 
    6.30662e-18))
s1.CircleByCenterPerimeter(center=(-0.394380138881737, 0.17188031463867), 
    point1=(-0.394380138881737, 0.16625031463867))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.78217, 
    farPlane=1.86445, width=0.43992, height=0.271994, cameraPosition=(
    -0.249095, -0.0668264, 1.82331), cameraTarget=(-0.249095, -0.0668264, 
    6.30662e-18))
s1.CircleByCenterPerimeter(center=(-0.394380138881737, 0.10298451463867), 
    point1=(-0.394380138881737, 0.0973545146386697))
s1.CircleByCenterPerimeter(center=(-0.394380138881737, 0.0340887146386697), 
    point1=(-0.394380138881737, 0.0284587146386697))
s1.CircleByCenterPerimeter(center=(-0.394380138881737, -0.0340880853613301), 
    point1=(-0.394380138881737, -0.0284580853613301))
s1.CircleByCenterPerimeter(center=(-0.250912320701737, 0.17188031463867), 
    point1=(-0.248958456104706, 0.166600228168121))
s1.CircleByCenterPerimeter(center=(-0.322646229791737, 0.17188031463867), 
    point1=(-0.321621940574229, 0.166344275296424))
s1.CircleByCenterPerimeter(center=(-0.179178411611737, 0.17188031463867), 
    point1=(-0.176446083292128, 0.166957786634294))
s1.CircleByCenterPerimeter(center=(-0.107444502521737, 0.17188031463867), 
    point1=(-0.107089822788528, 0.166261497833785))
s1.CircleByCenterPerimeter(center=(-0.035710593431737, 0.17188031463867), 
    point1=(-0.0366876114325903, 0.166335737483827))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.79119, 
    farPlane=1.85543, width=0.343468, height=0.212359, cameraPosition=(
    0.0520923, -0.0129452, 1.82331), cameraTarget=(0.0520923, -0.0129452, 
    6.30662e-18))
s1.CircleByCenterPerimeter(center=(0.0357103156682625, 0.17188031463867), 
    point1=(0.0366873336691158, 0.166335737483827))
s1.CircleByCenterPerimeter(center=(0.107444224758263, 0.17188031463867), 
    point1=(0.107089545025053, 0.166261497833785))
s1.CircleByCenterPerimeter(center=(0.179178133848263, 0.17188031463867), 
    point1=(0.176445805528653, 0.166957786634294))
s1.CircleByCenterPerimeter(center=(0.250912042938263, 0.17188031463867), 
    point1=(0.248958178341231, 0.166600228168121))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.78857, 
    farPlane=1.85804, width=0.371407, height=0.229633, cameraPosition=(
    0.241826, -0.0273214, 1.82331), cameraTarget=(0.241826, -0.0273214, 
    6.30662e-18))
s1.CircleByCenterPerimeter(center=(0.322645952028263, 0.17188031463867), 
    point1=(0.321621662810754, 0.166344275296424))
s1.CircleByCenterPerimeter(center=(0.394379861118263, 0.17188031463867), 
    point1=(0.394379861118263, 0.16625031463867))
s1.CircleByCenterPerimeter(center=(0.394379861118263, 0.10298451463867), 
    point1=(0.394379861118263, 0.0973545146386697))
s1.CircleByCenterPerimeter(center=(0.394379861118263, 0.0340887146386697), 
    point1=(0.394379861118263, 0.0284587146386697))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.78316, 
    farPlane=1.86345, width=0.42925, height=0.265397, cameraPosition=(0.257907, 
    -0.220205, 1.82331), cameraTarget=(0.257907, -0.220205, 6.30662e-18))
s1.CircleByCenterPerimeter(center=(0.394379861118263, -0.0340880853613301), 
    point1=(0.394379861118263, -0.0284580853613301))
s1.CircleByCenterPerimeter(center=(0.394379861118263, -0.10298388536133), 
    point1=(0.394379861118263, -0.0973538853613301))
s1.CircleByCenterPerimeter(center=(0.394379861118263, -0.17187968536133), 
    point1=(0.394379861118263, -0.16624968536133))
s1.CircleByCenterPerimeter(center=(0.322645952028263, -0.17187968536133), 
    point1=(0.321621662810754, -0.166343646019084))
s1.CircleByCenterPerimeter(center=(0.250912042938263, -0.17187968536133), 
    point1=(0.248958178341231, -0.166599598890782))
s1.CircleByCenterPerimeter(center=(0.179178133848263, -0.17187968536133), 
    point1=(0.176445805528653, -0.166957157356955))
s1.CircleByCenterPerimeter(center=(0.107444224758263, -0.17187968536133), 
    point1=(0.107089545025053, -0.166260868556446))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.77625, 
    farPlane=1.87036, width=0.503151, height=0.311088, cameraPosition=(
    -0.162088, -0.242376, 1.82331), cameraTarget=(-0.162088, -0.242376, 
    6.30662e-18))
s1.CircleByCenterPerimeter(center=(0.0357103156682625, -0.17187968536133), 
    point1=(0.0366873336691158, -0.166335108206487))
s1.CircleByCenterPerimeter(center=(-0.035710593431737, -0.17187968536133), 
    point1=(-0.0366876114325903, -0.166335108206487))
s1.CircleByCenterPerimeter(center=(-0.107444502521737, -0.17187968536133), 
    point1=(-0.107089822788528, -0.166260868556446))
#: Warning: Coincident point selected
#: Warning: Coincident point selected
#: Warning: Coincident point selected
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.78877, 
    farPlane=1.85784, width=0.369265, height=0.228309, cameraPosition=(
    -0.181232, -0.258138, 1.82331), cameraTarget=(-0.181232, -0.258138, 
    6.30662e-18))
s1.CircleByCenterPerimeter(center=(-0.179178411611737, -0.17187968536133), 
    point1=(-0.176446083292128, -0.166957157356955))
s1.CircleByCenterPerimeter(center=(-0.250912320701737, -0.17187968536133), 
    point1=(-0.248958456104706, -0.166599598890782))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.79045, 
    farPlane=1.85617, width=0.351386, height=0.217255, cameraPosition=(
    -0.334242, -0.230368, 1.82331), cameraTarget=(-0.334242, -0.230368, 
    6.30662e-18))
s1.CircleByCenterPerimeter(center=(-0.394380138881737, -0.10298388536133), 
    point1=(-0.394380138881737, -0.0973538853613301))
s1.CircleByCenterPerimeter(center=(-0.394380138881737, -0.17187968536133), 
    point1=(-0.394380138881737, -0.16624968536133))
s1.CircleByCenterPerimeter(center=(-0.322646229791737, -0.17187968536133), 
    point1=(-0.321621940574229, -0.166343646019084))
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.75369, 
    farPlane=1.89292, width=0.965729, height=0.59709, cameraPosition=(
    -0.209027, -0.211153, 1.82331), cameraTarget=(-0.209027, -0.211153, 
    6.30662e-18))
p = mdb.models['Model-1'].parts['Cap-Copy']
f, e = p.faces, p.edges
p.SolidExtrude(sketchPlane=f[0], sketchUpEdge=e[37], sketchPlaneSide=SIDE1, 
    sketchOrientation=RIGHT, sketch=s1, depth=0.0254, flipExtrudeDirection=OFF)
s1.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.27517, 
    farPlane=2.24783, width=0.734627, height=0.454205, cameraPosition=(
    -1.70934, -0.0600714, 0.615557), cameraUpVector=(-0.0640513, 0.95294, 
    -0.296316), cameraTarget=(-0.00845963, -0.14815, -0.0353609), 
    viewOffsetX=0.037524, viewOffsetY=0.00872622)
p = mdb.models['Model-1'].parts['Cap-Copy']
p.deleteFeatures(('Shell planar-1', 'Solid extrude-1', ))
