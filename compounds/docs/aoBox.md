### ***aoBox***
Generate ambient occlusion and assign it to the point color as a float4 (RGBA).  Also included are x, y, and z bounding box gradients.  AO is calculated by raycasting and as such, this compound can get quite heavy.  This compound will output to both a mesh, and as a usd asset. <br />

***
## Input
<span style="color:#90A3F4">***mesh_in***</span>
<br />The input geometry.

## Gradients

<span style="color:#E69963">***output_greyscale***</span>
<br />Output all 4 channels as greyscale.

<span style="color:#E69963">***show_x***</span>
<br />Apply a Bounding Box X gradient to the object

<span style="color:#E69963">***show_y***</span>
<br />Apply a Bounding Box Y gradient to the object.

<span style="color:#E69963">***show_z***</span>
<br />Apply a Bounding Box Z gradient to the object.

<span style="color:#CCB699">***adjust_x***</span>
<br />fCurve for adjustment of the X gradient.

<span style="color:#CCB699">***adjust_y***</span>
<br />fCurve for adjustment of the Y gradient.

<span style="color:#CCB699">***adjust_z***</span>
<br />fCurve for adjustment of the Z gradient.

## Skydome
<span style="color:#E69963">***use_skydome***</span>
<br />When checked, this replaces the bounding box gradients with a skydome light.

## Skydome Color
<span style="color:#A8D977">***ground***</span>
<br />The colour at the bottom of the skydome

<span style="color:#A8D977">***horizon***</span>
<br />The color at the middle of the skydome

<span style="color:#A8D977">***zenith***</span>
<br />The color at the top of the skydome

<span style="color:#82D99F">***skydome_intensity***</span>
<br />The overall brightness of the skydome

<span style="color:#82D99F">***skydome_radius***</span>
<br />The size of the skydome sphere

<span style="color:#62CFD9">***skydome_resolution***</span>
<br />The number of points to calculate the skydome lighting from, the higher the number, the smoother the lighting, but the heavier the calculation.

## Ambient Occlusion

<span style="color:#E69963">***enable_AO***</span>
<br />Enable/Disble ambient occlusion calculations.

<span style="color:#E69963">***normalize_AO***</span>
<br />Scale the AO values to a 0-1 range.

<span style="color:#CCB699">***adjust_normalized_AO***</span>
<br />When normalized, you can adjust the AO with this curve.


## AO settings

<span style="color:#82D99F">***resolution***</span>
<br />AO in this compound is calculated by raycasting. A hemisphere of rays, oriented to the point normal is cast.  This value controls the number of those rays. 

<span style="color:#82D99F">***brightness***</span>
<br />When those rays hit something the `point_color`, which starts as white, has a very small number subtracted from it, making it darker.  This is that number.

<span style="color:#82D99F">***maximum_radius***</span>
<br />This correspond to the length of the ray, The bigger this radius, the further out for a "hit" the ray reached.

<span style="color:#82D99F">***minimum_radius***</span>
<br />Since these rays are looking for hits on the object that is casting them, this number guarantees that the ray doesn't register it's own starting point as a hit, and turn the object totally black.

<span style="color:#E69963">***infinite_radius***</span>
<br />When this is on, the rays will keep going until they hit something.

## USD
This compund offers Bifrost USD for ease of workflow, this works by saving out the USD stage as an asset that is available to be used in Unity or Unreal Engine.  

<span style="color:#D9BE6C">***asset_name***</span>
<br />The name of your asset, this will be carried through to the game engines.

<span style="color:#A8D977">***asset_scale***</span>
<br />The scale of the resulting asset.

<span style="color:#E69963">***enable_usd***</span>
<br />Enables/Disables USD output.  When this is on, the compound saves the asset on any change to the graph.

<span style="color:#D9BE6C">***save_asset_to***</span>
<br />This is the asset on disk.

<span style="color:#D9BE6C">***stage***</span>
<br />This is the usd file you are working on, on disk.

***
## Output
<span style="color:#82D99F">***mesh_output***</span>
<br />Bifrost mesh output - when plugged into `bifrostGeoToMaya`, this can be output to FBX etc.

<span style="color:#82D99F">***usd_output***</span>
<br />The USD stage output, for this to work it must be connected to an output node.

