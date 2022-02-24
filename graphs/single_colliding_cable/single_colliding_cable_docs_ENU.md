# `Single Colliding Cable`
This compound is the first Bifrost game tool I have written, huge thanks to Aslan Jafari, [Maxime Jeanmougin](https://app.gumroad.com/mjcg) and most of all, Thomas Pasieka for all the help, support and motivation.

## `Setup`
The compound needs 4 locators (start, middle, middle2, end) to be connected in the node editor.  These locators describe both the catenary curve (start, end) and the bezier curve (start, middle, end for 3-point bezier, all the locators for a 4-point bezier).  The inputs are positional (float3), and named start, middle, middle2 and end.  

Connect any colliders to the "colliders" input.  This is an array input and takes world_matrix inputs.  Simple shapes work best.  The dotted line is what your colliders are colliding with, so make sure you have some mesh - dotted line intersection going on for best effect.

## `Settings`
All the relevant settings are exposed on the bifrost node in the outliner.

### `Cable Radius`
The radius of the cable.

### `Curve Resolution`
The number of divisions **along** the cable.

### `Resolution Along Curve`
The number of divisions **around** the cable.

### `Smoothing`
How smooth the cable is.

### `Mesh Output`
When on, the compound outputs a mesh, with UVs.

### `Collision Surface Displacement`
The amount to lift the cable from the collision surface.

### `Catenary`
When on, the curve is a catenary, 2-point curve (default).  When off, the cable is a bezier curve.

### `Curve Sag`
When **catenary** curve is on, this controls how much the cables sag between collsions.

### `Cubic Bezier`
When **catenary** curve is off, this enables the 'middle2' locator and produces a 4-point bezier.
 
### `Show Collisions`
Visualises the curve collision points.

### `Display Colorx, Display Colory, Display Colorz`
The colour of the cable before meshing.  Display only.






