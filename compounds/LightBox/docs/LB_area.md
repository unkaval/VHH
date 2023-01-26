### ***LB_area***
**Component Compound** - this compound is a light in the the LightBox system.<br /><br />
**Arealight** - This is a diffuse light generator that mimics the lighting from an *area* light.  It does this by taking the light direction and the mesh surface normal, performing a dot product and multiplying by the light's intensity.  The area light is made by using projections and sampling, therefore has more settings used in creating shadow information.<br /><br />
The diagnostic tab will hide and show the light rays used in the calculations.<br />
<br />

***
## Input
<span style="color:#90A3F4">***input_mesh***</span>
<br />The object you are lighting.

<span style="color:#E67373">***maya_geo_plane_matrix***</span>
<br />The world matrix for your area light.  This can be a Maya plane, or be generated within Bifrost.  This light needs SRT information.

<span style="color:#E67373">***maya_areaLight_matrix***</span>
<br />The world matrix for your area light.  This can be a Maya area light, or be generated within Bifrost.  This light needs SRT information.


<span style="color:#A8D977">***areaLight_intensity***</span>
<br />Intensity and color of the light.

<span style="color:#82D99F">***falloff_distance***</span>
<br />The distance to which the light's intensity will falloff to zero.  This is in worldspace units and is an inverse square falloff.

<span style="color:#82D99F">***areaLight_focus***</span>
<br />This controls the direction of the light rays.  A value of 0 will produce parallel rays, positive or negative numbers will change the angle of the rays.

<span style="color:#62CFD9">***areaLight_resolution***</span>
<br />This value represents the number of rays cast to calculate the area light contribution.  A higher number will deliver smoother results, at a higher cost of calculation.

<span style="color:#82D99F">***areaLight_spread***</span>
<br />This refers to how may points around the ray hit are lit.  This is highly dependent on the resolution of your mesh and the space between its points..

<span style="color:#82D99F">***area_weight***</span>
<br />This is an overall multiplier of the output.  It is a auto-port, allowing for the input of `float`, `floatArray` and `scalar_field` data.

<span style="color:#A8D977">***black_array***</span>
<br />This port is intended for use in the LightBox system.  It is an array of value {0,0,0} that the light result will be added to, can be left unconnected.


***
## Output
<span style="color:#A8D977">***area_contribution***</span>
<br />An array of values, per point, of this light's contribution to the lighting.  Add this to the `point_color` of your mesh to see the result.

