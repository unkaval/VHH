### ***scatter_plus***
Scatter+ is an attempt to extend scatter functionality.  It implements 3 more scatter types, introduces the concept of filtering and includes clustering, automatic point id by color and value, filter and culling by weight.  Unlike *scatter_points* the weights are visible and the schema is black = zero weight, white = full weights.  When the diagnostic tab is on, the points will be displayed with their weights as a color.  The points can be culled inside Scatter+ or externally based on the *point_weights* property on the output points. <br />

***
## Input
<span style="color:#90A3F4">***mesh_to_scatter_on***</span>
<br />The input mesh you are going to scatter points on.

<span style="color:#90A3F4">***excluding_strands***</span>
<br />This port is where you would plug in any meshes you wanted to use as a scatter mask.

<span style="color:#90A3F4">***excluding_meshes***</span>
<br />This port is where you would plug in any strands you wanted to use as a scatter mask..

<span style="color:#90A3F4">***weight_filter***</span>
<br />This port is the input for the pre-made filters.  These are accessed through the "create value node" menu item - if you right-click this port, you will be able to access these.

<span style="color:#82D99F">***custom_weights***</span>
<br />This is an interpreted auto port - which means that you can plug any float data into it.  Scalar fields, single float, float arrays etc.

<span style="color:#E69963">***orient_to_geo***</span>
<br />When checked, this will orient the points to the underlying geometry.

<span style="color:#CCB699">***adjust_weights***</span>
<br />An fCurve that will adjust all of the weights.

<span style="color:#E69963">***blur_weights***</span>
<br />When this is checked, you are able to apply a gaussian blur to the weights.  This will slow the system down if *rebuild_scatter* is checked.

<span style="color:#82D99F">***blur_amount***</span>
<br />The amount of blur to apply to the weights.

<span style="color:#D9BE6C">***transfer_properties***</span>
<br />These are properties that you wish to transfer from the scatter mesh to the points.

### ***Scatter Settings***

<span style="color:#E69963">***rebuild_scatter***</span>
<br />When this is checked, the scatter will no longer update.  This speeds up the system but if any changes are made to the scatter or weights they will not be reflected or built until this is checked again.  This is included to speed up culling. 

<span style="color:#62CFD9">***which_scatter***</span>
<br />Choose which scatter to use:
- points per face
    - Points per face randomly places *number_of_points_per_face* points inside a triangle face.  If your mesh is not triangulated, it will be converted internally and the scatter applied.  This will mean for a quad mesh, you will have twice the number of points.

- scatter points
    - This is the Bifrost default scatter we all know and love.

- incircle packing
    - Uses the incircle and inradius of each triangulated face to place and size a point.  If your mesh is not triangulated, it will be converted internally and the scatter applied.  This will mean for a quad mesh, you will have twice the number of points.

- grid scatter
    - Very similar to Unreal's PCG scatter system. A grid is created and projected onto the mesh.  This only works well with planes/terrain.

<span style="color:#82D99F">***point_size***</span>
<br />The point size for *points_per_face* and *scatter_points*.

<span style="color:#62CFD9">***seed***</span>
<br />The random seed.

#### ***Points per face***

<span style="color:#62CFD9">***number_of_points_per_face***</span>
<br />How many points per triangle to scatter.

#### ***Scatter points***

<span style="color:#62CFD9">***scatter_mode***</span>
<br />The mode to use for scattering:  Random gives a uniform pseudo-random distribution. This is the closest to truly random, but exhibits clumps and bare patches that may be unwanted for some purposes.  BlueNoise gives a "blue noise" distribution. This is also referred to as a "quasi-random" or "low discrepancy" distribution. It provides a more even distribution, with points more equally spaced.  BlueNoiseMaximal gives a similar distribution to BlueNoise. This gives the most evenly-spaced distribution, but is the slowest to compute..

<span style="color:#62CFD9">***amount_mode***</span>
<br />Controls the interpretation of the amount parameter:  Radius generates locations that are spaced at least 2 × amount units apart. If spheres with this radius are placed on the resulting points, none of the spheres would intersect. Points may be further apart, but never closer than twice this radius.
number generates the amount number of locations.  Density generates amount locations per unit of surface area, strand length, or volume..

<span style="color:#82D99F">***amount***</span>
<br />Number of points to scatter.

