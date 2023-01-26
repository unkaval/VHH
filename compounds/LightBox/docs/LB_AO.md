### ***LB_AO***
**Component Compound** - this compound is a component in the the LightBox system.<br /><br />
**LB_AO** - This is a compound that generates an ambient occlusion value to be multiplied onto the lighting information.  As this is calculated by multiple raycasts **per point**, the more points you have in your mesh, or the higher the `resolution` setting, the slower this will go.  It's as fast as I can make it, for now, and it can be set to only compute on a single frame, so this can help.<br /><br />

***
## Input
<span style="color:#90A3F4">***mesh_in***</span>
<br />The mesh to calculcate the AO upon.

<span style="color:#E69963">***compute_on_frame***</span>
<br />When this is checked, the AO will only be calculated only on the `frame` selected below, any other frame will be the cached data from that frame and therefore much faster.

<span style="color:#62CFD9">***frame***</span>
<br />The frame to calculate the AO on.

<span style="color:#82D99F">***resolution***</span>
<br />The resolution of the ao is the number of rays shot from each point to find closest geo.  The more of these you have, the slower it runs.

<span style="color:#82D99F">***brightness***</span>
<br />When those rays hit something the `point_color`, which starts as white, has a very small number subtracted from it, making it darker.  This is that number.

<span style="color:#82D99F">***maximum_radius***</span>
<br />This correspond to the length of the ray, The bigger this radius, the further out for a "hit" the ray reached.

<span style="color:#82D99F">***minimum_radius***</span>
<br />Since these rays are looking for hits on the object that is casting them, this number guarantees that the ray doesn't register it's own starting point as a hit, and turn the object totally black.

<span style="color:#E69963">***infinite_radius***</span>
<br />When this is on, the rays will keep going until they hit something.

<span style="color:#E69963">***normalize***</span>
<br />Scale the output AO values to a 0-1 range

<span style="color:#CCB699">***adjust_normalized_AO***</span>
<br />When normalized, you can adjust the AO with this curve.

***
## Output
<span style="color:#82D99F">***AO contribution***</span>
<br />The AO contribution to be multiplied with your total light contribution in `LB_display`.