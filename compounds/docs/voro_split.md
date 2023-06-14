### ***voro_split***
This compound splits a mesh based on a voronoi pattern.  Note.  This does not split faces, it breaks up the mesh according it's existing structure.  This means that the final result is heavily dependent on the mesh resolution.  If you want a higher resolution mesh I would recoomend converting to volume and back, this compound works fast.<br />

***
## Input
<span style="color:#90A3F4">***incoming_mesh***</span>
<br />The Mesh you want to split.

<span style="color:#A8D977">***input_points***</span>
<br />Custom points to control the voronoi result.  Anything plugged into this port will override the settings below.

<span style="color:#E69963">***triangulate_mesh***</span>
<br />Perform a triangulation on the mesh before splitting.

<span style="color:#62CFD9">***number_of_tiles***</span>
<br />When `input_points` is empty, this is the number of tiles you wish to have in your result.

<span style="color:#62CFD9">***tile_seed***</span>
<br />Random seed for the point scattering.

<span style="color:#E69963">***scatter_mode***</span>
<br />Random or Bluenoise scattering.

***
## Output
<span style="color:#90A3F4">***output_mesh_array***</span>
<br />An array of meshes after the split.  Each tile is broken away from the original mesh and added to the output array.

