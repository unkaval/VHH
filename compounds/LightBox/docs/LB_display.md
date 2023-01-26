### ***LB_display***
**Component Compound** - this compound is a component in the the LightBox system.<br /><br />
**LB_display** - the end of the chain for lightbox.  This compound handles both display and output of your lighting system.  The lighting and AO information is stored on the verts, and can be output in 2 ways. There's `mesh_out` that can be sent to an `output` node, then converted to a Maya mesh as usual and exported as FBX etc.  Then there's the USD output built into the interior of the node.  This can be turned on and off on the controls, as well as setting your output file, `asset_name`, etc.<br /><br />

***
## Input
<span style="color:#90A3F4">***mesh***</span>
<br />This is the mesh you are applying lighting and ao to..

<span style="color:#90A3F4">***lighting_contributions***</span>
<br />This input port is a fan-in array, enabling you to put as many lights as you wish into it.  This is designed to take the `light_data` output objects from the LightBox lighting nodes, and will not work with float3 arrays.

<span style="color:#82D99F">***AO_contribution***</span>
<br />This input port is designed to take your single-float-array ambient occlusion information.  This comes from the `LB_AO` compound.

<span style="color:#E69963">***enable_lighting***</span>
<br />Switches the lighting display on and off.

<span style="color:#E69963">***enable_ao***</span>
<br />Switches the ambient occlusion on and off.

<span style="color:#62CFD9">***median_blur_iterations***</span>
<br />Because LightBox is designed to work with low-poly meshes, sometimes the lighting information can look ... sharp.  This is a blurring system that will average the lighting and ambient occlusion data across the mesh to provide a better looking result.  The blur is applied to both display and output streams. 

<span style="color:#D9BE6C">***asset_name***</span>
<br />This is the name of the asset in the USD hierarchy.  This is placed under a USD prim called `lightbox_obj`.  Currently, the system only works for single assets at a time.

<span style="color:#E69963">***enable_USD_save***</span>
<br />When this is enabled, the USD file will be written to disk.

<span style="color:#D9BE6C">***USD_output***</span>
<br />The file and path of the USD output file, can be usda, usdc and usd formats.


***
## Output
<span style="color:#90A3F4">***mesh_out***</span>
<br />The output mesh with the lighting and ambient occlusion written to the verticies.  This will not display this information, the diagnostic tab on the compound is used for that.  When this is connected to an output, you will be able to right-click and `create_maya_mesh`. 

