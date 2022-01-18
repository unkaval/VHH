# `bezier_curve`
generates a bezier curve based on 2 anchor points and control points

## Inputs

### `curve_resolution`
the resolution of the quadratic bezier, cubic bezier is double this value

### `show_points`
visualise the points that make up the curves

### `cubic_bezier`
the curves are quadratic beziers by default, this will switch the output to a cubic bezier

### `Inputs`
Anchor and control points input, math vector3 format.  When the output is set to cubic, control_2 is used, otherwise it is ignored
* start
* control_1
* control_2
* end

## Output

### `bezier`
the final curve output as a strand, strand ratio and basis are calculated in the compound





