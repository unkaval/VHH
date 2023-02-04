### ***point_color_by_property***
Allows you to visualise and edit a property on an object.  Useful for visualization and some basic tweaking.  Supports long, float and vector properties.<br />

***
## Input
<span style="color:#90A3F4">***in_geometry***</span>
<br />The geometry to display.  

<span style="color:#D9BE6C">***property***</span>
<br />The property in question.  

<span style="color:#E69963">***write_property***</span>
<br />When true, the property will be set on the object.

<span style="color:#CCB699">***adjust_property***</span>
<br />An fCurve allowing you to adjust the property.  The curve works as a 0-1 range without changing the range of the incoming property.

<span style="color:#A8D977">***color***</span>
<br />The color used for the visualization.  

<span style="color:#E69963">***use_ramp***</span>
<br />Uses a ramp to display the property.  

<span style="color:#E69963">***display_on_points***</span>
<br />Display the color or the ramp on the points, rather than the mesh.  

<span style="color:#E69963">***screen_aligned***</span>
<br />When clicked, points will always face the camera.

<span style="color:#E69963">***shape***</span>
<br />The shape of the display points.

<span style="color:#E69963">***random_color***</span>
<br />Assign a random color to the property.

<span style="color:#62CFD9">***random_color_seed***</span>
<br />The seed for the random color generator.

<span style="color:#A8D977">***custom_ramp_input***</span>
<br />`Array:float3` input allowing you to send a custom array of colors as a custom ramp.  

<span style="color:#E69963">***ramp_preset***</span>
<br />A selection of pre-made ramps. 

***
## Output
<span style="color:#90A3F4">***out_geometry***</span>
<br />The output geometry.





