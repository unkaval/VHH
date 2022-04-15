### ***ramp***
This compound generates a ramp output based on several criteria. It outputs both the color per vertex and the geometry with a colour property written to it.
<br /><br />[<span style="color:#CCB699">**ramp (youtube)**</span>](https://youtu.be/S5Kzf1-eiuU)

***
## Input
<span style="color:#90A3F4">***geo_input***</span>
<br />Object to generate a ramp for.  

<span style="color:#A8D977">***in_color_array***</span>
<br />If you have an array of colours, it can be plugged in here.  Plugging an array into this port will override any other colour settings on this compound apart from *constant* and a ramp will be generated from this input.

***single_color***    
<span style="color:#A8D977">***constant***</span>
<br />Colour the object a single, constant colour.  

***start_end_ramp***    
<span style="color:#A8D977">***ramp_start***</span>
<br />First colour of the two-point ramp. 

<span style="color:#A8D977">***ramp_end***</span>
<br />Second colour of the two-point ramp. 

***: controls***    
<span style="color:#E69963">***ramp_type***</span>  
<font size="2">**constant**<br />Sets the colour output to a single, constant colour.<br/><br/>**bounding_box**<br />Bases the ramp on the input object's bounding box.<br/><br/>**random**<br />Bases the ramp random values between the first and last colours in the input ramp or [ramp_start] and [ramp_end].<br/><br/>
**from_property**<br />The ramp's input float array is controlled by the property in the [ramp_property] input.<br/><br/>
**random_from_property**<br />The ramp's input float array is controlled by the property in the [ramp_property] input and the colours are the first and last colours in the input ramp or [ramp_start] and [ramp_end] with a threshold.</font>

<span style="color:#E69963">***erase_colour_property***</span>
<br />This will remove the colour property in the [colour_property] input. 

<span style="color:#D9BE6C">***colour_property***</span>
<br />The name of the colour property already on the geometry or which you want to write on the geometry.

<span style="color:#E69963">***reverse***</span>
<br />Reverses the direction of the array.

<span style="color:#CCB699">***adjust_ramp***</span>
<br />Allows adjustment of the ramp's input float array.

***:: random_ramp***    
<span style="color:#62CFD9">***random_seed***</span>
<br />Seed for the random number generator. 

***:: bounding_box_ramp***    
<span style="color:#E69963">***axis***</span>
<br />Allows choice between X, Y and Z axes.

***:: property_ramp***    
<span style="color:#D9BE6C">***ramp_property***</span>
<br />This is the property to base the ramp's input on.  Currently works with int, float and float3 properties.

***:: random_property_ramp***    
<span style="color:#82D99F">***property_threshold***</span>
<br />Allows you to change the threshold of the two colours. 

***
## Output
<span style="color:#A8D977">***color***</span>
<br />The resulting array of colours.

<span style="color:#90A3F4">***out_geometry***</span>
<br />The input geometry with the [colour_property] written to it.<br/><br/>  




