### ***voronoise***
Generates a voronoi pattern based on the surface points on an object by generating a random scattering of feature points and calculating the voronoi diagram.<br />

***
## Input
<span style="color:#90A3F4">***geo_in***</span>
<br />The input object, the fineness of detail in the resulting output depends on the number of points in this geo.

<span style="color:#A8D977">***control_points_input***</span>
<br />An array of positions, allowing you to input your own control points.  If this array is empty, the compound will generate points for you based on the settings in the `noise` settings.

<span style="color:#E69963">***scatter_mode***</span>
<br />What kind of scatter to perform.
* Random gives a uniform pseudo-random distribution. This is the closest to truly random, but exhibits clumps and bare patches that may be unwanted for some purposes.
* BlueNoise gives a "blue noise" distribution. This is also referred to as a "quasi-random" or "low discrepancy" distribution. It provides a more even distribution, with points more equally spaced.
* BlueNoiseMaximal gives a similar distribution to BlueNoise. This gives the most evenly-spaced distribution, but is the slowest to compute.

<span style="color:#62CFD9">***frequency***</span>
<br />How many random points to scatter on the object.

<span style="color:#62CFD9">***seed***</span>
<br />The seed for the random number generator.

<span style="color:#E69963">***normalize_diagnostic***</span>
<br />The output of the `voronoise` is distances to the first and second scattered point, this will normalize those distances to a 0-1 range.

<span style="color:#E69963">***color_diagnostic***</span>
<br />A random color array applied to the voronoi cells.

***
## Output
<span style="color:#90A3F4">***out_geometry***</span>
<br />This is a pass-through node, your geometry is unchanged.

<span style="color:#82D99F">***out_first_distance***</span>
<br />The distance to the closest voronoi point (the distance within each cell).

<span style="color:#82D99F">***out_second_distance***</span>
<br />The distance to the next closest voronoi point (the distance to the next cell).