#### ***Incircle packing***

<span style="color:#82D99F">***size_mult_incircle***</span>
<br />Enables scaling of the triangle's incircle, which sets the size of the points.

#### ***Grid scatter***

<span style="color:#82D99F">***grid_segments***</span>
<br />Controls the number of segments of the grid - higher numbers result in more points.

<span style="color:#82D99F">***master_scale_grid***</span>
<br />Master point size scale of the grid points.

<span style="color:#82D99F">***randomize***</span>
<br />This is a zero to one control that randomizes the positions and scale of the grid points.  Zero is no randomization, One is full randomization.

### ***Culling Settings***

<span style="color:#82D99F">***cull_below***</span>
<br />Cull any weights below this value.

<span style="color:#82D99F">***cull_above***</span>
<br />Cull any weights above this value.

<span style="color:#E69963">***cull_overlapping_points***</span>
<br />Removes points that are closer than 2 x *overlapping_radius* units to other points.

<span style="color:#82D99F">***overlapping_radius***</span>
<br />Controls the distance between points when cull_overlapping is enabled.

### ***Point ID Settings***

<span style="color:#E69963">***use_point_id***</span>
<br />A point_id property is generated from the input mesh or an image absed on the value or hue of the data.  If this is checked, the point id system will be active.

<span style="color:#D9BE6C">***point_id_property***</span>
<br />The property to write to the points.

<span style="color:#62CFD9">***sample_attribute***</span>
<br />Whether to sample the hue or value of the incoming data.

<span style="color:#62CFD9">***tolerance***</span>
<br />How tightly the data is matched to a point_id.

<span style="color:#62CFD9">***unique_instances***</span>
<br />How many unique instances will be used with the *point_id* property.

<span style="color:#E69963">***use_image***</span>
<br />Read an image from disk to provide the point_id data.

<span style="color:#D9BE6C">***filepath***</span>
<br />Path to the file on disk.

<span style="color:#D9BE6C">***vector_property_to_sample***</span>
<br />Which vector property on the mesh to generate point ids from.

### ***Clumping Settings***

<span style="color:#E69963">***clumping***</span>
<br />Clumping uses the scatter points and adds a clump (secondary scatter) around them.  This means that if you have scattered 2 million points, you're in for a rouhg time.  This works best with a lesser number of points.

<span style="color:#E69963">***show_clumping_id***</span>
<br />When each clump is scattered, it is given an id which is added to the output points as a property.  This allows more control later on and this control will assign a random color to each clump

<span style="color:#E69963">***use_bluedisc***</span>
<br />This scatters points on a disc around the input points using bluenoise.  It adds a more regular looking clump.

<span style="color:#E69963">***show_radius***</span>
<br />The clumping system allows for culling outside a radius and inside an inner radius.  This will display the radii.

<span style="color:#62CFD9">***clumping_seed***</span>
<br />Random seed for clumping.

<span style="color:#62CFD9">***points_per_clump***</span>
<br />How many points per clump.

<span style="color:#82D99F">***points_per_clump_random***</span>
<br />Amount of randomization in the clump point counts, per clump.

<span style="color:#82D99F">***radius_per_clump***</span>
<br />The radius per clump.

<span style="color:#82D99F">***radius_per_clump_random***</span>
<br />Amount of randomization in the clump radii, per clump.

<span style="color:#82D99F">***interior_radius***</span>
<br />The interior radius inside which points will be culled.

<span style="color:#62CFD9">***Clump_interpolation***</span>
<br />The clumps can be interpolated from the center to the edge to give different looks.

<span style="color:#82D99F">***exponent***</span>
<br />Exponent for the exponent interpolation.

<span style="color:#82D99F">***mean***</span>
<br />Mean for Gaussian A and Gaussian B interpoltion.

<span style="color:#82D99F">***standard_deviation***</span>
<br />SD for Gaussian A and Gaussian B interpoltion.

<span style="color:#82D99F">***exclude_by_strands_radius***</span>
<br />When excluding points with a strand, this controls the radius outwards from the strand to cull.

***
## Output
<span style="color:#90A3F4">***points_output***</span>
<br />The final points output.  Includes all properties.

<span style="color:#62CFD9">***point_id_override***</span>
<br />The point_id output as a separate data stream.  This can be plugged into an instance node.
