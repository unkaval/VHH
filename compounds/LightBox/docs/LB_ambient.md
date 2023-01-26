### ***LB_ambient***
**Component Compound** - this compound is a light in the the LightBox system.<br /><br />
**Ambientlight** - This is a diffuse light generator that mimics the lighting from an *ambient* light.  It does this by applying a flat colour to the entire mesh.<br /><br />

***
## Input
<span style="color:#90A3F4">***input_mesh***</span>
<br />The object you are lighting.

<span style="color:#A8D977">***ambient_intensity***</span>
<br />Intensity and color of the light.

<span style="color:#82D99F">***ambient_weight***</span>
<br />This is an overall multiplier of the output.  It is a auto-port, allowing for the input of `float`, `floatArray` and `scalar_field` data.

***
## Output
<span style="color:#A8D977">***ambient_contribution***</span>
<br />An array of values, per point, of this light's contribution to the lighting.  Add this to the `point_color` of your mesh to see the result.

<span style="color:#90A3F4">***light_data***</span>
<br />The light data output as an object.  This is intended for use with `LB_display`