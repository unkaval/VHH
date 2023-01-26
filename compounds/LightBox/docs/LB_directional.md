### ***LB_directional***
**Component Compound** - this compound is a light in the the LightBox system.<br /><br />
**Directionallight** - This is a diffuse light generator that mimics the lighting from a *directional* light.  It does this by taking the light direction and the mesh surface normal, performing a dot product and multiplying by the light's intensity.  Then applying shadow information.<br /><br />
The diagnostic tab will hide and show the shadow rays to the light.<br />

***
## Input
<span style="color:#90A3F4">***input_mesh***</span>
<br />The object you are lighting.

<span style="color:#90A3F4">***accelerator***</span>
<br />You need to construct a raycast accelerator from the mesh to plug in here.

<span style="color:#A8D977">***light_direction***</span>
<br />The direction the light is pointing.  If you are using a Maya light, you will need to derive this from it's matrix.

<span style="color:#A8D977">***directional_intensity***</span>
<br />Intensity and color of the light.

<span style="color:#A8D977">***icon_position***</span>
<br />The position of the directional icon in world space.

<span style="color:#82D99F">***directional_weight***</span>
<br />This is an overall multiplier of the output.  It is a auto-port, allowing for the input of `float`, `floatArray` and `scalar_field` data.

***
## Output
<span style="color:#82D99F">***direction_contribution***</span>
<br />An array of values, per point, of this light's contribution to the lighting.  Add this to the `point_color` of your mesh to see the result.

