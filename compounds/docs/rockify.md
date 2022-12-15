### ***rockify***
Using noise and displacement, turn anything into a rock, or at least a stony-looking blob.<br /><br />[<span style="color:#CCB699">**rockify workflow**</span>](https://youtu.be/rqklfVhOtvA) 

***
## Input
<span style="color:#90A3F4">***input_mesh***</span>
<br />The mesh you wish to rockify.

***
***Subdivide Input***<br />
This uses `sqrt3_subdivide_mesh` internally to subdivide your input mesh.  Be warned here, the more subdivisions you create, the slower the whole system becomes.

<span style="color:#E69963">***subdivide_input_mesh***</span>
<br />Check this to subdivide the mesh based on the settings below.

<span style="color:#82D99F">***detail_size***</span>
<br />The resolution of the subdivision, smaller numbers = more subdivisions.

<span style="color:#82D99F">***detail_size_scale***</span>
<br />A scalaing factor on the detail size.

<span style="color:#E69963">***resolution_mode***</span>
<br />`sqrt3_subdivide_mesh` uses a volume to guide the subdivision, this is the resolution mode of that volume.

<span style="color:#E69963">***volume_adaptivity***</span>
<br />Methods to apply adaptivity to the volume, `Optimize` and `Off` are the only active choices.

<span style="color:#E69963">***mesh_adaptivity***</span>
<br />Methods to apply adaptivity to the resulting mesh, `Automatic` and `Off` are the only active choices.

***
***Smooth By Volume***<br />
Displacements are well known for tearing up your meshes.  If you need to tear up your mesh and still wish to render it, this is the setting for you - this will convert everything to a volume and then back to a mesh.  It will also apply a generated UV map using the `mapUV_auto_six` compound.  This can and will slow you down basd on the settings below.

<span style="color:#E69963">***smooth_by_volume***</span>
<br />When checked, this will smooth the mesh by volume.

<span style="color:#82D99F">***volume_smooth_detail_size***</span>
<br />The detail size of the `convert_to_volume`.

<span style="color:#82D99F">***volume_smooth_erode***</span>
<br />Apply erosion to the mesh, positive values will grow, negative will shrink the mesh.

<span style="color:#82D99F">***volume_smooth_detail_size_scale***</span>
<br />This will scale the detail on the mesh.

<span style="color:#82D99F">***volume_smoothing***</span>
<br />How smooth the resulting mesh is.

***
***Random Generation***<br />
There are 4 different noises and 1 field displacing this mesh, these are the controls for those.

<span style="color:#62CFD9">***master_seed***</span>
<br />Seed for the first worley noise.

<span style="color:#62CFD9">***minor_seed_crease***</span>
<br />Seed for the second worley noise.

<span style="color:#62CFD9">***minor_seed_fractal***</span>
<br />Seed for the detail noises.

<span style="color:#82D99F">***primary_mag***</span>
<br />Magnitude of the first worley noise.

<span style="color:#62CFD9">***primary_freq***</span>
<br />Frequency of the first worley noise.

<span style="color:#82D99F">***secondary_mag***</span>
<br />Magnitude of the second worley noise.

<span style="color:#62CFD9">***secondary_freq***</span>
<br />Frequency of the second worley noise.

<span style="color:#82D99F">***detail_strength***</span>
<br />Overall strength of the detail noise.

<span style="color:#82D99F">***detail_freq_1***</span>
<br />Frequency of the first detail noise.

<span style="color:#82D99F">***detail_freq_2***</span>
<br />Frequency of the second detail noise..

***
***Smooth***<br />
This applies a median blur across the most "pinched" of the first worley noise.  This helps to avoid tearing without losing too much detail.

<span style="color:#62CFD9">***blur***</span>
<br />The number iterations of the median blur.

***
***Field Detail***<br />
The final displacement.  This uses a scalar field to add smaller and more random details on the surface, by controlling the weights of this displacement.  If you plug in your own scalar field, this will override the field inside the compound.

<span style="color:#CCB699">***detail_field***</span>
<br />Plug for the input of a custom field.

<span style="color:#E69963">***disable_detail_field***</span>
<br />Completely turns off the detail field.

<span style="color:#82D99F">***detail_scale***</span>
<br />Scale the hight on the surface of the smaller details.

<span style="color:#82D99F">***normal_to_detail_ratio***</span>
<br />The field is applied to the mesh using a combination of the `point_normals` and the detail field.  This controls how much of each is applied. 0 is full normals, 1 is full field.

<span style="color:#A8D977">***detail_up_axis***</span>
<br />The direction of the details, this can be changed to achieve different looks.

<span style="color:#E69963">***invert_detail_up_axis***</span>
<br />Reverse the direction of the details.

<span style="color:#82D99F">***detail_frequency***</span>
<br />Frequency of the detail field.

<span style="color:#82D99F">***detail_magnitude***</span>
<br />Magnitude of the detail field.

<span style="color:#82D99F">***detail_mask_frequency***</span>
<br />Frequency of the detail mask field.

<span style="color:#82D99F">***detail_mask_magnitude***</span>
<br />Magnitude of the detail mask field.

***
***Flatten Base***<br />
Rocks usually sit on a surface (if they're not asteroids).  This will flatten the base of the rock.

<span style="color:#E69963">***flatten_base***</span>
<br />Flattens the base of the rock.

<span style="color:#A8D977">***base_flatten_curve***</span>
<br />fCurve to control the flattening of the base.

***
***Generate UVs***<br />
<span style="color:#E69963">***generate_uvs***</span>
<br />Utilises `mapUV_auto_six` internally to generate a set of very basic UVs.  It makes a 6-axis projection (auto-map) and lays it out automatically.  It's designed to give an artist a good start on UV layout, not a final output.  See the info on the node for more details.

***
## Output
<span style="color:#90A3F4">***output_mesh***</span>
<br />Your new blob that looks a bit like a rock.

