### ***petrify***
Petrify is a displacement-based stone surface generator.  It makes rocks of various detail levels. It uses 2 cellular displacements and as many detail fields as you would like to use to make something more rocky.  It's not Rockify 2, works in a different way.<br />
***
## Input
<span style="color:#90A3F4">***input_mesh***</span>
<br />The compound takes a mesh in and applies displacements to it - to make it look rocky - this is that mesh.

<span style="color:#CCB699">***detail_fields***</span>
<br />This is a fan-in array port for the detail fields (more on that later).

<span style="color:#CCB699">***mask_fields***</span>
<br />This is a fan-in array port for the mask fields (more on that later too).

<span style="color:#62CFD9">***seed***</span>
<br />The master seed, this will change the enire rock.

<span style="color:#82D99F">***master_scale***</span>
<br />This is the master displacement scale, it controls all the displacements.

<font size =4><br />***mesh setup***</font>

<span style="color:#E69963">***flatten_object_base***</span>
<br />So if you wanted to make a boulder and flatten the base of it, this is where you'd do it.  Would not recommend doing this for a plane.

<span style="color:#CCB699">***base_flatten_Curve***</span>
<br />If you are flattening the butt, here's the curve you use to shape it.

<span style="color:#82D99F">***mesh_offset_y***</span>
<br />Move that mesh up and down some.

<font size =4><br />***displacements***</font>
<br />Here is the main displacement control.  The two cellular displacements are done within the compound, while the detail fields are an input of their own.  This allows you to get as funky with your displacements as you like.

<span style="color:#E69963">***enable_primary***</span>
<br />Enable the Primary Displacement.

<span style="color:#E69963">***enable_secondary***</span>
<br />Enable the Secondary Displacement.

<span style="color:#E69963">***enable_details***</span>
<br />Enable the Details Displacement.

<font size =3><br />***cellular primary***</font><br />
<span style="color:#82D99F">***primary_cellular_weight***</span>
<br />The weight of the primary cellular displacement. 0 = all secondary, 1 = all primary.<br />
<span style="color:#82D99F">***primary_magnitude***</span>
<br />How big the primary displacement is.<br />
<span style="color:#62CFD9">***primary_frequency***</span>
<br />What frequency the primary displacement is.<br />
<span style="color:#62CFD9">***primary_F_point***</span>
<br />The "F point" is the *nth* closest point to the feature point, a classic Worley woudl be 0 (the closest point).<br />
<span style="color:#62CFD9">***scatter_shape_P***</span>
<br />This controls where the interior points are scattered; *axis bounds* scatters on the axis aligned bounding box, *object bounds* scatters on the object-aligned bounding box, *spherical bounds* scatters on the bounding sphere, and *on the object* scatters directly on the mesh.<br />
<span style="color:#E69963">***mode_P***</span>
<br />Cellular noise requires "feature points" to calculate the shapes, those points need to be scattered.  There's an internal ***scatter_points*** compound here and this controls how those points are scattered.<br />
<span style="color:#62CFD9">***distance_metric_P***</span>
<br />Euclidian, Manhattan or Chebyshev distances.<br />
<span style="color:#CCB699">***adjust_shape_P***</span>
<br />If the *distance_metric_P* is set to euclidian, this allows you to adjust the shape.<br />
<span style="color:#E69963">***smooth_primary***</span>
<br />Applies a smoothing to the primary displacement.<br />
<span style="color:#62CFD9">***primary_smooth***</span>
<br />Primary Displacement smoothing iterations.<br />
<font size =3><br />***cellular secondary***</font><br />
<span style="color:#82D99F">***secondary_magnitude***</span>
<br />How big the secondary displacement is.<br />
<span style="color:#62CFD9">***secondary_frequency***</span>
<br />What frequency the secondary displacement is<br />
<span style="color:#62CFD9">***secondary_F_point***</span>
<br />The "F point" is the *nth* closest point to the feature point, a classic Worley woudl be 0 (the closest point).<br />
<span style="color:#62CFD9">***scatter_shape_S***</span>
<br />This controls where the interior points are scattered; *axis bounds* scatters on the axis aligned bounding box, *object bounds* scatters on the object-aligned bounding box, *spherical bounds* scatters on the bounding sphere, and *on the object* scatters directly on the mesh.<br />
<span style="color:#E69963">***mode_S***</span>
<br />Cellular noise requires "feature points" to calculate the shapes, those points need to be scattered.  There's an internal ***scatter_points*** compound here and this controls how those points are scattered.<br />
<span style="color:#62CFD9">***distance_metric_S***</span>
<br />Euclidian, Manhattan or Chebyshev distances.<br />
<span style="color:#CCB699">***adjust_shape_S***</span>
<br />If the *distance_metric_P* is set to euclidian, this allows you to adjust the shape.<br />
<span style="color:#E69963">***smooth_secondary***</span>
<br />Applies a smoothing to the swcondary displacement.<br />
<span style="color:#62CFD9">***secondary_smooth***</span>
<br />Secondary Displacement smoothing iterations.<br />
<font size =3><br />***details***</font><br />
<span style="color:#82D99F">***detail_weight_per_field***</span>
<br />This *interpreted auto port* allows you to set a field weight per field.<br />
<span style="color:#82D99F">***details_strength***</span>
<br />How strong the details displacement is.<br />

<font size =4><br />***masking***</font>

<span style="color:#E69963">***use_voronoi_mask***</span>
<br />Useful for adding details quickly, this masks the displacement by a voronoi scatter.

<span style="color:#82D99F">***voronoi_strength***</span>
<br />How strong the voronoi mask is.

<span style="color:#62CFD9">***voronoi_scatter***</span>
<br />The scatter method for the voronoi points.

<span style="color:#62CFD9">***voronoi_frequency***</span>
<br />The frequency of the voronoi points.

<span style="color:#E69963">***invert_voronoi***</span>
<br />Invert the mask.

<span style="color:#E69963">***invert_field_mask***</span>
<br />If there are field masks connected, this will invert them.

<span style="color:#A8D977">***adjust_field_mask***</span>
<br />A curve to adjust the masking fields.

<font size =4><br />***post smoothing***</font>

<span style="color:#E69963">***smooth_output***</span>
<br />When checked, this smooths the entire displacement.

<span style="color:#62CFD9">***smooth***</span>
<br />How many smoothing iterations are performed.

<span style="color:#82D99F">***smooth_weights***</span>
<br />This *interpreted auto port* allows you to smooth based on point weights.

<span style="color:#E69963">***weighted_average***</span>
<br />When this is checked the mesh smoothing is based on a weighted average.

<span style="color:#E69963">***preserve_detail***</span>
<br />When checked, this attempts to preserve the smaller details of the displacement.

<span style="color:#E69963">***invert_weights***</span>
<br />Flips the weights of the smooth.

<font size =4><br />***display settings***</font>

<span style="color:#E69963">***show_field_mask***</span>
<br />When checked, this will display the mask on the mesh.

<span style="color:#E69963">***show_feature_points_P***</span>
<br />Display the feature points used to generate the Primary Displacement.

<span style="color:#E69963">***show_feature_points_S***</span>
<br />Display the feature points used to generate the Secondary Displacement.

<span style="color:#A8D977">***secondary_point_color***</span>
<br />The color of the Primary displacement points.

<span style="color:#A8D977">***primary_point_color***</span>
<br />The color of the Secondary displacement points.

***
## Output
<span style="color:#90A3F4">***petrified***</span>
<br />The displaced mesh.

