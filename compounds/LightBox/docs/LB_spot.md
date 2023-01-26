### ***LB_spot***
**Component Compound** - this compound is a light in the the LightBox system.<br /><br />
**Spotlight** - This is a diffuse light generator that mimics the lighting from a *spot* light.  It does this by taking the light direction and the mesh surface normal, performing a dot product and multiplying by the light's intensity.  Then applying shadow and penumbra information .<br /><br />
The diagnostic tab will hide and show the shadow rays to the light.  The proxy tab will show and hide the light's icon.<br />

***
## Input
<span style="color:#90A3F4">***input_mesh***</span>
<br />The object you are lighting.

<span style="color:#90A3F4">***accelerator***</span>
<br />You need to construct a raycast accelerator from the mesh to plug in here.

<span style="color:#A8D977">***spotLight_intensity***</span>
<br />Intensity and color of the spot light.

<span style="color:#A8D977">***spotLight_position***</span>
<br />The position in space opf the spotlight.

<span style="color:#A8D977">***spotLight_direction***</span>
<br />The direction the spotlight is pointing.

<span style="color:#82D99F">***spotLight_cone_angle***</span>
<br />The spotlight's cone angle, this can be entered, or brought in from Maya.

<span style="color:#82D99F">***penumbra_response***</span>
<br />How narrow or wide the penumbra of the spotlight is.  

<span style="color:#82D99F">***falloff_distance***</span>
<br />The distance to which the light's intensity will falloff to zero.  This is in worldspace units and is an inverse square falloff.

<span style="color:#82D99F">***spotLight_weight***</span>
<br />This is an overall multiplier of the output.  It is a auto-port, allowing for the input of `float`, `floatArray` and `scalar_field` data.

<span style="color:#A8D977">***black_array***</span>
<br />This port is intended for use in the LightBox system.  It is an array of value {0,0,0} that the light result will be added to, can be left unconnected.

***
## Output
<span style="color:#A8D977">***spot_contribution***</span>
<br />An array of values, per point, of this light's contribution to the lighting.  Add this to the `point_color` of your mesh to see the result.

<span style="color:#90A3F4">***light_data***</span>
<br />The light data output as an object.  This is intended for use with `LB_display`
