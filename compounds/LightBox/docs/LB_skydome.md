### ***LB_skydome***
**Component Compound** - this compound is a light in the the LightBox system.<br /><br />
**Skydome** - This is a diffuse light generator that mimics the lighting from a *skydome* light.  It does this by taking the direction to each point in the "dome" (a sphere generated based on input) and the mesh surface normal, performing a dot product and multiplying by the light's intensity.<br /><br />
The diagnostic tab will hide and show the dome generated sphere.<br />

***

## Input

<span style="color:#90A3F4">***input_mesh***</span>
<br />The object you are lighting. 

<span style="color:#E69963">***enable_skydome***</span>
<br />An "on/off" switch for the domelight contribution, when this is checked, the compound will output the resulting values for the domelight to be added to the lighting. 

<span style="color:#82D99F">***dome_radius***</span>
<br />The radius of the dome.  This should be considerably larger than the object you are lighting.

<span style="color:#A8D977">***ground***</span>
<br />The color at the bottom of the domelight.

<span style="color:#A8D977">***sky_horizon***</span>
<br />The color at the middle of the domelight.

<span style="color:#A8D977">***sky_zenith***</span>
<br />The color at the top of the domelight.

<span style="color:#82D99F">***intensity***</span>
<br />The overall brightness of the domelight.

<span style="color:#82D99F">***horizon_bias***</span>
<br />Adjusts the position of the dome's horizon.

<span style="color:#62CFD9">***dome_resolution***</span>
<br />The number of points to calculate the domelight lighting from, the higher the number, the smoother the lighting, but the heavier the calculation.

<span style="color:#82D99F">***weight***</span>
<br />This is an overall multiplier of the output.  It is a auto-port, allowing for the input of `float`, `floatArray` and `scalar_field` data.

<span style="color:#A8D977">***black_array***</span>
<br />This port is intended for use in the LightBox system.  It is an array of value {0,0,0} that the light result will be added to, can be left unconnected. 

***
## Output
<span style="color:#A8D977">***skydome_contribution***</span>
<br />An array of values, per point, of this light's contribution to the lighting.  Add this to the `point_color` of your mesh to see the result. 

<span style="color:#90A3F4">***light_data***</span>
<br />An object carrying the light data - this is intended for use with the `LB_display` compound. 
