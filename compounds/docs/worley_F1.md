# `Worley F1`
Basic Worley (Cellular) Noise Generator.  One point per cell, takes the nearest neighbor to calculate distance (n = 1).

## Inputs
### `geometry`
The input mesh to calculate the noise upon

### `magnitude`
A multiplier to adjust the overall magnitude of the resulting noise.

### `frequency`
The number of cells to be created on the object.

### `metric`
How the cell center distances are calculated:
+  Euclidian:  distance by vector length. 
+  Manhattan:  also called "Taxicab geometry", distance is the sum of the absolute difference of their positions.
+  Chebeshev:  distance is the maximum component of the distance vector.

### `scatter_type`
+ Bounds Cube:  Cell centers are scattered inside the bounding box.
+ Bounds Sphere:  Cell centers are scattered inside the bounding sphere.
+ on Object:  Cell centers are scattered on the object surface.

### `padding`
Amound to add to Bounds Cube and Bounds Sphere scatter type.

### `seed`
Seed for the random number generator.

### `F`
Which neighbor to calculate distance to:  F=0 is the nearest neighbor, F=1 the next nearest etc.

## `Scattering Options`
Scattering and display controls.

### `on Object::mode`
Scatter on Object controls
+ Uniform: pseudo-random distribution.
+ BlueNoise:  low discrepancy distribution.
+ BlueNoiseMaximal:  most relaxed distribution (slow).

### `Sphere::Sphere Interpolation`
Controls the interpolation of the distances towards the center of the sphere when scatter type is set to "Bounds Sphere"

+ Ease_in:  slow start, quick finish.
+ Ease_out:  quick start, slow finish.
+ Exponent:  exponentional (power of 2) interpolation.
+ SmoothStep: slow start and finish, smooth curve.
+ Off:  No interpolation.

### `Euclidian::Adjust Shape`
fCurve to control the falloff of the Euclidian distribution.

### `Display::Feature Points Default Colour`
If no colour array is plugged into the "feature_points_color_in" plug, all points will default to this colour for display.

## Output

### `noise scaled`
The resulting noise output at it's generated magnitude.

### `noise`
The resulting noise output at a range of -1.0 to 1.0.

