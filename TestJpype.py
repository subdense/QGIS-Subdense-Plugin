import jpype
import jpype.imports
from jpype.types import *

# Check if JVM is already started
#if not jpype.isJVMStarted():
#    jpype.startJVM()  # Adjust with the correct arguments if needed
#
#jpype.addClassPath("/home/MNdim/.local/share/QGIS/QGIS3/profiles/default/python/plugins/matching_plugin/jars/geoxygene-matching-1.10-SNAPSHOT.jar")

jpype.startJVM(jpype.getDefaultJVMPath(), "-Djava.class.path=/home/MNdim/.local/share/QGIS/QGIS3/profiles/default/python/plugins/matching_plugin/jars/geoxygene-matching-1.10-SNAPSHOT.jar")

import java.lang

# Now you can import your Java classes
from fr.ign.cogit.geoxygene.contrib.appariement.surfaces import ParametresAppSurfaces, AppariementSurfaces
from fr.ign.cogit.geoxygene.util.conversion import ShapefileReader, ShapefileWriter
