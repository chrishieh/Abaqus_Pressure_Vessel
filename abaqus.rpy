# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2019 replay file
# Internal Version: 2018_09_24-14.41.51 157541
# Run by chs17004 on Wed Oct  7 11:08:19 2020
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=356.125030517578, 
    height=249.75)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
openMdb('Pressure_Box With Holes.cae')
#: The model database "C:\Users\chs17004\Desktop\New folder\Pressure_Box With Holes.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['Bottom']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
#--- Recover file: 'Pressure_Box With Holes.rec' ---
# -*- coding: mbcs -*- 
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
mdb.jobs['Pressure_Box_With_Holes'].submit(consistencyChecking=OFF)
mdb.jobs['Pressure_Box_With_Holes']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'FFM5TW1', 'handle': 0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'THE SLAVE SURFACES ASSEMBLY_Side 1 slave surface AND ASSEMBLY_S_SURF-37 INTERSECT EACH OTHER. THEY ARE PAIRED WITH MASTER SURFACES ASSEMBLY_BOTTOM_MASTER_SURFACE AND ASSEMBLY_M_SURF-37 THAT ALSO INTERSECT EACH OTHER. IF BOTH PAIRS ARE *CONTACT PAIRs, THESE TWO PAIRS SHOULD NOT BE SIMULTANEOUSLY PRESENT IN A STEP BECAUSE OF POSSIBLE CONVERGENCE PROBLEMS; USE *MODEL CHANGE,TYPE=CONTACT PAIR TO REMOVE ONE OF THEM. IF BOTH ARE *TIE PAIRS, THE REDUNDANT TIES WILL BE REMOVED AUTOMATICALLY. IF ONE PAIR IS *TIE AND ANOTHER IS *CONTACT PAIR, REMOVE ONE OF THEM.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-14_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), NOT ALL THE NODES THAT HAVE BEEN ADJUSTED WERE PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), ADJUSTED NODES WITH VERY SMALL ADJUSTMENTS WERE NOT PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-45,ASSEMBLY_M_SURF-45) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-45-ASSEMBLY_M_SURF-45), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-47,ASSEMBLY_M_SURF-47) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-47-ASSEMBLY_M_SURF-47), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-21_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-21_CNS_-ASSEMBLY_M_SURF-49), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-22_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-22_CNS_-ASSEMBLY_M_SET-22_CNS_), ADJUSTED NODES WITH VERY SMALL ADJUSTMENTS WERE NOT PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '23 nodes have been adjusted. The nodes have been identified in node set WarnNodeAdjust.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 11 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 11 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 55 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 55 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 45 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 45 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 19 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 19 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 20 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 20 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 31 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 31 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 32 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 54 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 32 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 54 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 33 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 55 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 33 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 55 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 34 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 55 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 34 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 55 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 35 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 35 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE Short Side-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE Short Side-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 5 INSTANCE Short Side-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 18 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 5 INSTANCE Short Side-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 18 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 9 INSTANCE Short Side-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 18 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 9 INSTANCE Short Side-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 18 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 13 INSTANCE Short Side-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 13 INSTANCE Short Side-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 2 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 2 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 3 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 39 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 3 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 39 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 4 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 40 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 4 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 40 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 5 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 19 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 5 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 19 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 6 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 19 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 6 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 19 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 7 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 19 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 7 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 19 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 8 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 43 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 8 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 43 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 9 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 44 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 9 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 44 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 10 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 10 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 11 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 11 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 11 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 11 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 45 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 45 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 46 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 46 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 47 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 32 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 47 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 32 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 48 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 31 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 48 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 31 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 49 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 30 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 49 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 30 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 50 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 30 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 50 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 30 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 51 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 29 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 51 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 29 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 52 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 28 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 52 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 28 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 53 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 27 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 53 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 27 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 54 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 54 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 55 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 55 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE Short Side-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE Short Side-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 45 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE Short Side-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 45 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE Short Side-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 55 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 55 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '225 nodes are either missing intersection with their respective master surface or are outside the adjust zone. The nodes have been identified in node set WarnNodeMissMasterIntersect.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '37 nodes are used more than once as a slave node in *TIE keyword. One of the *TIE constraints at each of these nodes have been removed. The nodes have been identified in node set WarnNodeOverconTieSlave.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '2 elements are curved/warped. The angle subtended between the average element normal and a nodal normal exceeds 10 degrees. Mesh refinement is recommended. The elements have been identified in element set WarnElemWarped.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FILE, {
    'phase': BATCHPRE_PHASE, 
    'file': 'C:\\Users\\chs17004\\Downloads\\Pressure_Box_With_Holes.odb', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(COMPLETED, {
    'phase': BATCHPRE_PHASE, 'message': 'Analysis phase complete', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'FFM5TW1', 'handle': 12664, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STEP, {'phase': STANDARD_PHASE, 
    'stepId': 1, 'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(MEMORY_ESTIMATE, {
    'phase': STANDARD_PHASE, 'jobName': 'Pressure_Box_With_Holes', 
    'memory': 33.0})
mdb.jobs['Pressure_Box_With_Holes']._Message(PHYSICAL_MEMORY, {
    'phase': STANDARD_PHASE, 'physical_memory': 8147.0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(MINIMUM_MEMORY, {
    'minimum_memory': 23.0, 'phase': STANDARD_PHASE, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 1, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STATUS, {'totalTime': 1.0, 
    'attempts': 1, 'timeIncrement': 1.0, 'increment': 1, 'stepTime': 1.0, 
    'step': 1, 'jobName': 'Pressure_Box_With_Holes', 'severe': 0, 
    'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Pressure_Box_With_Holes']._Message(END_STEP, {
    'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(COMPLETED, {
    'phase': STANDARD_PHASE, 'message': 'Analysis phase complete', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(JOB_COMPLETED, {
    'time': 'Tue Oct  6 12:02:16 2020', 'jobName': 'Pressure_Box_With_Holes'})
mdb.models['Model-1'].parts['Bottom'].deleteMesh()
mdb.models['Model-1'].parts['Bottom'].seedPart(minSizeFactor=0.9, size=0.025)
mdb.models['Model-1'].parts['Bottom'].generateMesh()
mdb.models['Model-1'].parts['Cap'].deleteMesh()
mdb.models['Model-1'].parts['Cap'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=0.025)
mdb.models['Model-1'].parts['Cap'].generateMesh()
mdb.models['Model-1'].parts['Long_Side'].deleteMesh()
mdb.models['Model-1'].parts['Long_Side'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=0.025)
mdb.models['Model-1'].parts['Long_Side'].generateMesh()
mdb.models['Model-1'].parts['Short Side With Holes'].deleteMesh()
mdb.models['Model-1'].parts['Short Side With Holes'].seedPart(
    deviationFactor=0.1, minSizeFactor=0.1, size=0.025)
mdb.models['Model-1'].parts['Short Side With Holes'].generateMesh()
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.jobs['Pressure_Box_With_Holes'].submit(consistencyChecking=OFF)
mdb.jobs['Pressure_Box_With_Holes']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'FFM5TW1', 'handle': 0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'THE SLAVE SURFACES ASSEMBLY_Side 1 slave surface AND ASSEMBLY_S_SURF-37 INTERSECT EACH OTHER. THEY ARE PAIRED WITH MASTER SURFACES ASSEMBLY_BOTTOM_MASTER_SURFACE AND ASSEMBLY_M_SURF-37 THAT ALSO INTERSECT EACH OTHER. IF BOTH PAIRS ARE *CONTACT PAIRs, THESE TWO PAIRS SHOULD NOT BE SIMULTANEOUSLY PRESENT IN A STEP BECAUSE OF POSSIBLE CONVERGENCE PROBLEMS; USE *MODEL CHANGE,TYPE=CONTACT PAIR TO REMOVE ONE OF THEM. IF BOTH ARE *TIE PAIRS, THE REDUNDANT TIES WILL BE REMOVED AUTOMATICALLY. IF ONE PAIR IS *TIE AND ANOTHER IS *CONTACT PAIR, REMOVE ONE OF THEM.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-14_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), NOT ALL THE NODES THAT HAVE BEEN ADJUSTED WERE PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), ADJUSTED NODES WITH VERY SMALL ADJUSTMENTS WERE NOT PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-45,ASSEMBLY_M_SURF-45) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-45-ASSEMBLY_M_SURF-45), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-47,ASSEMBLY_M_SURF-47) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-47-ASSEMBLY_M_SURF-47), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-21_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-21_CNS_-ASSEMBLY_M_SURF-49), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-22_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-22_CNS_-ASSEMBLY_M_SET-22_CNS_), ADJUSTED NODES WITH VERY SMALL ADJUSTMENTS WERE NOT PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '98 nodes have been adjusted. The nodes have been identified in node set WarnNodeAdjust.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 31 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 31 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 62 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 62 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 372 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 372 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 403 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 403 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 32 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 32 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 342 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 342 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 373 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 373 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 9 INSTANCE Short Side-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 100 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 9 INSTANCE Short Side-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 100 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 13 INSTANCE Short Side-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 13 INSTANCE Short Side-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 2 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 2 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE Short Side-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE Short Side-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE Short Side-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE Short Side-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 5 INSTANCE Short Side-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 96 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 5 INSTANCE Short Side-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 96 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 373 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 373 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 374 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 374 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 373 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE Short Side-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 373 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE Short Side-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 19 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 19 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 50 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 189 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 50 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 189 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 51 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 190 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 51 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 190 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 52 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 191 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 52 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 191 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 53 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 53 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 402 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 402 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 403 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 403 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 403 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 403 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 20 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 20 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 30 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 30 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 31 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 31 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 31 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 31 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 43 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 182 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 43 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 182 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 44 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 183 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 44 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 183 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 45 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 184 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 45 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 184 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 46 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 185 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 46 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 185 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 47 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 186 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 47 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 186 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 48 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 187 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 48 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 187 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 49 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 187 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 49 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 187 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 3 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 116 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 3 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 116 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 4 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 117 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 4 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 117 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 5 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 118 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 5 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 118 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 6 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 118 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 6 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 118 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 7 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 119 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 7 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 119 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 8 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 121 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 8 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 121 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 9 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 122 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 9 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 122 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 10 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 122 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 10 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 122 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 11 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 123 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 11 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 123 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 12 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 125 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 12 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 125 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 13 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 126 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 13 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 126 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 14 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 126 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 14 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 126 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 15 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 127 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 15 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 127 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 129 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 129 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 17 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 130 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 17 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 130 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 18 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 131 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 18 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 131 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 19 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 131 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 19 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 131 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 20 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 132 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 20 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 132 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 21 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 134 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 21 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 134 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 22 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 134 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 22 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 134 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 23 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 136 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 23 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 136 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 24 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 136 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 24 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 136 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 25 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 138 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 25 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 138 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 26 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 138 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 26 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 138 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 27 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 139 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 27 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 139 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 28 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 141 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 28 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 141 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 29 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 141 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 29 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 141 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 375 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 91 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 375 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 91 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 376 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 90 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 376 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 90 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 377 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 89 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 377 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 89 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 378 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 89 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 378 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 89 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 379 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 88 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 379 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 88 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 380 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 86 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 380 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 86 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 381 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 85 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 381 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 85 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 382 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 85 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 382 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 85 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 383 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 84 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 383 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 84 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 384 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 82 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 384 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 82 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 385 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 81 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 385 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 81 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 386 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 81 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 386 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 81 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 387 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 80 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 387 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 80 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 388 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 78 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 388 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 78 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 389 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 77 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 389 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 77 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 390 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 76 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 390 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 76 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 391 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 76 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 391 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 76 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 392 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 75 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 392 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 75 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 393 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 73 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 393 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 73 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 394 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 73 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 394 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 73 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 395 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 71 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 395 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 71 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 396 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 71 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 396 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 71 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 397 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 69 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 397 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 69 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 398 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 69 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 398 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 69 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 399 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 68 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 399 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 68 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 400 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 66 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 400 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 66 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 401 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 66 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 401 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 66 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '1042 nodes are either missing intersection with their respective master surface or are outside the adjust zone. The nodes have been identified in node set WarnNodeMissMasterIntersect.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'Normal cannot be computed in 17 elements. The nodal coordinates may be incorrect or the element aspect ratio may exceed 1000 to 1. The elements have been identified in element set ErrElemNormal.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '87 nodes are used more than once as a slave node in *TIE keyword. One of the *TIE constraints at each of these nodes have been removed. The nodes have been identified in node set WarnNodeOverconTieSlave.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'The geometry of 16 elements is too distorted. Check the nodal coordinates or node numbering on elements identified in element set ErrElemDistorted.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '61 elements are distorted. Either the isoparametric angles are out of the suggested limits or the triangular or tetrahedral quality measure is bad. The elements have been identified in element set WarnElemDistorted.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'The area of 9 elements is zero, small, or negative. Check coordinates or node numbering, or modify the mesh seed. The elements have been identified in element set ErrElemAreaSmallNegZero.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'The aspect ratio for 3 elements exceeds 100 to 1. The elements have been identified in element set WarnElemAspectRatio.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'Error in defining normal to the element surface at a node in 17 elements. The elements have been identified in element set ErrElemShellNormal.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FILE, {
    'phase': BATCHPRE_PHASE, 
    'file': 'C:\\Users\\chs17004\\Downloads\\Pressure_Box_With_Holes.odb', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ABORTED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase failed due to errors', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ERROR, {
    'message': 'Analysis Input File Processor exited with an error.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(JOB_ABORTED, {
    'message': 'Analysis Input File Processor exited with an error.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.models['Model-1'].constraints['Constraint-7'].suppress()
mdb.jobs['Pressure_Box_With_Holes'].submit(consistencyChecking=OFF)
mdb.jobs['Pressure_Box_With_Holes']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'FFM5TW1', 'handle': 0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'THE SLAVE SURFACES ASSEMBLY_Side 1 slave surface AND ASSEMBLY_S_SURF-37 INTERSECT EACH OTHER. THEY ARE PAIRED WITH MASTER SURFACES ASSEMBLY_BOTTOM_MASTER_SURFACE AND ASSEMBLY_M_SURF-37 THAT ALSO INTERSECT EACH OTHER. IF BOTH PAIRS ARE *CONTACT PAIRs, THESE TWO PAIRS SHOULD NOT BE SIMULTANEOUSLY PRESENT IN A STEP BECAUSE OF POSSIBLE CONVERGENCE PROBLEMS; USE *MODEL CHANGE,TYPE=CONTACT PAIR TO REMOVE ONE OF THEM. IF BOTH ARE *TIE PAIRS, THE REDUNDANT TIES WILL BE REMOVED AUTOMATICALLY. IF ONE PAIR IS *TIE AND ANOTHER IS *CONTACT PAIR, REMOVE ONE OF THEM.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-14_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), NOT ALL THE NODES THAT HAVE BEEN ADJUSTED WERE PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), ADJUSTED NODES WITH VERY SMALL ADJUSTMENTS WERE NOT PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-45,ASSEMBLY_M_SURF-45) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-45-ASSEMBLY_M_SURF-45), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-47,ASSEMBLY_M_SURF-47) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-47-ASSEMBLY_M_SURF-47), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-22_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-22_CNS_-ASSEMBLY_M_SET-22_CNS_), ADJUSTED NODES WITH VERY SMALL ADJUSTMENTS WERE NOT PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '98 nodes have been adjusted. The nodes have been identified in node set WarnNodeAdjust.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 31 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 31 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 62 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 62 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 372 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 372 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 403 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 403 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 32 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 32 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 342 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 342 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 373 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 373 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE Short Side-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE Short Side-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 373 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE Short Side-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 373 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE Short Side-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 403 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 403 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 31 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 31 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '1042 nodes are either missing intersection with their respective master surface or are outside the adjust zone. The nodes have been identified in node set WarnNodeMissMasterIntersect.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'Normal cannot be computed in 17 elements. The nodal coordinates may be incorrect or the element aspect ratio may exceed 1000 to 1. The elements have been identified in element set ErrElemNormal.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '12 nodes are used more than once as a slave node in *TIE keyword. One of the *TIE constraints at each of these nodes have been removed. The nodes have been identified in node set WarnNodeOverconTieSlave.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'The geometry of 16 elements is too distorted. Check the nodal coordinates or node numbering on elements identified in element set ErrElemDistorted.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '61 elements are distorted. Either the isoparametric angles are out of the suggested limits or the triangular or tetrahedral quality measure is bad. The elements have been identified in element set WarnElemDistorted.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'The area of 9 elements is zero, small, or negative. Check coordinates or node numbering, or modify the mesh seed. The elements have been identified in element set ErrElemAreaSmallNegZero.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'The aspect ratio for 3 elements exceeds 100 to 1. The elements have been identified in element set WarnElemAspectRatio.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'Error in defining normal to the element surface at a node in 17 elements. The elements have been identified in element set ErrElemShellNormal.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FILE, {
    'phase': BATCHPRE_PHASE, 
    'file': 'C:\\Users\\chs17004\\Downloads\\Pressure_Box_With_Holes.odb', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ABORTED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase failed due to errors', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ERROR, {
    'message': 'Analysis Input File Processor exited with an error.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(JOB_ABORTED, {
    'message': 'Analysis Input File Processor exited with an error.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.models['Model-1'].constraints['Constraint-8'].suppress()
mdb.jobs['Pressure_Box_With_Holes'].submit(consistencyChecking=OFF)
mdb.jobs['Pressure_Box_With_Holes']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'FFM5TW1', 'handle': 0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'THE SLAVE SURFACES ASSEMBLY_Side 1 slave surface AND ASSEMBLY_S_SURF-37 INTERSECT EACH OTHER. THEY ARE PAIRED WITH MASTER SURFACES ASSEMBLY_BOTTOM_MASTER_SURFACE AND ASSEMBLY_M_SURF-37 THAT ALSO INTERSECT EACH OTHER. IF BOTH PAIRS ARE *CONTACT PAIRs, THESE TWO PAIRS SHOULD NOT BE SIMULTANEOUSLY PRESENT IN A STEP BECAUSE OF POSSIBLE CONVERGENCE PROBLEMS; USE *MODEL CHANGE,TYPE=CONTACT PAIR TO REMOVE ONE OF THEM. IF BOTH ARE *TIE PAIRS, THE REDUNDANT TIES WILL BE REMOVED AUTOMATICALLY. IF ONE PAIR IS *TIE AND ANOTHER IS *CONTACT PAIR, REMOVE ONE OF THEM.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-14_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), NOT ALL THE NODES THAT HAVE BEEN ADJUSTED WERE PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), ADJUSTED NODES WITH VERY SMALL ADJUSTMENTS WERE NOT PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-45,ASSEMBLY_M_SURF-45) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-45-ASSEMBLY_M_SURF-45), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-47,ASSEMBLY_M_SURF-47) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-47-ASSEMBLY_M_SURF-47), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '98 nodes have been adjusted. The nodes have been identified in node set WarnNodeAdjust.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 32 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 32 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 342 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 342 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 373 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 373 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE Short Side-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE Short Side-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 373 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE Short Side-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 373 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE Short Side-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '1042 nodes are either missing intersection with their respective master surface or are outside the adjust zone. The nodes have been identified in node set WarnNodeMissMasterIntersect.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'Normal cannot be computed in 17 elements. The nodal coordinates may be incorrect or the element aspect ratio may exceed 1000 to 1. The elements have been identified in element set ErrElemNormal.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '6 nodes are used more than once as a slave node in *TIE keyword. One of the *TIE constraints at each of these nodes have been removed. The nodes have been identified in node set WarnNodeOverconTieSlave.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'The geometry of 16 elements is too distorted. Check the nodal coordinates or node numbering on elements identified in element set ErrElemDistorted.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '61 elements are distorted. Either the isoparametric angles are out of the suggested limits or the triangular or tetrahedral quality measure is bad. The elements have been identified in element set WarnElemDistorted.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'The area of 9 elements is zero, small, or negative. Check coordinates or node numbering, or modify the mesh seed. The elements have been identified in element set ErrElemAreaSmallNegZero.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'The aspect ratio for 3 elements exceeds 100 to 1. The elements have been identified in element set WarnElemAspectRatio.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'Error in defining normal to the element surface at a node in 17 elements. The elements have been identified in element set ErrElemShellNormal.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FILE, {
    'phase': BATCHPRE_PHASE, 
    'file': 'C:\\Users\\chs17004\\Downloads\\Pressure_Box_With_Holes.odb', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ABORTED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase failed due to errors', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ERROR, {
    'message': 'Analysis Input File Processor exited with an error.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(JOB_ABORTED, {
    'message': 'Analysis Input File Processor exited with an error.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.models['Model-1'].constraints['Constraint-6'].suppress()
mdb.jobs['Pressure_Box_With_Holes'].submit(consistencyChecking=OFF)
mdb.jobs['Pressure_Box_With_Holes']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'FFM5TW1', 'handle': 0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'THE SLAVE SURFACES ASSEMBLY_Side 1 slave surface AND ASSEMBLY_S_SURF-37 INTERSECT EACH OTHER. THEY ARE PAIRED WITH MASTER SURFACES ASSEMBLY_BOTTOM_MASTER_SURFACE AND ASSEMBLY_M_SURF-37 THAT ALSO INTERSECT EACH OTHER. IF BOTH PAIRS ARE *CONTACT PAIRs, THESE TWO PAIRS SHOULD NOT BE SIMULTANEOUSLY PRESENT IN A STEP BECAUSE OF POSSIBLE CONVERGENCE PROBLEMS; USE *MODEL CHANGE,TYPE=CONTACT PAIR TO REMOVE ONE OF THEM. IF BOTH ARE *TIE PAIRS, THE REDUNDANT TIES WILL BE REMOVED AUTOMATICALLY. IF ONE PAIR IS *TIE AND ANOTHER IS *CONTACT PAIR, REMOVE ONE OF THEM.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-14_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), NOT ALL THE NODES THAT HAVE BEEN ADJUSTED WERE PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), ADJUSTED NODES WITH VERY SMALL ADJUSTMENTS WERE NOT PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-45,ASSEMBLY_M_SURF-45) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-45-ASSEMBLY_M_SURF-45), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '98 nodes have been adjusted. The nodes have been identified in node set WarnNodeAdjust.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 32 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 32 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 342 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 342 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 373 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 373 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '1012 nodes are either missing intersection with their respective master surface or are outside the adjust zone. The nodes have been identified in node set WarnNodeMissMasterIntersect.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'Normal cannot be computed in 17 elements. The nodal coordinates may be incorrect or the element aspect ratio may exceed 1000 to 1. The elements have been identified in element set ErrElemNormal.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '4 nodes are used more than once as a slave node in *TIE keyword. One of the *TIE constraints at each of these nodes have been removed. The nodes have been identified in node set WarnNodeOverconTieSlave.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'The geometry of 16 elements is too distorted. Check the nodal coordinates or node numbering on elements identified in element set ErrElemDistorted.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '61 elements are distorted. Either the isoparametric angles are out of the suggested limits or the triangular or tetrahedral quality measure is bad. The elements have been identified in element set WarnElemDistorted.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'The area of 9 elements is zero, small, or negative. Check coordinates or node numbering, or modify the mesh seed. The elements have been identified in element set ErrElemAreaSmallNegZero.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'The aspect ratio for 3 elements exceeds 100 to 1. The elements have been identified in element set WarnElemAspectRatio.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'Error in defining normal to the element surface at a node in 17 elements. The elements have been identified in element set ErrElemShellNormal.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FILE, {
    'phase': BATCHPRE_PHASE, 
    'file': 'C:\\Users\\chs17004\\Downloads\\Pressure_Box_With_Holes.odb', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ABORTED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase failed due to errors', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ERROR, {
    'message': 'Analysis Input File Processor exited with an error.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(JOB_ABORTED, {
    'message': 'Analysis Input File Processor exited with an error.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.models['Model-1'].constraints['Constraint-1'].suppress()
mdb.models['Model-1'].constraints['Constraint-5'].suppress()
mdb.jobs['Pressure_Box_With_Holes'].submit(consistencyChecking=OFF)
mdb.jobs['Pressure_Box_With_Holes']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'FFM5TW1', 'handle': 0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'THE SLAVE SURFACES ASSEMBLY_Side 1 slave surface AND ASSEMBLY_S_SURF-37 INTERSECT EACH OTHER. THEY ARE PAIRED WITH MASTER SURFACES ASSEMBLY_BOTTOM_MASTER_SURFACE AND ASSEMBLY_M_SURF-37 THAT ALSO INTERSECT EACH OTHER. IF BOTH PAIRS ARE *CONTACT PAIRs, THESE TWO PAIRS SHOULD NOT BE SIMULTANEOUSLY PRESENT IN A STEP BECAUSE OF POSSIBLE CONVERGENCE PROBLEMS; USE *MODEL CHANGE,TYPE=CONTACT PAIR TO REMOVE ONE OF THEM. IF BOTH ARE *TIE PAIRS, THE REDUNDANT TIES WILL BE REMOVED AUTOMATICALLY. IF ONE PAIR IS *TIE AND ANOTHER IS *CONTACT PAIR, REMOVE ONE OF THEM.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FILE, {
    'phase': BATCHPRE_PHASE, 
    'file': 'C:\\Users\\chs17004\\Downloads\\Pressure_Box_With_Holes.odb', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(COMPLETED, {
    'phase': BATCHPRE_PHASE, 'message': 'Analysis phase complete', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'FFM5TW1', 'handle': 13340, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STEP, {'phase': STANDARD_PHASE, 
    'stepId': 1, 'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THERE ARE 6 UNCONNECTED REGIONS IN THE MODEL.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(MEMORY_ESTIMATE, {
    'phase': STANDARD_PHASE, 'jobName': 'Pressure_Box_With_Holes', 
    'memory': 78.0})
mdb.jobs['Pressure_Box_With_Holes']._Message(PHYSICAL_MEMORY, {
    'phase': STANDARD_PHASE, 'physical_memory': 8147.0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(MINIMUM_MEMORY, {
    'minimum_memory': 52.0, 'phase': STANDARD_PHASE, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'DISPLACEMENT INCREMENT FOR CONTACT IS TOO BIG.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'DISPLACEMENT INCREMENT FOR CONTACT IS TOO BIG.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'DISPLACEMENT INCREMENT FOR CONTACT IS TOO BIG.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'DISPLACEMENT INCREMENT FOR CONTACT IS TOO BIG.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STATUS, {'totalTime': 0.0, 
    'attempts': ' 1U', 'timeIncrement': 1.0, 'increment': 1, 'stepTime': 0.0, 
    'step': 1, 'jobName': 'Pressure_Box_With_Holes', 'severe': 0, 
    'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'DISPLACEMENT INCREMENT FOR CONTACT IS TOO BIG.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'DISPLACEMENT INCREMENT FOR CONTACT IS TOO BIG.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'DISPLACEMENT INCREMENT FOR CONTACT IS TOO BIG.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'DISPLACEMENT INCREMENT FOR CONTACT IS TOO BIG.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STATUS, {'totalTime': 0.0, 
    'attempts': ' 2U', 'timeIncrement': 0.25, 'increment': 1, 'stepTime': 0.0, 
    'step': 1, 'jobName': 'Pressure_Box_With_Holes', 'severe': 0, 
    'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'DISPLACEMENT INCREMENT FOR CONTACT IS TOO BIG.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'DISPLACEMENT INCREMENT FOR CONTACT IS TOO BIG.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'DISPLACEMENT INCREMENT FOR CONTACT IS TOO BIG.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'DISPLACEMENT INCREMENT FOR CONTACT IS TOO BIG.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STATUS, {'totalTime': 0.0, 
    'attempts': ' 3U', 'timeIncrement': 0.0625, 'increment': 1, 
    'stepTime': 0.0, 'step': 1, 'jobName': 'Pressure_Box_With_Holes', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'DISPLACEMENT INCREMENT FOR CONTACT IS TOO BIG.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'DISPLACEMENT INCREMENT FOR CONTACT IS TOO BIG.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'DISPLACEMENT INCREMENT FOR CONTACT IS TOO BIG.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'DISPLACEMENT INCREMENT FOR CONTACT IS TOO BIG.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STATUS, {'totalTime': 0.0, 
    'attempts': ' 4U', 'timeIncrement': 0.015625, 'increment': 1, 
    'stepTime': 0.0, 'step': 1, 'jobName': 'Pressure_Box_With_Holes', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'DISPLACEMENT INCREMENT FOR CONTACT IS TOO BIG.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'DISPLACEMENT INCREMENT FOR CONTACT IS TOO BIG.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'DISPLACEMENT INCREMENT FOR CONTACT IS TOO BIG.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'DISPLACEMENT INCREMENT FOR CONTACT IS TOO BIG.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STATUS, {'totalTime': 0.0, 
    'attempts': ' 5U', 'timeIncrement': 0.00390625, 'increment': 1, 
    'stepTime': 0.0, 'step': 1, 'jobName': 'Pressure_Box_With_Holes', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Pressure_Box_With_Holes']._Message(ERROR, {'phase': STANDARD_PHASE, 
    'message': 'Too many attempts made for this increment', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ABORTED, {'phase': STANDARD_PHASE, 
    'message': 'Analysis phase failed due to errors', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ERROR, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(JOB_ABORTED, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.models['Model-1'].constraints['Constraint-8'].resume()
mdb.models['Model-1'].constraints['Constraint-3'].resume()
mdb.models['Model-1'].constraints['Constraint-4'].resume()
mdb.models['Model-1'].constraints['Constraint-5'].resume()
mdb.models['Model-1'].constraints['Constraint-6'].resume()
mdb.models['Model-1'].constraints['Constraint-7'].resume()
mdb.models['Model-1'].constraints['Constraint-1'].resume()
mdb.models['Model-1'].rootAssembly.deleteFeatures(('Edge to Edge-4', 
    'Edge to Edge-5', 'Edge to Edge-6', 'Edge to Edge-7'))
mdb.models['Model-1'].interactions['Int-6'].suppress()
mdb.models['Model-1'].constraints['Constraint-6'].suppress()
mdb.models['Model-1'].constraints['Constraint-5'].suppress()
mdb.models['Model-1'].constraints['Constraint-3'].suppress()
mdb.models['Model-1'].constraints['Constraint-4'].suppress()
mdb.models['Model-1'].constraints['Constraint-6'].resume()
mdb.models['Model-1'].constraints['Constraint-5'].resume()
mdb.jobs['Pressure_Box_With_Holes'].submit(consistencyChecking=OFF)
mdb.jobs['Pressure_Box_With_Holes']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'FFM5TW1', 'handle': 0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'THE SLAVE SURFACES ASSEMBLY_Side 1 slave surface AND ASSEMBLY_S_SURF-37 INTERSECT EACH OTHER. THEY ARE PAIRED WITH MASTER SURFACES ASSEMBLY_BOTTOM_MASTER_SURFACE AND ASSEMBLY_M_SURF-37 THAT ALSO INTERSECT EACH OTHER. IF BOTH PAIRS ARE *CONTACT PAIRs, THESE TWO PAIRS SHOULD NOT BE SIMULTANEOUSLY PRESENT IN A STEP BECAUSE OF POSSIBLE CONVERGENCE PROBLEMS; USE *MODEL CHANGE,TYPE=CONTACT PAIR TO REMOVE ONE OF THEM. IF BOTH ARE *TIE PAIRS, THE REDUNDANT TIES WILL BE REMOVED AUTOMATICALLY. IF ONE PAIR IS *TIE AND ANOTHER IS *CONTACT PAIR, REMOVE ONE OF THEM.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-14_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), NOT ALL THE NODES THAT HAVE BEEN ADJUSTED WERE PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), ADJUSTED NODES WITH VERY SMALL ADJUSTMENTS WERE NOT PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-45,ASSEMBLY_M_SURF-45) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-45-ASSEMBLY_M_SURF-45), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-47,ASSEMBLY_M_SURF-47) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-47-ASSEMBLY_M_SURF-47), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-21_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-21_CNS_-ASSEMBLY_M_SURF-49), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-22_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-22_CNS_-ASSEMBLY_M_SET-22_CNS_), ADJUSTED NODES WITH VERY SMALL ADJUSTMENTS WERE NOT PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '98 nodes have been adjusted. The nodes have been identified in node set WarnNodeAdjust.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 31 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 31 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 62 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 62 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 372 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 372 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 403 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 403 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 32 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 32 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 342 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 342 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 373 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 373 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 9 INSTANCE Short Side-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 100 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 9 INSTANCE Short Side-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 100 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 13 INSTANCE Short Side-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 13 INSTANCE Short Side-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 2 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 2 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE Short Side-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE Short Side-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE Short Side-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE Short Side-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 5 INSTANCE Short Side-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 96 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 5 INSTANCE Short Side-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 96 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 373 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 373 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 374 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 374 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 373 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE Short Side-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 373 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE Short Side-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 19 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 19 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 50 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 189 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 50 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 189 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 51 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 190 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 51 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 190 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 52 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 191 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 52 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 191 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 53 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 53 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 402 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 402 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 403 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 403 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 403 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 403 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 20 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 20 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 30 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 30 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 31 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 31 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 31 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 31 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 43 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 182 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 43 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 182 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 44 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 183 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 44 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 183 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 45 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 184 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 45 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 184 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 46 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 185 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 46 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 185 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 47 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 186 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 47 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 186 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 48 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 187 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 48 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 187 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 49 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 187 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 49 INSTANCE Short Side With Holes-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 187 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 3 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 116 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 3 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 116 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 4 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 117 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 4 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 117 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 5 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 118 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 5 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 118 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 6 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 118 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 6 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 118 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 7 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 119 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 7 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 119 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 8 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 121 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 8 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 121 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 9 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 122 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 9 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 122 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 10 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 122 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 10 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 122 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 11 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 123 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 11 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 123 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 12 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 125 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 12 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 125 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 13 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 126 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 13 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 126 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 14 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 126 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 14 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 126 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 15 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 127 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 15 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 127 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 129 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 129 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 17 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 130 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 17 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 130 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 18 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 131 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 18 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 131 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 19 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 131 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 19 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 131 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 20 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 132 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 20 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 132 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 21 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 134 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 21 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 134 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 22 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 134 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 22 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 134 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 23 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 136 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 23 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 136 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 24 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 136 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 24 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 136 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 25 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 138 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 25 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 138 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 26 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 138 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 26 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 138 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 27 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 139 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 27 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 139 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 28 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 141 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 28 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 141 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 29 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 141 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 29 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 141 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 375 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 91 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 375 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 91 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 376 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 90 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 376 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 90 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 377 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 89 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 377 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 89 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 378 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 89 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 378 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 89 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 379 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 88 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 379 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 88 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 380 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 86 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 380 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 86 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 381 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 85 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 381 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 85 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 382 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 85 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 382 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 85 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 383 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 84 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 383 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 84 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 384 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 82 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 384 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 82 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 385 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 81 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 385 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 81 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 386 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 81 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 386 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 81 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 387 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 80 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 387 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 80 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 388 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 78 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 388 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 78 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 389 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 77 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 389 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 77 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 390 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 76 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 390 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 76 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 391 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 76 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 391 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 76 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 392 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 75 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 392 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 75 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 393 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 73 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 393 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 73 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 394 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 73 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 394 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 73 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 395 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 71 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 395 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 71 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 396 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 71 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 396 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 71 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 397 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 69 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 397 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 69 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 398 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 69 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 398 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 69 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 399 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 68 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 399 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 68 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 400 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 66 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 400 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 66 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 401 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 66 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 401 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 66 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '1042 nodes are either missing intersection with their respective master surface or are outside the adjust zone. The nodes have been identified in node set WarnNodeMissMasterIntersect.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'Normal cannot be computed in 17 elements. The nodal coordinates may be incorrect or the element aspect ratio may exceed 1000 to 1. The elements have been identified in element set ErrElemNormal.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '87 nodes are used more than once as a slave node in *TIE keyword. One of the *TIE constraints at each of these nodes have been removed. The nodes have been identified in node set WarnNodeOverconTieSlave.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'The geometry of 16 elements is too distorted. Check the nodal coordinates or node numbering on elements identified in element set ErrElemDistorted.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '61 elements are distorted. Either the isoparametric angles are out of the suggested limits or the triangular or tetrahedral quality measure is bad. The elements have been identified in element set WarnElemDistorted.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'The area of 9 elements is zero, small, or negative. Check coordinates or node numbering, or modify the mesh seed. The elements have been identified in element set ErrElemAreaSmallNegZero.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'The aspect ratio for 3 elements exceeds 100 to 1. The elements have been identified in element set WarnElemAspectRatio.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'Error in defining normal to the element surface at a node in 17 elements. The elements have been identified in element set ErrElemShellNormal.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FILE, {
    'phase': BATCHPRE_PHASE, 
    'file': 'C:\\Users\\chs17004\\Downloads\\Pressure_Box_With_Holes.odb', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ABORTED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase failed due to errors', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ERROR, {
    'message': 'Analysis Input File Processor exited with an error.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(JOB_ABORTED, {
    'message': 'Analysis Input File Processor exited with an error.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.models['Model-1'].interactions.changeKey(fromName='Int-10', 
    toName='Sides to Cap')
mdb.models['Model-1'].interactions.changeKey(fromName='Int-7', 
    toName='Sides to sides')
mdb.models['Model-1'].constraints.changeKey(fromName='Constraint-1', 
    toName='Bottom to Sides')
mdb.models['Model-1'].constraints.changeKey(fromName='Constraint-5', 
    toName='Sides to sides')
mdb.models['Model-1'].constraints.changeKey(fromName='Constraint-6', 
    toName='Cap to sides')
mdb.models['Model-1'].constraints['Constraint-8'].suppress()
mdb.models['Model-1'].constraints['Constraint-7'].suppress()
mdb.jobs['Pressure_Box_With_Holes'].submit(consistencyChecking=OFF)
mdb.jobs['Pressure_Box_With_Holes']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'FFM5TW1', 'handle': 0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'THE SLAVE SURFACES ASSEMBLY_Side 1 slave surface AND ASSEMBLY_S_SURF-37 INTERSECT EACH OTHER. THEY ARE PAIRED WITH MASTER SURFACES ASSEMBLY_BOTTOM_MASTER_SURFACE AND ASSEMBLY_M_SURF-37 THAT ALSO INTERSECT EACH OTHER. IF BOTH PAIRS ARE *CONTACT PAIRs, THESE TWO PAIRS SHOULD NOT BE SIMULTANEOUSLY PRESENT IN A STEP BECAUSE OF POSSIBLE CONVERGENCE PROBLEMS; USE *MODEL CHANGE,TYPE=CONTACT PAIR TO REMOVE ONE OF THEM. IF BOTH ARE *TIE PAIRS, THE REDUNDANT TIES WILL BE REMOVED AUTOMATICALLY. IF ONE PAIR IS *TIE AND ANOTHER IS *CONTACT PAIR, REMOVE ONE OF THEM.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-14_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), NOT ALL THE NODES THAT HAVE BEEN ADJUSTED WERE PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), ADJUSTED NODES WITH VERY SMALL ADJUSTMENTS WERE NOT PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-47,ASSEMBLY_M_SURF-47) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-47-ASSEMBLY_M_SURF-47), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-45,ASSEMBLY_M_SURF-45) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-45-ASSEMBLY_M_SURF-45), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '98 nodes have been adjusted. The nodes have been identified in node set WarnNodeAdjust.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 32 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 32 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 342 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 342 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 373 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 373 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 373 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 373 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '1042 nodes are either missing intersection with their respective master surface or are outside the adjust zone. The nodes have been identified in node set WarnNodeMissMasterIntersect.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'Normal cannot be computed in 17 elements. The nodal coordinates may be incorrect or the element aspect ratio may exceed 1000 to 1. The elements have been identified in element set ErrElemNormal.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '6 nodes are used more than once as a slave node in *TIE keyword. One of the *TIE constraints at each of these nodes have been removed. The nodes have been identified in node set WarnNodeOverconTieSlave.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'The geometry of 16 elements is too distorted. Check the nodal coordinates or node numbering on elements identified in element set ErrElemDistorted.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '61 elements are distorted. Either the isoparametric angles are out of the suggested limits or the triangular or tetrahedral quality measure is bad. The elements have been identified in element set WarnElemDistorted.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'The area of 9 elements is zero, small, or negative. Check coordinates or node numbering, or modify the mesh seed. The elements have been identified in element set ErrElemAreaSmallNegZero.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'The aspect ratio for 3 elements exceeds 100 to 1. The elements have been identified in element set WarnElemAspectRatio.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'Error in defining normal to the element surface at a node in 17 elements. The elements have been identified in element set ErrElemShellNormal.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FILE, {
    'phase': BATCHPRE_PHASE, 
    'file': 'C:\\Users\\chs17004\\Downloads\\Pressure_Box_With_Holes.odb', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ABORTED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase failed due to errors', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ERROR, {
    'message': 'Analysis Input File Processor exited with an error.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(JOB_ABORTED, {
    'message': 'Analysis Input File Processor exited with an error.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.models['Model-1'].parts['Bottom'].deleteMesh()
mdb.models['Model-1'].parts['Bottom'].seedPart(minSizeFactor=0.9, size=0.05)
mdb.models['Model-1'].parts['Bottom'].generateMesh()
mdb.models['Model-1'].parts['Cap'].deleteMesh()
mdb.models['Model-1'].parts['Cap'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=0.05)
mdb.models['Model-1'].parts['Cap'].generateMesh()
mdb.models['Model-1'].parts['Long_Side'].deleteMesh()
mdb.models['Model-1'].parts['Long_Side'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=0.05)
mdb.models['Model-1'].parts['Long_Side'].generateMesh()
mdb.models['Model-1'].parts['Short Side With Holes'].deleteMesh()
mdb.models['Model-1'].parts['Short Side With Holes'].seedPart(
    deviationFactor=0.1, minSizeFactor=0.1, size=0.05)
mdb.models['Model-1'].parts['Short Side With Holes'].generateMesh()
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.jobs['Pressure_Box_With_Holes'].submit(consistencyChecking=OFF)
mdb.jobs['Pressure_Box_With_Holes']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'FFM5TW1', 'handle': 0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'THE SLAVE SURFACES ASSEMBLY_Side 1 slave surface AND ASSEMBLY_S_SURF-37 INTERSECT EACH OTHER. THEY ARE PAIRED WITH MASTER SURFACES ASSEMBLY_BOTTOM_MASTER_SURFACE AND ASSEMBLY_M_SURF-37 THAT ALSO INTERSECT EACH OTHER. IF BOTH PAIRS ARE *CONTACT PAIRs, THESE TWO PAIRS SHOULD NOT BE SIMULTANEOUSLY PRESENT IN A STEP BECAUSE OF POSSIBLE CONVERGENCE PROBLEMS; USE *MODEL CHANGE,TYPE=CONTACT PAIR TO REMOVE ONE OF THEM. IF BOTH ARE *TIE PAIRS, THE REDUNDANT TIES WILL BE REMOVED AUTOMATICALLY. IF ONE PAIR IS *TIE AND ANOTHER IS *CONTACT PAIR, REMOVE ONE OF THEM.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-14_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), NOT ALL THE NODES THAT HAVE BEEN ADJUSTED WERE PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), ADJUSTED NODES WITH VERY SMALL ADJUSTMENTS WERE NOT PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-47,ASSEMBLY_M_SURF-47) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-47-ASSEMBLY_M_SURF-47), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-45,ASSEMBLY_M_SURF-45) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-45-ASSEMBLY_M_SURF-45), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '33 nodes have been adjusted. The nodes have been identified in node set WarnNodeAdjust.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '342 nodes are either missing intersection with their respective master surface or are outside the adjust zone. The nodes have been identified in node set WarnNodeMissMasterIntersect.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '4 nodes are used more than once as a slave node in *TIE keyword. One of the *TIE constraints at each of these nodes have been removed. The nodes have been identified in node set WarnNodeOverconTieSlave.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '1 elements are distorted. Either the isoparametric angles are out of the suggested limits or the triangular or tetrahedral quality measure is bad. The elements have been identified in element set WarnElemDistorted.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '9 elements are curved/warped. The angle subtended between the average element normal and a nodal normal exceeds 10 degrees. Mesh refinement is recommended. The elements have been identified in element set WarnElemWarped.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FILE, {
    'phase': BATCHPRE_PHASE, 
    'file': 'C:\\Users\\chs17004\\Downloads\\Pressure_Box_With_Holes.odb', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(COMPLETED, {
    'phase': BATCHPRE_PHASE, 'message': 'Analysis phase complete', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'FFM5TW1', 'handle': 9448, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STEP, {'phase': STANDARD_PHASE, 
    'stepId': 1, 'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(MEMORY_ESTIMATE, {
    'phase': STANDARD_PHASE, 'jobName': 'Pressure_Box_With_Holes', 
    'memory': 38.0})
mdb.jobs['Pressure_Box_With_Holes']._Message(PHYSICAL_MEMORY, {
    'phase': STANDARD_PHASE, 'physical_memory': 8147.0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(MINIMUM_MEMORY, {
    'minimum_memory': 25.0, 'phase': STANDARD_PHASE, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 1, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STATUS, {'totalTime': 1.0, 
    'attempts': 1, 'timeIncrement': 1.0, 'increment': 1, 'stepTime': 1.0, 
    'step': 1, 'jobName': 'Pressure_Box_With_Holes', 'severe': 0, 
    'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Pressure_Box_With_Holes']._Message(END_STEP, {
    'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(COMPLETED, {
    'phase': STANDARD_PHASE, 'message': 'Analysis phase complete', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(JOB_COMPLETED, {
    'time': 'Tue Oct  6 12:13:28 2020', 'jobName': 'Pressure_Box_With_Holes'})
mdb.models['Model-1'].constraints['Constraint-8'].resume()
mdb.jobs['Pressure_Box_With_Holes'].submit(consistencyChecking=OFF)
mdb.jobs['Pressure_Box_With_Holes']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'FFM5TW1', 'handle': 0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'THE SLAVE SURFACES ASSEMBLY_Side 1 slave surface AND ASSEMBLY_S_SURF-37 INTERSECT EACH OTHER. THEY ARE PAIRED WITH MASTER SURFACES ASSEMBLY_BOTTOM_MASTER_SURFACE AND ASSEMBLY_M_SURF-37 THAT ALSO INTERSECT EACH OTHER. IF BOTH PAIRS ARE *CONTACT PAIRs, THESE TWO PAIRS SHOULD NOT BE SIMULTANEOUSLY PRESENT IN A STEP BECAUSE OF POSSIBLE CONVERGENCE PROBLEMS; USE *MODEL CHANGE,TYPE=CONTACT PAIR TO REMOVE ONE OF THEM. IF BOTH ARE *TIE PAIRS, THE REDUNDANT TIES WILL BE REMOVED AUTOMATICALLY. IF ONE PAIR IS *TIE AND ANOTHER IS *CONTACT PAIR, REMOVE ONE OF THEM.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-14_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), NOT ALL THE NODES THAT HAVE BEEN ADJUSTED WERE PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), ADJUSTED NODES WITH VERY SMALL ADJUSTMENTS WERE NOT PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-47,ASSEMBLY_M_SURF-47) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-47-ASSEMBLY_M_SURF-47), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-22_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-22_CNS_-ASSEMBLY_M_SET-22_CNS_), ADJUSTED NODES WITH VERY SMALL ADJUSTMENTS WERE NOT PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-45,ASSEMBLY_M_SURF-45) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-45-ASSEMBLY_M_SURF-45), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '33 nodes have been adjusted. The nodes have been identified in node set WarnNodeAdjust.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '342 nodes are either missing intersection with their respective master surface or are outside the adjust zone. The nodes have been identified in node set WarnNodeMissMasterIntersect.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '8 nodes are used more than once as a slave node in *TIE keyword. One of the *TIE constraints at each of these nodes have been removed. The nodes have been identified in node set WarnNodeOverconTieSlave.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '1 elements are distorted. Either the isoparametric angles are out of the suggested limits or the triangular or tetrahedral quality measure is bad. The elements have been identified in element set WarnElemDistorted.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '9 elements are curved/warped. The angle subtended between the average element normal and a nodal normal exceeds 10 degrees. Mesh refinement is recommended. The elements have been identified in element set WarnElemWarped.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FILE, {
    'phase': BATCHPRE_PHASE, 
    'file': 'C:\\Users\\chs17004\\Downloads\\Pressure_Box_With_Holes.odb', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(COMPLETED, {
    'phase': BATCHPRE_PHASE, 'message': 'Analysis phase complete', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'FFM5TW1', 'handle': 13880, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STEP, {'phase': STANDARD_PHASE, 
    'stepId': 1, 'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(MEMORY_ESTIMATE, {
    'phase': STANDARD_PHASE, 'jobName': 'Pressure_Box_With_Holes', 
    'memory': 38.0})
mdb.jobs['Pressure_Box_With_Holes']._Message(PHYSICAL_MEMORY, {
    'phase': STANDARD_PHASE, 'physical_memory': 8147.0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(MINIMUM_MEMORY, {
    'minimum_memory': 25.0, 'phase': STANDARD_PHASE, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 1, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STATUS, {'totalTime': 1.0, 
    'attempts': 1, 'timeIncrement': 1.0, 'increment': 1, 'stepTime': 1.0, 
    'step': 1, 'jobName': 'Pressure_Box_With_Holes', 'severe': 0, 
    'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Pressure_Box_With_Holes']._Message(END_STEP, {
    'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(COMPLETED, {
    'phase': STANDARD_PHASE, 'message': 'Analysis phase complete', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(JOB_COMPLETED, {
    'time': 'Tue Oct  6 12:14:14 2020', 'jobName': 'Pressure_Box_With_Holes'})
del mdb.models['Model-1'].rootAssembly.surfaces['Surf-12']
mdb.jobs['Pressure_Box_With_Holes'].submit(consistencyChecking=OFF)
mdb.jobs['Pressure_Box_With_Holes']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'FFM5TW1', 'handle': 0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'THE SLAVE SURFACES ASSEMBLY_Side 1 slave surface AND ASSEMBLY_S_SURF-37 INTERSECT EACH OTHER. THEY ARE PAIRED WITH MASTER SURFACES ASSEMBLY_BOTTOM_MASTER_SURFACE AND ASSEMBLY_M_SURF-37 THAT ALSO INTERSECT EACH OTHER. IF BOTH PAIRS ARE *CONTACT PAIRs, THESE TWO PAIRS SHOULD NOT BE SIMULTANEOUSLY PRESENT IN A STEP BECAUSE OF POSSIBLE CONVERGENCE PROBLEMS; USE *MODEL CHANGE,TYPE=CONTACT PAIR TO REMOVE ONE OF THEM. IF BOTH ARE *TIE PAIRS, THE REDUNDANT TIES WILL BE REMOVED AUTOMATICALLY. IF ONE PAIR IS *TIE AND ANOTHER IS *CONTACT PAIR, REMOVE ONE OF THEM.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-14_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), NOT ALL THE NODES THAT HAVE BEEN ADJUSTED WERE PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), ADJUSTED NODES WITH VERY SMALL ADJUSTMENTS WERE NOT PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-47,ASSEMBLY_M_SURF-47) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-47-ASSEMBLY_M_SURF-47), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-22_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-22_CNS_-ASSEMBLY_M_SET-22_CNS_), ADJUSTED NODES WITH VERY SMALL ADJUSTMENTS WERE NOT PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-45,ASSEMBLY_M_SURF-45) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-45-ASSEMBLY_M_SURF-45), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '33 nodes have been adjusted. The nodes have been identified in node set WarnNodeAdjust.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '342 nodes are either missing intersection with their respective master surface or are outside the adjust zone. The nodes have been identified in node set WarnNodeMissMasterIntersect.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '8 nodes are used more than once as a slave node in *TIE keyword. One of the *TIE constraints at each of these nodes have been removed. The nodes have been identified in node set WarnNodeOverconTieSlave.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '1 elements are distorted. Either the isoparametric angles are out of the suggested limits or the triangular or tetrahedral quality measure is bad. The elements have been identified in element set WarnElemDistorted.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '9 elements are curved/warped. The angle subtended between the average element normal and a nodal normal exceeds 10 degrees. Mesh refinement is recommended. The elements have been identified in element set WarnElemWarped.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FILE, {
    'phase': BATCHPRE_PHASE, 
    'file': 'C:\\Users\\chs17004\\Downloads\\Pressure_Box_With_Holes.odb', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(COMPLETED, {
    'phase': BATCHPRE_PHASE, 'message': 'Analysis phase complete', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'FFM5TW1', 'handle': 9340, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STEP, {'phase': STANDARD_PHASE, 
    'stepId': 1, 'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(MEMORY_ESTIMATE, {
    'phase': STANDARD_PHASE, 'jobName': 'Pressure_Box_With_Holes', 
    'memory': 38.0})
mdb.jobs['Pressure_Box_With_Holes']._Message(PHYSICAL_MEMORY, {
    'phase': STANDARD_PHASE, 'physical_memory': 8147.0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(MINIMUM_MEMORY, {
    'minimum_memory': 25.0, 'phase': STANDARD_PHASE, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 1, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STATUS, {'totalTime': 1.0, 
    'attempts': 1, 'timeIncrement': 1.0, 'increment': 1, 'stepTime': 1.0, 
    'step': 1, 'jobName': 'Pressure_Box_With_Holes', 'severe': 0, 
    'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Pressure_Box_With_Holes']._Message(END_STEP, {
    'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(COMPLETED, {
    'phase': STANDARD_PHASE, 'message': 'Analysis phase complete', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(JOB_COMPLETED, {
    'time': 'Tue Oct  6 12:16:51 2020', 'jobName': 'Pressure_Box_With_Holes'})
del mdb.models['Model-1'].rootAssembly.surfaces['Surf-4']
del mdb.models['Model-1'].rootAssembly.surfaces['Surf-11']
mdb.jobs['Pressure_Box_With_Holes'].submit(consistencyChecking=OFF)
mdb.jobs['Pressure_Box_With_Holes']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'FFM5TW1', 'handle': 0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'THE SLAVE SURFACES ASSEMBLY_Side 1 slave surface AND ASSEMBLY_S_SURF-37 INTERSECT EACH OTHER. THEY ARE PAIRED WITH MASTER SURFACES ASSEMBLY_BOTTOM_MASTER_SURFACE AND ASSEMBLY_M_SURF-37 THAT ALSO INTERSECT EACH OTHER. IF BOTH PAIRS ARE *CONTACT PAIRs, THESE TWO PAIRS SHOULD NOT BE SIMULTANEOUSLY PRESENT IN A STEP BECAUSE OF POSSIBLE CONVERGENCE PROBLEMS; USE *MODEL CHANGE,TYPE=CONTACT PAIR TO REMOVE ONE OF THEM. IF BOTH ARE *TIE PAIRS, THE REDUNDANT TIES WILL BE REMOVED AUTOMATICALLY. IF ONE PAIR IS *TIE AND ANOTHER IS *CONTACT PAIR, REMOVE ONE OF THEM.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-14_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), NOT ALL THE NODES THAT HAVE BEEN ADJUSTED WERE PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), ADJUSTED NODES WITH VERY SMALL ADJUSTMENTS WERE NOT PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-47,ASSEMBLY_M_SURF-47) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-47-ASSEMBLY_M_SURF-47), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-22_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-22_CNS_-ASSEMBLY_M_SET-22_CNS_), ADJUSTED NODES WITH VERY SMALL ADJUSTMENTS WERE NOT PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-45,ASSEMBLY_M_SURF-45) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-45-ASSEMBLY_M_SURF-45), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '33 nodes have been adjusted. The nodes have been identified in node set WarnNodeAdjust.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '342 nodes are either missing intersection with their respective master surface or are outside the adjust zone. The nodes have been identified in node set WarnNodeMissMasterIntersect.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '8 nodes are used more than once as a slave node in *TIE keyword. One of the *TIE constraints at each of these nodes have been removed. The nodes have been identified in node set WarnNodeOverconTieSlave.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '1 elements are distorted. Either the isoparametric angles are out of the suggested limits or the triangular or tetrahedral quality measure is bad. The elements have been identified in element set WarnElemDistorted.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '9 elements are curved/warped. The angle subtended between the average element normal and a nodal normal exceeds 10 degrees. Mesh refinement is recommended. The elements have been identified in element set WarnElemWarped.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FILE, {
    'phase': BATCHPRE_PHASE, 
    'file': 'C:\\Users\\chs17004\\Downloads\\Pressure_Box_With_Holes.odb', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(COMPLETED, {
    'phase': BATCHPRE_PHASE, 'message': 'Analysis phase complete', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'FFM5TW1', 'handle': 8592, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STEP, {'phase': STANDARD_PHASE, 
    'stepId': 1, 'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(MEMORY_ESTIMATE, {
    'phase': STANDARD_PHASE, 'jobName': 'Pressure_Box_With_Holes', 
    'memory': 38.0})
mdb.jobs['Pressure_Box_With_Holes']._Message(PHYSICAL_MEMORY, {
    'phase': STANDARD_PHASE, 'physical_memory': 8147.0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(MINIMUM_MEMORY, {
    'minimum_memory': 25.0, 'phase': STANDARD_PHASE, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 1, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STATUS, {'totalTime': 1.0, 
    'attempts': 1, 'timeIncrement': 1.0, 'increment': 1, 'stepTime': 1.0, 
    'step': 1, 'jobName': 'Pressure_Box_With_Holes', 'severe': 0, 
    'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Pressure_Box_With_Holes']._Message(END_STEP, {
    'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(COMPLETED, {
    'phase': STANDARD_PHASE, 'message': 'Analysis phase complete', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(JOB_COMPLETED, {
    'time': 'Tue Oct  6 12:18:41 2020', 'jobName': 'Pressure_Box_With_Holes'})
del mdb.models['Model-1'].rootAssembly.surfaces['m_Surf-1']
del mdb.models['Model-1'].rootAssembly.surfaces['m_Surf-2']
mdb.models['Model-1'].rootAssembly.deleteSurfaces(surfaceNames=('m_Surf-5', 
    'm_Surf-6', 'm_Surf-7', 'm_Surf-8', 'm_Surf-9'))
mdb.jobs['Pressure_Box_With_Holes'].submit(consistencyChecking=OFF, 
    datacheckJob=True)
mdb.jobs['Pressure_Box_With_Holes']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'FFM5TW1', 'handle': 0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'THE SLAVE SURFACES ASSEMBLY_Side 1 slave surface AND ASSEMBLY_S_SURF-37 INTERSECT EACH OTHER. THEY ARE PAIRED WITH MASTER SURFACES ASSEMBLY_BOTTOM_MASTER_SURFACE AND ASSEMBLY_M_SURF-37 THAT ALSO INTERSECT EACH OTHER. IF BOTH PAIRS ARE *CONTACT PAIRs, THESE TWO PAIRS SHOULD NOT BE SIMULTANEOUSLY PRESENT IN A STEP BECAUSE OF POSSIBLE CONVERGENCE PROBLEMS; USE *MODEL CHANGE,TYPE=CONTACT PAIR TO REMOVE ONE OF THEM. IF BOTH ARE *TIE PAIRS, THE REDUNDANT TIES WILL BE REMOVED AUTOMATICALLY. IF ONE PAIR IS *TIE AND ANOTHER IS *CONTACT PAIR, REMOVE ONE OF THEM.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-14_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), NOT ALL THE NODES THAT HAVE BEEN ADJUSTED WERE PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), ADJUSTED NODES WITH VERY SMALL ADJUSTMENTS WERE NOT PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-47,ASSEMBLY_M_SURF-47) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-47-ASSEMBLY_M_SURF-47), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-22_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-22_CNS_-ASSEMBLY_M_SET-22_CNS_), ADJUSTED NODES WITH VERY SMALL ADJUSTMENTS WERE NOT PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-45,ASSEMBLY_M_SURF-45) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-45-ASSEMBLY_M_SURF-45), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '33 nodes have been adjusted. The nodes have been identified in node set WarnNodeAdjust.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '342 nodes are either missing intersection with their respective master surface or are outside the adjust zone. The nodes have been identified in node set WarnNodeMissMasterIntersect.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '8 nodes are used more than once as a slave node in *TIE keyword. One of the *TIE constraints at each of these nodes have been removed. The nodes have been identified in node set WarnNodeOverconTieSlave.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '1 elements are distorted. Either the isoparametric angles are out of the suggested limits or the triangular or tetrahedral quality measure is bad. The elements have been identified in element set WarnElemDistorted.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '9 elements are curved/warped. The angle subtended between the average element normal and a nodal normal exceeds 10 degrees. Mesh refinement is recommended. The elements have been identified in element set WarnElemWarped.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FILE, {
    'phase': BATCHPRE_PHASE, 
    'file': 'C:\\Users\\chs17004\\Downloads\\Pressure_Box_With_Holes.odb', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(COMPLETED, {
    'phase': BATCHPRE_PHASE, 'message': 'Analysis phase complete', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'FFM5TW1', 'handle': 7420, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STEP, {'phase': STANDARD_PHASE, 
    'stepId': 1, 'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(MEMORY_ESTIMATE, {
    'phase': STANDARD_PHASE, 'jobName': 'Pressure_Box_With_Holes', 
    'memory': 17.0})
mdb.jobs['Pressure_Box_With_Holes']._Message(PHYSICAL_MEMORY, {
    'phase': STANDARD_PHASE, 'physical_memory': 8147.0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(MINIMUM_MEMORY, {
    'minimum_memory': 13.0, 'phase': STANDARD_PHASE, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(COMPLETED, {
    'phase': STANDARD_PHASE, 'message': 'Analysis phase complete', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(JOB_COMPLETED, {
    'time': 'Tue Oct  6 12:19:13 2020', 'jobName': 'Pressure_Box_With_Holes'})
del mdb.models['Model-1'].rootAssembly.surfaces['m_Surf-16']
del mdb.models['Model-1'].rootAssembly.surfaces['m_Surf-24']
mdb.models['Model-1'].rootAssembly.deleteSurfaces(surfaceNames=('m_Surf-26', 
    'm_Surf-27', 'm_Surf-28', 'm_Surf-29'))
mdb.models['Model-1'].rootAssembly.deleteSurfaces(surfaceNames=('m_Surf-33', 
    'm_Surf-35'))
mdb.models['Model-1'].rootAssembly.deleteSurfaces(surfaceNames=('m_Surf-41', 
    'm_Surf-43'))
mdb.models['Model-1'].rootAssembly.deleteSurfaces(surfaceNames=('m_Surf-49', 
    'm_Surf-50'))
mdb.jobs['Pressure_Box_With_Holes'].submit(consistencyChecking=OFF)
mdb.jobs['Pressure_Box_With_Holes']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'FFM5TW1', 'handle': 0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'THE SLAVE SURFACES ASSEMBLY_Side 1 slave surface AND ASSEMBLY_S_SURF-37 INTERSECT EACH OTHER. THEY ARE PAIRED WITH MASTER SURFACES ASSEMBLY_BOTTOM_MASTER_SURFACE AND ASSEMBLY_M_SURF-37 THAT ALSO INTERSECT EACH OTHER. IF BOTH PAIRS ARE *CONTACT PAIRs, THESE TWO PAIRS SHOULD NOT BE SIMULTANEOUSLY PRESENT IN A STEP BECAUSE OF POSSIBLE CONVERGENCE PROBLEMS; USE *MODEL CHANGE,TYPE=CONTACT PAIR TO REMOVE ONE OF THEM. IF BOTH ARE *TIE PAIRS, THE REDUNDANT TIES WILL BE REMOVED AUTOMATICALLY. IF ONE PAIR IS *TIE AND ANOTHER IS *CONTACT PAIR, REMOVE ONE OF THEM.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-14_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), NOT ALL THE NODES THAT HAVE BEEN ADJUSTED WERE PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), ADJUSTED NODES WITH VERY SMALL ADJUSTMENTS WERE NOT PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-47,ASSEMBLY_M_SURF-47) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-47-ASSEMBLY_M_SURF-47), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-22_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-22_CNS_-ASSEMBLY_M_SET-22_CNS_), ADJUSTED NODES WITH VERY SMALL ADJUSTMENTS WERE NOT PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-45,ASSEMBLY_M_SURF-45) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-45-ASSEMBLY_M_SURF-45), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '33 nodes have been adjusted. The nodes have been identified in node set WarnNodeAdjust.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '342 nodes are either missing intersection with their respective master surface or are outside the adjust zone. The nodes have been identified in node set WarnNodeMissMasterIntersect.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '8 nodes are used more than once as a slave node in *TIE keyword. One of the *TIE constraints at each of these nodes have been removed. The nodes have been identified in node set WarnNodeOverconTieSlave.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '1 elements are distorted. Either the isoparametric angles are out of the suggested limits or the triangular or tetrahedral quality measure is bad. The elements have been identified in element set WarnElemDistorted.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '9 elements are curved/warped. The angle subtended between the average element normal and a nodal normal exceeds 10 degrees. Mesh refinement is recommended. The elements have been identified in element set WarnElemWarped.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FILE, {
    'phase': BATCHPRE_PHASE, 
    'file': 'C:\\Users\\chs17004\\Downloads\\Pressure_Box_With_Holes.odb', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(COMPLETED, {
    'phase': BATCHPRE_PHASE, 'message': 'Analysis phase complete', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'FFM5TW1', 'handle': 4516, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STEP, {'phase': STANDARD_PHASE, 
    'stepId': 1, 'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(MEMORY_ESTIMATE, {
    'phase': STANDARD_PHASE, 'jobName': 'Pressure_Box_With_Holes', 
    'memory': 38.0})
mdb.jobs['Pressure_Box_With_Holes']._Message(PHYSICAL_MEMORY, {
    'phase': STANDARD_PHASE, 'physical_memory': 8147.0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(MINIMUM_MEMORY, {
    'minimum_memory': 25.0, 'phase': STANDARD_PHASE, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 1, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STATUS, {'totalTime': 1.0, 
    'attempts': 1, 'timeIncrement': 1.0, 'increment': 1, 'stepTime': 1.0, 
    'step': 1, 'jobName': 'Pressure_Box_With_Holes', 'severe': 0, 
    'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Pressure_Box_With_Holes']._Message(END_STEP, {
    'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(COMPLETED, {
    'phase': STANDARD_PHASE, 'message': 'Analysis phase complete', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(JOB_COMPLETED, {
    'time': 'Tue Oct  6 12:20:38 2020', 'jobName': 'Pressure_Box_With_Holes'})
mdb.models['Model-1'].rootAssembly.deleteSurfaces(surfaceNames=('s_Surf-2', 
    's_Surf-9', 's_Surf-19'))
mdb.models['Model-1'].rootAssembly.deleteSurfaces(surfaceNames=('s_Surf-20', 
    's_Surf-21'))
mdb.models['Model-1'].rootAssembly.deleteSurfaces(surfaceNames=('s_Surf-22', 
    's_Surf-24', 's_Surf-30'))
mdb.models['Model-1'].rootAssembly.deleteSurfaces(surfaceNames=('s_Surf-33', 
    's_Surf-35'))
mdb.models['Model-1'].rootAssembly.deleteSurfaces(surfaceNames=('s_Surf-41', 
    's_Surf-43'))
del mdb.models['Model-1'].rootAssembly.surfaces['s_Surf-50']
mdb.jobs['Pressure_Box_With_Holes'].submit(consistencyChecking=OFF)
mdb.jobs['Pressure_Box_With_Holes']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'FFM5TW1', 'handle': 0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'THE SLAVE SURFACES ASSEMBLY_Side 1 slave surface AND ASSEMBLY_S_SURF-37 INTERSECT EACH OTHER. THEY ARE PAIRED WITH MASTER SURFACES ASSEMBLY_BOTTOM_MASTER_SURFACE AND ASSEMBLY_M_SURF-37 THAT ALSO INTERSECT EACH OTHER. IF BOTH PAIRS ARE *CONTACT PAIRs, THESE TWO PAIRS SHOULD NOT BE SIMULTANEOUSLY PRESENT IN A STEP BECAUSE OF POSSIBLE CONVERGENCE PROBLEMS; USE *MODEL CHANGE,TYPE=CONTACT PAIR TO REMOVE ONE OF THEM. IF BOTH ARE *TIE PAIRS, THE REDUNDANT TIES WILL BE REMOVED AUTOMATICALLY. IF ONE PAIR IS *TIE AND ANOTHER IS *CONTACT PAIR, REMOVE ONE OF THEM.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-14_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), NOT ALL THE NODES THAT HAVE BEEN ADJUSTED WERE PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), ADJUSTED NODES WITH VERY SMALL ADJUSTMENTS WERE NOT PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-47,ASSEMBLY_M_SURF-47) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-47-ASSEMBLY_M_SURF-47), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-22_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-22_CNS_-ASSEMBLY_M_SET-22_CNS_), ADJUSTED NODES WITH VERY SMALL ADJUSTMENTS WERE NOT PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-45,ASSEMBLY_M_SURF-45) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-45-ASSEMBLY_M_SURF-45), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '33 nodes have been adjusted. The nodes have been identified in node set WarnNodeAdjust.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '342 nodes are either missing intersection with their respective master surface or are outside the adjust zone. The nodes have been identified in node set WarnNodeMissMasterIntersect.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '8 nodes are used more than once as a slave node in *TIE keyword. One of the *TIE constraints at each of these nodes have been removed. The nodes have been identified in node set WarnNodeOverconTieSlave.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '1 elements are distorted. Either the isoparametric angles are out of the suggested limits or the triangular or tetrahedral quality measure is bad. The elements have been identified in element set WarnElemDistorted.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '9 elements are curved/warped. The angle subtended between the average element normal and a nodal normal exceeds 10 degrees. Mesh refinement is recommended. The elements have been identified in element set WarnElemWarped.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FILE, {
    'phase': BATCHPRE_PHASE, 
    'file': 'C:\\Users\\chs17004\\Downloads\\Pressure_Box_With_Holes.odb', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(COMPLETED, {
    'phase': BATCHPRE_PHASE, 'message': 'Analysis phase complete', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'FFM5TW1', 'handle': 12304, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STEP, {'phase': STANDARD_PHASE, 
    'stepId': 1, 'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(MEMORY_ESTIMATE, {
    'phase': STANDARD_PHASE, 'jobName': 'Pressure_Box_With_Holes', 
    'memory': 38.0})
mdb.jobs['Pressure_Box_With_Holes']._Message(PHYSICAL_MEMORY, {
    'phase': STANDARD_PHASE, 'physical_memory': 8147.0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(MINIMUM_MEMORY, {
    'minimum_memory': 25.0, 'phase': STANDARD_PHASE, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 1, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STATUS, {'totalTime': 1.0, 
    'attempts': 1, 'timeIncrement': 1.0, 'increment': 1, 'stepTime': 1.0, 
    'step': 1, 'jobName': 'Pressure_Box_With_Holes', 'severe': 0, 
    'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Pressure_Box_With_Holes']._Message(END_STEP, {
    'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(COMPLETED, {
    'phase': STANDARD_PHASE, 'message': 'Analysis phase complete', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(JOB_COMPLETED, {
    'time': 'Tue Oct  6 12:21:55 2020', 'jobName': 'Pressure_Box_With_Holes'})
mdb.models['Model-1'].rootAssembly.Set(
    faces=mdb.models['Model-1'].rootAssembly.instances['Short Side-1'].faces.getSequenceFromMask(
    mask=('[#1 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Long_Side-1'].faces.getSequenceFromMask(
    mask=('[#1 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Short Side With Holes-1'].faces.getSequenceFromMask(
    mask=('[#1 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Long_Side-2'].faces.getSequenceFromMask(
    mask=('[#1 ]', ), ), name='s_Set-14')
mdb.models['Model-1'].rootAssembly.Surface(name='Bottom_master_surface', 
    side2Faces=mdb.models['Model-1'].rootAssembly.instances['Bottom-1'].faces.getSequenceFromMask(
    ('[#1ff ]', ), ))
mdb.jobs['Pressure_Box_With_Holes'].submit(consistencyChecking=OFF)
mdb.jobs['Pressure_Box_With_Holes']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'FFM5TW1', 'handle': 0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'THE SLAVE SURFACES ASSEMBLY_Side 1 slave surface AND ASSEMBLY_S_SURF-37 INTERSECT EACH OTHER. THEY ARE PAIRED WITH MASTER SURFACES ASSEMBLY_BOTTOM_MASTER_SURFACE AND ASSEMBLY_M_SURF-37 THAT ALSO INTERSECT EACH OTHER. IF BOTH PAIRS ARE *CONTACT PAIRs, THESE TWO PAIRS SHOULD NOT BE SIMULTANEOUSLY PRESENT IN A STEP BECAUSE OF POSSIBLE CONVERGENCE PROBLEMS; USE *MODEL CHANGE,TYPE=CONTACT PAIR TO REMOVE ONE OF THEM. IF BOTH ARE *TIE PAIRS, THE REDUNDANT TIES WILL BE REMOVED AUTOMATICALLY. IF ONE PAIR IS *TIE AND ANOTHER IS *CONTACT PAIR, REMOVE ONE OF THEM.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-14_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), NOT ALL THE NODES THAT HAVE BEEN ADJUSTED WERE PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), ADJUSTED NODES WITH VERY SMALL ADJUSTMENTS WERE NOT PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-47,ASSEMBLY_M_SURF-47) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-47-ASSEMBLY_M_SURF-47), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-22_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-22_CNS_-ASSEMBLY_M_SET-22_CNS_), ADJUSTED NODES WITH VERY SMALL ADJUSTMENTS WERE NOT PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-45,ASSEMBLY_M_SURF-45) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-45-ASSEMBLY_M_SURF-45), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '33 nodes have been adjusted. The nodes have been identified in node set WarnNodeAdjust.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '342 nodes are either missing intersection with their respective master surface or are outside the adjust zone. The nodes have been identified in node set WarnNodeMissMasterIntersect.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '8 nodes are used more than once as a slave node in *TIE keyword. One of the *TIE constraints at each of these nodes have been removed. The nodes have been identified in node set WarnNodeOverconTieSlave.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '1 elements are distorted. Either the isoparametric angles are out of the suggested limits or the triangular or tetrahedral quality measure is bad. The elements have been identified in element set WarnElemDistorted.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '9 elements are curved/warped. The angle subtended between the average element normal and a nodal normal exceeds 10 degrees. Mesh refinement is recommended. The elements have been identified in element set WarnElemWarped.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FILE, {
    'phase': BATCHPRE_PHASE, 
    'file': 'C:\\Users\\chs17004\\Downloads\\Pressure_Box_With_Holes.odb', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(COMPLETED, {
    'phase': BATCHPRE_PHASE, 'message': 'Analysis phase complete', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'FFM5TW1', 'handle': 6196, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STEP, {'phase': STANDARD_PHASE, 
    'stepId': 1, 'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(MEMORY_ESTIMATE, {
    'phase': STANDARD_PHASE, 'jobName': 'Pressure_Box_With_Holes', 
    'memory': 38.0})
mdb.jobs['Pressure_Box_With_Holes']._Message(PHYSICAL_MEMORY, {
    'phase': STANDARD_PHASE, 'physical_memory': 8147.0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(MINIMUM_MEMORY, {
    'minimum_memory': 25.0, 'phase': STANDARD_PHASE, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 1, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STATUS, {'totalTime': 1.0, 
    'attempts': 1, 'timeIncrement': 1.0, 'increment': 1, 'stepTime': 1.0, 
    'step': 1, 'jobName': 'Pressure_Box_With_Holes', 'severe': 0, 
    'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Pressure_Box_With_Holes']._Message(END_STEP, {
    'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(COMPLETED, {
    'phase': STANDARD_PHASE, 'message': 'Analysis phase complete', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(JOB_COMPLETED, {
    'time': 'Tue Oct  6 12:24:54 2020', 'jobName': 'Pressure_Box_With_Holes'})
del mdb.models['Model-1'].rootAssembly.sets['m_Set-17']
mdb.models['Model-1'].rootAssembly.Set(
    faces=mdb.models['Model-1'].rootAssembly.instances['Long_Side-1'].faces.getSequenceFromMask(
    mask=('[#1 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Long_Side-2'].faces.getSequenceFromMask(
    mask=('[#1 ]', ), ), name='s_Set-2')
mdb.models['Model-1'].rootAssembly.Set(
    faces=mdb.models['Model-1'].rootAssembly.instances['Long_Side-2'].faces.getSequenceFromMask(
    mask=('[#1 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Long_Side-1'].faces.getSequenceFromMask(
    mask=('[#1 ]', ), ), name='s_Set-22')
mdb.models['Model-1'].rootAssembly.Set(
    faces=mdb.models['Model-1'].rootAssembly.instances['Short Side With Holes-1'].faces.getSequenceFromMask(
    mask=('[#1 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Short Side-1'].faces.getSequenceFromMask(
    mask=('[#1 ]', ), ), name='m_Set-22')
mdb.jobs['Pressure_Box_With_Holes'].submit(consistencyChecking=OFF)
mdb.jobs['Pressure_Box_With_Holes']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'FFM5TW1', 'handle': 0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'THE SLAVE SURFACES ASSEMBLY_Side 1 slave surface AND ASSEMBLY_S_SURF-37 INTERSECT EACH OTHER. THEY ARE PAIRED WITH MASTER SURFACES ASSEMBLY_BOTTOM_MASTER_SURFACE AND ASSEMBLY_M_SURF-37 THAT ALSO INTERSECT EACH OTHER. IF BOTH PAIRS ARE *CONTACT PAIRs, THESE TWO PAIRS SHOULD NOT BE SIMULTANEOUSLY PRESENT IN A STEP BECAUSE OF POSSIBLE CONVERGENCE PROBLEMS; USE *MODEL CHANGE,TYPE=CONTACT PAIR TO REMOVE ONE OF THEM. IF BOTH ARE *TIE PAIRS, THE REDUNDANT TIES WILL BE REMOVED AUTOMATICALLY. IF ONE PAIR IS *TIE AND ANOTHER IS *CONTACT PAIR, REMOVE ONE OF THEM.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-14_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), NOT ALL THE NODES THAT HAVE BEEN ADJUSTED WERE PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), ADJUSTED NODES WITH VERY SMALL ADJUSTMENTS WERE NOT PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-47,ASSEMBLY_M_SURF-47) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-47-ASSEMBLY_M_SURF-47), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-22_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-22_CNS_-ASSEMBLY_M_SET-22_CNS_), ADJUSTED NODES WITH VERY SMALL ADJUSTMENTS WERE NOT PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-45,ASSEMBLY_M_SURF-45) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-45-ASSEMBLY_M_SURF-45), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '33 nodes have been adjusted. The nodes have been identified in node set WarnNodeAdjust.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 4 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 4 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 33 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 3 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 33 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 3 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 65 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 15 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 65 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 15 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 16 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 16 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 65 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 65 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 13 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 13 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 33 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 33 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '342 nodes are either missing intersection with their respective master surface or are outside the adjust zone. The nodes have been identified in node set WarnNodeMissMasterIntersect.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '12 nodes are used more than once as a slave node in *TIE keyword. One of the *TIE constraints at each of these nodes have been removed. The nodes have been identified in node set WarnNodeOverconTieSlave.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '1 elements are distorted. Either the isoparametric angles are out of the suggested limits or the triangular or tetrahedral quality measure is bad. The elements have been identified in element set WarnElemDistorted.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '9 elements are curved/warped. The angle subtended between the average element normal and a nodal normal exceeds 10 degrees. Mesh refinement is recommended. The elements have been identified in element set WarnElemWarped.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FILE, {
    'phase': BATCHPRE_PHASE, 
    'file': 'C:\\Users\\chs17004\\Downloads\\Pressure_Box_With_Holes.odb', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(COMPLETED, {
    'phase': BATCHPRE_PHASE, 'message': 'Analysis phase complete', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'FFM5TW1', 'handle': 8160, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STEP, {'phase': STANDARD_PHASE, 
    'stepId': 1, 'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(MEMORY_ESTIMATE, {
    'phase': STANDARD_PHASE, 'jobName': 'Pressure_Box_With_Holes', 
    'memory': 38.0})
mdb.jobs['Pressure_Box_With_Holes']._Message(PHYSICAL_MEMORY, {
    'phase': STANDARD_PHASE, 'physical_memory': 8147.0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(MINIMUM_MEMORY, {
    'minimum_memory': 25.0, 'phase': STANDARD_PHASE, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 1, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STATUS, {'totalTime': 1.0, 
    'attempts': 1, 'timeIncrement': 1.0, 'increment': 1, 'stepTime': 1.0, 
    'step': 1, 'jobName': 'Pressure_Box_With_Holes', 'severe': 0, 
    'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Pressure_Box_With_Holes']._Message(END_STEP, {
    'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(COMPLETED, {
    'phase': STANDARD_PHASE, 'message': 'Analysis phase complete', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(JOB_COMPLETED, {
    'time': 'Tue Oct  6 12:26:50 2020', 'jobName': 'Pressure_Box_With_Holes'})
mdb.models['Model-1'].parts['Short Side'].deleteMesh()
mdb.models['Model-1'].parts['Short Side'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=0.025)
mdb.models['Model-1'].parts['Short Side'].generateMesh()
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.jobs['Pressure_Box_With_Holes'].submit(consistencyChecking=OFF)
mdb.jobs['Pressure_Box_With_Holes']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'FFM5TW1', 'handle': 0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'THE SLAVE SURFACES ASSEMBLY_Side 1 slave surface AND ASSEMBLY_S_SURF-37 INTERSECT EACH OTHER. THEY ARE PAIRED WITH MASTER SURFACES ASSEMBLY_BOTTOM_MASTER_SURFACE AND ASSEMBLY_M_SURF-37 THAT ALSO INTERSECT EACH OTHER. IF BOTH PAIRS ARE *CONTACT PAIRs, THESE TWO PAIRS SHOULD NOT BE SIMULTANEOUSLY PRESENT IN A STEP BECAUSE OF POSSIBLE CONVERGENCE PROBLEMS; USE *MODEL CHANGE,TYPE=CONTACT PAIR TO REMOVE ONE OF THEM. IF BOTH ARE *TIE PAIRS, THE REDUNDANT TIES WILL BE REMOVED AUTOMATICALLY. IF ONE PAIR IS *TIE AND ANOTHER IS *CONTACT PAIR, REMOVE ONE OF THEM.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-14_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), NOT ALL THE NODES THAT HAVE BEEN ADJUSTED WERE PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), ADJUSTED NODES WITH VERY SMALL ADJUSTMENTS WERE NOT PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-47,ASSEMBLY_M_SURF-47) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-47-ASSEMBLY_M_SURF-47), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-22_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-22_CNS_-ASSEMBLY_M_SET-22_CNS_), ADJUSTED NODES WITH VERY SMALL ADJUSTMENTS WERE NOT PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-45,ASSEMBLY_M_SURF-45) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'PLEASE MAKE SURE THAT THE MESH DENSITY OF THE SLAVE SURFACE IN THE TIE PAIR (ASSEMBLY_S_SURF-45,ASSEMBLY_M_SURF-45) IS FINER THAN THE MASTER SURFACE.  THE ANALYSIS MAY RUN SLOWER, MAY YIELD INACCURATE RESULTS, AND MAY REQUIRE MORE MEMORY IF THIS IS NOT THE CASE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-45-ASSEMBLY_M_SURF-45), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '48 nodes have been adjusted. The nodes have been identified in node set WarnNodeAdjust.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 13 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 13 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 155 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 155 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 157 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 157 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 17 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 159 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 17 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 159 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 33 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 161 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 33 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 161 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 49 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 163 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 49 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 163 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 65 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 165 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 65 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 165 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 81 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 167 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 81 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 167 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 17 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 11 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 17 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 11 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 33 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 33 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 49 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 7 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 49 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 7 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 65 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 65 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 81 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 3 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 81 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 3 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '495 nodes are either missing intersection with their respective master surface or are outside the adjust zone. The nodes have been identified in node set WarnNodeMissMasterIntersect.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'Normal cannot be computed in 5 elements. The nodal coordinates may be incorrect or the element aspect ratio may exceed 1000 to 1. The elements have been identified in element set ErrElemNormal.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '18 nodes are used more than once as a slave node in *TIE keyword. One of the *TIE constraints at each of these nodes have been removed. The nodes have been identified in node set WarnNodeOverconTieSlave.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'The geometry of 5 elements is too distorted. Check the nodal coordinates or node numbering on elements identified in element set ErrElemDistorted.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '11 elements are distorted. Either the isoparametric angles are out of the suggested limits or the triangular or tetrahedral quality measure is bad. The elements have been identified in element set WarnElemDistorted.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'The area of 2 elements is zero, small, or negative. Check coordinates or node numbering, or modify the mesh seed. The elements have been identified in element set ErrElemAreaSmallNegZero.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'The aspect ratio for 1 elements exceeds 100 to 1. The elements have been identified in element set WarnElemAspectRatio.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '13 elements are curved/warped. The angle subtended between the average element normal and a nodal normal exceeds 10 degrees. Mesh refinement is recommended. The elements have been identified in element set WarnElemWarped.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'Error in defining normal to the element surface at a node in 5 elements. The elements have been identified in element set ErrElemShellNormal.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FILE, {
    'phase': BATCHPRE_PHASE, 
    'file': 'C:\\Users\\chs17004\\Downloads\\Pressure_Box_With_Holes.odb', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ABORTED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase failed due to errors', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ERROR, {
    'message': 'Analysis Input File Processor exited with an error.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(JOB_ABORTED, {
    'message': 'Analysis Input File Processor exited with an error.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.models['Model-1'].parts['Short Side'].deleteMesh()
mdb.models['Model-1'].parts['Short Side'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=0.05)
mdb.models['Model-1'].parts['Short Side'].generateMesh()
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.jobs['Pressure_Box_With_Holes'].submit(consistencyChecking=OFF)
mdb.jobs['Pressure_Box_With_Holes']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'FFM5TW1', 'handle': 0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'THE SLAVE SURFACES ASSEMBLY_Side 1 slave surface AND ASSEMBLY_S_SURF-37 INTERSECT EACH OTHER. THEY ARE PAIRED WITH MASTER SURFACES ASSEMBLY_BOTTOM_MASTER_SURFACE AND ASSEMBLY_M_SURF-37 THAT ALSO INTERSECT EACH OTHER. IF BOTH PAIRS ARE *CONTACT PAIRs, THESE TWO PAIRS SHOULD NOT BE SIMULTANEOUSLY PRESENT IN A STEP BECAUSE OF POSSIBLE CONVERGENCE PROBLEMS; USE *MODEL CHANGE,TYPE=CONTACT PAIR TO REMOVE ONE OF THEM. IF BOTH ARE *TIE PAIRS, THE REDUNDANT TIES WILL BE REMOVED AUTOMATICALLY. IF ONE PAIR IS *TIE AND ANOTHER IS *CONTACT PAIR, REMOVE ONE OF THEM.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-14_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), NOT ALL THE NODES THAT HAVE BEEN ADJUSTED WERE PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), ADJUSTED NODES WITH VERY SMALL ADJUSTMENTS WERE NOT PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-47,ASSEMBLY_M_SURF-47) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-47-ASSEMBLY_M_SURF-47), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-22_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-22_CNS_-ASSEMBLY_M_SET-22_CNS_), ADJUSTED NODES WITH VERY SMALL ADJUSTMENTS WERE NOT PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-45,ASSEMBLY_M_SURF-45) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-45-ASSEMBLY_M_SURF-45), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '34 nodes have been adjusted. The nodes have been identified in node set WarnNodeAdjust.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 7 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 7 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 49 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 49 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 43 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 43 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 17 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 44 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 17 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 44 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 33 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 45 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 33 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 45 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 49 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 46 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 49 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 46 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 65 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 47 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 65 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 47 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 81 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 48 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 81 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 48 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 17 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 17 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 33 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 33 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 49 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 4 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 49 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 4 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 65 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 3 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 65 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 3 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 81 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 81 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '375 nodes are either missing intersection with their respective master surface or are outside the adjust zone. The nodes have been identified in node set WarnNodeMissMasterIntersect.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '18 nodes are used more than once as a slave node in *TIE keyword. One of the *TIE constraints at each of these nodes have been removed. The nodes have been identified in node set WarnNodeOverconTieSlave.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '1 elements are distorted. Either the isoparametric angles are out of the suggested limits or the triangular or tetrahedral quality measure is bad. The elements have been identified in element set WarnElemDistorted.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '11 elements are curved/warped. The angle subtended between the average element normal and a nodal normal exceeds 10 degrees. Mesh refinement is recommended. The elements have been identified in element set WarnElemWarped.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FILE, {
    'phase': BATCHPRE_PHASE, 
    'file': 'C:\\Users\\chs17004\\Downloads\\Pressure_Box_With_Holes.odb', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(COMPLETED, {
    'phase': BATCHPRE_PHASE, 'message': 'Analysis phase complete', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'FFM5TW1', 'handle': 13652, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STEP, {'phase': STANDARD_PHASE, 
    'stepId': 1, 'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(MEMORY_ESTIMATE, {
    'phase': STANDARD_PHASE, 'jobName': 'Pressure_Box_With_Holes', 
    'memory': 39.0})
mdb.jobs['Pressure_Box_With_Holes']._Message(PHYSICAL_MEMORY, {
    'phase': STANDARD_PHASE, 'physical_memory': 8147.0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(MINIMUM_MEMORY, {
    'minimum_memory': 26.0, 'phase': STANDARD_PHASE, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 1, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STATUS, {'totalTime': 1.0, 
    'attempts': 1, 'timeIncrement': 1.0, 'increment': 1, 'stepTime': 1.0, 
    'step': 1, 'jobName': 'Pressure_Box_With_Holes', 'severe': 0, 
    'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Pressure_Box_With_Holes']._Message(END_STEP, {
    'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(COMPLETED, {
    'phase': STANDARD_PHASE, 'message': 'Analysis phase complete', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(JOB_COMPLETED, {
    'time': 'Tue Oct  6 12:29:56 2020', 'jobName': 'Pressure_Box_With_Holes'})
mdb.models['Model-1'].constraints['Bottom to Sides'].setValues(
    tieRotations=OFF)
mdb.models['Model-1'].constraints['Cap to sides'].setValues(tieRotations=OFF)
mdb.models['Model-1'].constraints['Constraint-8'].setValues(tieRotations=OFF)
mdb.models['Model-1'].constraints['Sides to sides'].setValues(tieRotations=OFF)
mdb.jobs['Pressure_Box_With_Holes'].submit(consistencyChecking=OFF)
mdb.jobs['Pressure_Box_With_Holes']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'FFM5TW1', 'handle': 0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'THE SLAVE SURFACES ASSEMBLY_Side 1 slave surface AND ASSEMBLY_S_SURF-37 INTERSECT EACH OTHER. THEY ARE PAIRED WITH MASTER SURFACES ASSEMBLY_BOTTOM_MASTER_SURFACE AND ASSEMBLY_M_SURF-37 THAT ALSO INTERSECT EACH OTHER. IF BOTH PAIRS ARE *CONTACT PAIRs, THESE TWO PAIRS SHOULD NOT BE SIMULTANEOUSLY PRESENT IN A STEP BECAUSE OF POSSIBLE CONVERGENCE PROBLEMS; USE *MODEL CHANGE,TYPE=CONTACT PAIR TO REMOVE ONE OF THEM. IF BOTH ARE *TIE PAIRS, THE REDUNDANT TIES WILL BE REMOVED AUTOMATICALLY. IF ONE PAIR IS *TIE AND ANOTHER IS *CONTACT PAIR, REMOVE ONE OF THEM.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-14_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), NOT ALL THE NODES THAT HAVE BEEN ADJUSTED WERE PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), ADJUSTED NODES WITH VERY SMALL ADJUSTMENTS WERE NOT PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-47,ASSEMBLY_M_SURF-47) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-47-ASSEMBLY_M_SURF-47), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-22_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-22_CNS_-ASSEMBLY_M_SET-22_CNS_), ADJUSTED NODES WITH VERY SMALL ADJUSTMENTS WERE NOT PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-45,ASSEMBLY_M_SURF-45) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-45-ASSEMBLY_M_SURF-45), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '34 nodes have been adjusted. The nodes have been identified in node set WarnNodeAdjust.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 7 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 49 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 43 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 17 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 44 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 33 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 45 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 49 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 46 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 65 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 47 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 81 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 48 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 17 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 33 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 49 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 4 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 65 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 3 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 81 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '375 nodes are either missing intersection with their respective master surface or are outside the adjust zone. The nodes have been identified in node set WarnNodeMissMasterIntersect.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '18 nodes are used more than once as a slave node in *TIE keyword. One of the *TIE constraints at each of these nodes have been removed. The nodes have been identified in node set WarnNodeOverconTieSlave.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '1 elements are distorted. Either the isoparametric angles are out of the suggested limits or the triangular or tetrahedral quality measure is bad. The elements have been identified in element set WarnElemDistorted.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '11 elements are curved/warped. The angle subtended between the average element normal and a nodal normal exceeds 10 degrees. Mesh refinement is recommended. The elements have been identified in element set WarnElemWarped.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FILE, {
    'phase': BATCHPRE_PHASE, 
    'file': 'C:\\Users\\chs17004\\Downloads\\Pressure_Box_With_Holes.odb', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(COMPLETED, {
    'phase': BATCHPRE_PHASE, 'message': 'Analysis phase complete', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'FFM5TW1', 'handle': 10408, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STEP, {'phase': STANDARD_PHASE, 
    'stepId': 1, 'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(MEMORY_ESTIMATE, {
    'phase': STANDARD_PHASE, 'jobName': 'Pressure_Box_With_Holes', 
    'memory': 40.0})
mdb.jobs['Pressure_Box_With_Holes']._Message(PHYSICAL_MEMORY, {
    'phase': STANDARD_PHASE, 'physical_memory': 8147.0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(MINIMUM_MEMORY, {
    'minimum_memory': 26.0, 'phase': STANDARD_PHASE, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 1, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STATUS, {'totalTime': 1.0, 
    'attempts': 1, 'timeIncrement': 1.0, 'increment': 1, 'stepTime': 1.0, 
    'step': 1, 'jobName': 'Pressure_Box_With_Holes', 'severe': 0, 
    'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Pressure_Box_With_Holes']._Message(END_STEP, {
    'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(COMPLETED, {
    'phase': STANDARD_PHASE, 'message': 'Analysis phase complete', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(JOB_COMPLETED, {
    'time': 'Tue Oct  6 12:47:18 2020', 'jobName': 'Pressure_Box_With_Holes'})
mdb.models['Model-1'].constraints['Bottom to Sides'].setValues(tieRotations=ON)
mdb.models['Model-1'].constraints['Cap to sides'].setValues(tieRotations=ON)
mdb.models['Model-1'].constraints['Constraint-8'].setValues(tieRotations=ON)
mdb.models['Model-1'].constraints['Sides to sides'].setValues(tieRotations=ON)
mdb.jobs['Pressure_Box_With_Holes'].submit(consistencyChecking=OFF)
mdb.jobs['Pressure_Box_With_Holes']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'FFM5TW1', 'handle': 0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'THE SLAVE SURFACES ASSEMBLY_Side 1 slave surface AND ASSEMBLY_S_SURF-37 INTERSECT EACH OTHER. THEY ARE PAIRED WITH MASTER SURFACES ASSEMBLY_BOTTOM_MASTER_SURFACE AND ASSEMBLY_M_SURF-37 THAT ALSO INTERSECT EACH OTHER. IF BOTH PAIRS ARE *CONTACT PAIRs, THESE TWO PAIRS SHOULD NOT BE SIMULTANEOUSLY PRESENT IN A STEP BECAUSE OF POSSIBLE CONVERGENCE PROBLEMS; USE *MODEL CHANGE,TYPE=CONTACT PAIR TO REMOVE ONE OF THEM. IF BOTH ARE *TIE PAIRS, THE REDUNDANT TIES WILL BE REMOVED AUTOMATICALLY. IF ONE PAIR IS *TIE AND ANOTHER IS *CONTACT PAIR, REMOVE ONE OF THEM.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-14_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), NOT ALL THE NODES THAT HAVE BEEN ADJUSTED WERE PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), ADJUSTED NODES WITH VERY SMALL ADJUSTMENTS WERE NOT PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-47,ASSEMBLY_M_SURF-47) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-47-ASSEMBLY_M_SURF-47), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-22_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-22_CNS_-ASSEMBLY_M_SET-22_CNS_), ADJUSTED NODES WITH VERY SMALL ADJUSTMENTS WERE NOT PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-45,ASSEMBLY_M_SURF-45) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-45-ASSEMBLY_M_SURF-45), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '34 nodes have been adjusted. The nodes have been identified in node set WarnNodeAdjust.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 7 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 7 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 49 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 49 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 43 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 43 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 17 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 44 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 17 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 44 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 33 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 45 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 33 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 45 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 49 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 46 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 49 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 46 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 65 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 47 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 65 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 47 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 81 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 48 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 81 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 48 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 17 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 17 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 33 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 33 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 49 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 4 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 49 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 4 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 65 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 3 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 65 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 3 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 81 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 81 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '375 nodes are either missing intersection with their respective master surface or are outside the adjust zone. The nodes have been identified in node set WarnNodeMissMasterIntersect.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '18 nodes are used more than once as a slave node in *TIE keyword. One of the *TIE constraints at each of these nodes have been removed. The nodes have been identified in node set WarnNodeOverconTieSlave.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '1 elements are distorted. Either the isoparametric angles are out of the suggested limits or the triangular or tetrahedral quality measure is bad. The elements have been identified in element set WarnElemDistorted.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '11 elements are curved/warped. The angle subtended between the average element normal and a nodal normal exceeds 10 degrees. Mesh refinement is recommended. The elements have been identified in element set WarnElemWarped.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FILE, {
    'phase': BATCHPRE_PHASE, 
    'file': 'C:\\Users\\chs17004\\Downloads\\Pressure_Box_With_Holes.odb', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(COMPLETED, {
    'phase': BATCHPRE_PHASE, 'message': 'Analysis phase complete', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'FFM5TW1', 'handle': 13660, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STEP, {'phase': STANDARD_PHASE, 
    'stepId': 1, 'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(MEMORY_ESTIMATE, {
    'phase': STANDARD_PHASE, 'jobName': 'Pressure_Box_With_Holes', 
    'memory': 39.0})
mdb.jobs['Pressure_Box_With_Holes']._Message(PHYSICAL_MEMORY, {
    'phase': STANDARD_PHASE, 'physical_memory': 8147.0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(MINIMUM_MEMORY, {
    'minimum_memory': 26.0, 'phase': STANDARD_PHASE, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 1, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STATUS, {'totalTime': 1.0, 
    'attempts': 1, 'timeIncrement': 1.0, 'increment': 1, 'stepTime': 1.0, 
    'step': 1, 'jobName': 'Pressure_Box_With_Holes', 'severe': 0, 
    'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Pressure_Box_With_Holes']._Message(END_STEP, {
    'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(COMPLETED, {
    'phase': STANDARD_PHASE, 'message': 'Analysis phase complete', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(JOB_COMPLETED, {
    'time': 'Tue Oct  6 12:48:30 2020', 'jobName': 'Pressure_Box_With_Holes'})
mdb.models['Model-1'].constraints['Sides to sides'].setValues(tieRotations=OFF)
mdb.models['Model-1'].constraints['Constraint-8'].setValues(tieRotations=OFF)
mdb.models['Model-1'].constraints['Cap to sides'].setValues(tieRotations=OFF)
mdb.models['Model-1'].constraints['Bottom to Sides'].setValues(
    tieRotations=OFF)
mdb.jobs['Pressure_Box_With_Holes'].submit(consistencyChecking=OFF)
mdb.jobs['Pressure_Box_With_Holes']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'FFM5TW1', 'handle': 0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'THE SLAVE SURFACES ASSEMBLY_Side 1 slave surface AND ASSEMBLY_S_SURF-37 INTERSECT EACH OTHER. THEY ARE PAIRED WITH MASTER SURFACES ASSEMBLY_BOTTOM_MASTER_SURFACE AND ASSEMBLY_M_SURF-37 THAT ALSO INTERSECT EACH OTHER. IF BOTH PAIRS ARE *CONTACT PAIRs, THESE TWO PAIRS SHOULD NOT BE SIMULTANEOUSLY PRESENT IN A STEP BECAUSE OF POSSIBLE CONVERGENCE PROBLEMS; USE *MODEL CHANGE,TYPE=CONTACT PAIR TO REMOVE ONE OF THEM. IF BOTH ARE *TIE PAIRS, THE REDUNDANT TIES WILL BE REMOVED AUTOMATICALLY. IF ONE PAIR IS *TIE AND ANOTHER IS *CONTACT PAIR, REMOVE ONE OF THEM.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-14_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), NOT ALL THE NODES THAT HAVE BEEN ADJUSTED WERE PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-14_CNS_-ASSEMBLY_BOTTOM-1_BOTTOM_PLATE_CNS_), ADJUSTED NODES WITH VERY SMALL ADJUSTMENTS WERE NOT PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-47,ASSEMBLY_M_SURF-47) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-47-ASSEMBLY_M_SURF-47), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'SLAVE SURFACE ASSEMBLY_S_SET-22_CNS_ IS A NODE-BASED SURFACE USED WITH SURFACE TO SURFACE APPROACH.  IN ORDER TO OBTAIN IMPROVED STRESS ACCURACY WITH THIS APPROACH, AN ELEMENT-BASED SURFACE SHOULD BE USED INSTEAD.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SET-22_CNS_-ASSEMBLY_M_SET-22_CNS_), ADJUSTED NODES WITH VERY SMALL ADJUSTMENTS WERE NOT PRINTED. SPECIFY *PREPRINT,MODEL=YES FOR COMPLETE PRINTOUT.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '*TIE BETWEEN SURFACE PAIR (ASSEMBLY_S_SURF-45,ASSEMBLY_M_SURF-45) IS REVERTED BACK TO TYPE NODE-TO-SURFACE. THIS CASE MAY HAPPEN IF TYPE SURFACE-TO-SURFACE CANNOT FIND NODES TO TIE TOGETHER OR IF DEFAULT ACOUSTIC-STRUCTURAL TIE IS SPECIFIED INVOLVING SHELLS. PLEASE CHECK THE SURFACE DEFINITIONS OR SPECIFY TYPE=SURFACE TO SURFACE FOR ACOUSTIC-STRUCTURAL TIE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'FOR *TIE PAIR (ASSEMBLY_S_SURF-45-ASSEMBLY_M_SURF-45), ADJUSTMENT WAS SPECIFIED BUT NO NODE WAS ADJUSTED MORE THAN THE ADJUSTMENT DISTANCE = 2.22000E-16.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '34 nodes have been adjusted. The nodes have been identified in node set WarnNodeAdjust.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 7 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE BOTTOM-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 49 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 112 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 14 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 16 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 9 INSTANCE CAP-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 97 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 1 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 43 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 1 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE CAP-1 IS REMOVED.  CHECK IF THIS IS ACCEPTABLE.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 17 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 44 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 33 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 45 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 49 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 46 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 65 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 47 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 81 INSTANCE LONG_SIDE-1 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 48 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 17 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 6 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 33 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 5 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 49 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 4 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 65 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 3 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OVERCONSTRAINT CHECKS: NODE 81 INSTANCE LONG_SIDE-2 IS USED MORE THAN ONCE AS A SLAVE NODE IN THE *TIE KEYWORD.  THE CONSTRAINT BETWEEN THIS NODE AND THE MASTER SURFACE WITH NODE 2 INSTANCE Short Side-1 IS REMOVED.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '375 nodes are either missing intersection with their respective master surface or are outside the adjust zone. The nodes have been identified in node set WarnNodeMissMasterIntersect.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '18 nodes are used more than once as a slave node in *TIE keyword. One of the *TIE constraints at each of these nodes have been removed. The nodes have been identified in node set WarnNodeOverconTieSlave.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '1 elements are distorted. Either the isoparametric angles are out of the suggested limits or the triangular or tetrahedral quality measure is bad. The elements have been identified in element set WarnElemDistorted.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '11 elements are curved/warped. The angle subtended between the average element normal and a nodal normal exceeds 10 degrees. Mesh refinement is recommended. The elements have been identified in element set WarnElemWarped.', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FILE, {
    'phase': BATCHPRE_PHASE, 
    'file': 'C:\\Users\\chs17004\\Downloads\\Pressure_Box_With_Holes.odb', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(COMPLETED, {
    'phase': BATCHPRE_PHASE, 'message': 'Analysis phase complete', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'FFM5TW1', 'handle': 9408, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STEP, {'phase': STANDARD_PHASE, 
    'stepId': 1, 'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(MEMORY_ESTIMATE, {
    'phase': STANDARD_PHASE, 'jobName': 'Pressure_Box_With_Holes', 
    'memory': 40.0})
mdb.jobs['Pressure_Box_With_Holes']._Message(PHYSICAL_MEMORY, {
    'phase': STANDARD_PHASE, 'physical_memory': 8147.0, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(MINIMUM_MEMORY, {
    'minimum_memory': 26.0, 'phase': STANDARD_PHASE, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(ODB_FRAME, {
    'phase': STANDARD_PHASE, 'step': 0, 'frame': 1, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(STATUS, {'totalTime': 1.0, 
    'attempts': 1, 'timeIncrement': 1.0, 'increment': 1, 'stepTime': 1.0, 
    'step': 1, 'jobName': 'Pressure_Box_With_Holes', 'severe': 0, 
    'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['Pressure_Box_With_Holes']._Message(END_STEP, {
    'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(COMPLETED, {
    'phase': STANDARD_PHASE, 'message': 'Analysis phase complete', 
    'jobName': 'Pressure_Box_With_Holes'})
mdb.jobs['Pressure_Box_With_Holes']._Message(JOB_COMPLETED, {
    'time': 'Tue Oct  6 12:55:57 2020', 'jobName': 'Pressure_Box_With_Holes'})
#--- End of Recover file ------
mdb.save()
#: The model database has been saved to "C:\Users\chs17004\Desktop\New folder\Pressure_Box With Holes.cae".
mdb.save()
#: The model database has been saved to "C:\Users\chs17004\Desktop\New folder\Pressure_Box With Holes.cae".
