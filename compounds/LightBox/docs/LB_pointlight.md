### ***LB_pointlight***
**Component Compound** - this compound is a light in the the LightBox system.<br /><br />
**Pointlight** - This is a diffuse light generator that mimics the lighting from a *point* light.  It does this by taking the direction from each point to the light and the mesh surface normal, performing a dot product and multiplying by the light's intensity.  Then applying shadow information.<br /><br />
The diagnostic tab will hide and show the shadow rays to the light.<br />

***
## Input
<span style="color:#90A3F4">***input_mesh***</span>
<br />The object you are lighting.

<span style="color:#90A3F4">***accelerator***</span>
<br />You need to construct a raycast accelerator from the mesh to plug in here.

<span style="color:#A8D977">***pointLight_position***</span>
<br />The position of the point light in world space.

<span style="color:#A8D977">***pointLight_intensity***</span>
<br />Intensity and color of the point light.

<span style="color:#82D99F">***pointLight_falloff_distance***</span>
<br />The distance to which the light's intensity will falloff to zero.  This is in worldspace units and is an inverse square falloff.

<span style="color:#82D99F">***pointLight_weight***</span>
<br />This is an overall multiplier of the output.  It is a auto-port, allowing for the input of `float`, `floatArray` and `scalar_field` data.

<span style="color:#A8D977">***black_array***</span>
<br />This port is intended for use in the LightBox system.  It is an array of value {0,0,0} that the light result will be added to, can be left unconnected.

***
## Output
<span style="color:#82D99F">***point_contribution***</span>
<br />An array of values, per point, of this light's contribution to the lighting.  Add this to the `point_color` of your mesh to see the result.

<span style="color:#90A3F4">***light_data***</span>
<br />The light data output as an object.  This is intended for use with `LB_display`.

