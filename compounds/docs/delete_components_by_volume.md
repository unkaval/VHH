### ***delete_components_by_volume***
This compound deletes faces (by default) or points based on whether those points are inside an object.  It will also generate scatter weights for that object to exclude the culled components.  Because it's interanlly based on a volume, you are able to erode/grow the volume.<br />

***
## Input
<span style="color:#90A3F4">***object_to_delete_from***</span>
<br />The object you wish to cull **from**.

<span style="color:#90A3F4">***culling_object***</span>
<br />The object inside which the components are culled.

<span style="color:#E69963">***points***</span>
<br />When this is true, the compound will delete points from the `object_to_delete_from` rather than faces.

<span style="color:#E69963">***volume_mode***</span>
<br />Solid mode voxelizes the mesh with a solid interior. Shell mode voxelizes the mesh as a thickened surface with a hollow interior.

<span style="color:#82D99F">***volume_resolution***</span>
<br />The resolution of the interior volume.  Smaller numbers will cull "tighter" to the culling object.

<span style="color:#82D99F">***offset_volume***</span>
<br />Erode/Expand the interior volume.

<span style="color:#CCB699">***adjust_culling***</span>
<br />An fCurve that controls the erode/expand of the internal volume.

***
## Output
<span style="color:#90A3F4">***culled_object***</span>
<br />The resulting object.

<span style="color:#82D99F">***scatter_weights***</span>
<br />Scatter weights array containing 0 (no poins) and 1 (all points).

