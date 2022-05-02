### ***switch_ramp***
This compounds enables switching between several ramp presets, or inputting a custom ramp.<br />

***
## Input
***: inputs***  
<span style="color:#82D99F">***ramp_intensity***</span>
<br />A zero-to-one array that controls what colour on the ramp applies to which point.

<span style="color:#A8D977">***custom_ramp***</span>
<br />Plug in any array of colors here will override the node and display that custom ramp instead of any selected preset.

<span style="color:#A8D977">***color_0***</span>
<br />The input color corresponding to the first color in the ramp.

<span style="color:#A8D977">***color_1***</span>
<br />The input color corresponding to the second color in the ramp.    

<span style="color:#E69963">***preset***</span>  
<font size="2">**color_0 to color_1**<br />Uses [color_0] and [color_1] above as the ramp.<br />![ramp example](../helper_icons/custom.png)<br/><br/>**monochrome**<br />Ramp from black to white.<br />![ramp example](../helper_icons/monochrome.png)<br/><br/>**black body**<br />Interpretation of the black body temperature ramp.<br />![ramp example](../helper_icons/bbody.png)<br/><br/>**infrared**<br />Interpretation of the classic ironbow ir ramp.<br />![ramp example](../helper_icons/ir.png)<br/><br/>**red to green**<br />A ramp from red through green to blue.<br />![ramp example](../helper_icons/r2g.png)</font>

***: settings***  
<span style="color:#E69963">***reverse***</span>
<br />The reverses the order of the ramp.

<span style="color:#E69963">***normalized_index***</span>
<br />Force index to a 0-1 range.

<span style="color:#CCB699">***adjust_ramp***</span>
<br />An fCurve allowing adjustment of the ramp.

***
## Output
<span style="color:#A8D977">***interpolated***</span>
<br />The ramp output as an array of color values.

