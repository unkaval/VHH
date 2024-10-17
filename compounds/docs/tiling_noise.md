### ***tiling_noise***
<br />A seamless tiling noise compound.

## Inputs

<span style="color:#A8D977">***data_in***</span>
<br />This is an auto-port that will accept a point positions array (vector3) or a mesh UV array (vector2).  When point positions are used, the noise uses the x and z values of the positions, this is very good for planes.  For 3d objects, the UVs will deliver a better result.

<span style="color:#82D99F">***frequency***</span>
<br />The frequency of the noise.

<span style="color:#82D99F">***amplitude***</span>
<br />The amplitude of the noise.

<span style="color:#82D99F">***tile_x***</span>
<br />Number of tiles in the "x" direction.

<span style="color:#82D99F">***tile_y***</span>
<br />Number of tiles in the "y" direction.

<span style="color:#62CFD9">***seed***</span>
<br />The seed for the fractal noise generator.

***

## Output

<span style="color:#82D99F">***tiled_noise***</span>
<br />The output noise values.
