This document sumarized the scenerios explicitly tested by the test suite. New tests are always welcome

CreateODB()/ReadODB
###################
Nodes and elements: Tested in 2D and 3D under for all possible element types
EigenValues: Tested 2D for beam elements, 3D for beam elements and quad elements
Defomormation:  Tested 2D for beam elements, 3D for quad elements
Forces: Not tested.
Relevant files: model_ODB, Shell3D_OBD_Animation, SteelFrame2D_OBD_Animation

plot_model()
############
Tested for 2D and 3D under all possible element types. Tested with and without active model.
Relevant files: plot_model_2D, plot_model_3D, Shell3D_OBD_Animation

plot_modeshape()
################
Tested 2D for beam elements, 3D for beam elements and quad elements. Tested with and without active model.
relevant files: Shell3D_OBD_Animation, SteelFrame2D_OBD_Animation

plot_deformedshape()
####################
Tested in 2D for beam elements, 3D for quad elements
relevant files: Shell3D_OBD_Animation, SteelFrame2D_OBD_Animation

animate_model()
###############
Tested 2D for beam elements, 3D for beam elements and quad elements
relevant files: Shell3D_OBD_Animation, SteelFrame2D_OBD_Animation

plot_FiberResponse2D()/plot_FiberResponse2D()
#############################################
Only tested for beam elements with fibers in the local y direction.
relevant files: FibreSection2D_OBD