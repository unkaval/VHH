### ***points_in_a_sphere***
This is basically a "sphrand" compound, with various controls.  It uses **math** to generate points in a sphere uniformly, then gives you some options for rearranging them to your liking.<br />

***
## Input
<span style="color:#62CFD9">***how_many_points***</span>
<br />Number of points you wish to scatter.

<span style="color:#82D99F">***radius***</span>
<br />The radius of the sphere.

<span style="color:#A8D977">***offset***</span>
<br />the center of the sphere.

<span style="color:#62CFD9">***seed***</span>
<br />Seed for the random number generator.

<span style="color:#62CFD9">***interpolation***</span>
<br />The interpolation of the final points (combo port);
* Off - no interpolation.
* Ease in - center points are closer, outer points are spread out.
* Ease out - center points are spread out, outer points are closer.
* Smoothstep - smoothly interpolates between center and outer points.
* Exponent - raises the positions to an exponent, to varying effect.

<span style="color:#82D99F">***exponent***</span>
<br />When interpolation is set to exponent, this is the exponent it is raised to.

***
## Output
<span style="color:#62CFD9">***size***</span>
<br />The number of points you have scattered, this can be used in a variety of ways.

<span style="color:#A8D977">***positions***</span>
<br />The output positions of the scatter.

<span style="color:#A8D977">***normals***</span>
<br />Generated normals of the points.  The point outwards from the center.

