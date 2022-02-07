# `falloff_field`
Spherical falloff field.

## Inputs
### `loc_in`
`world_matrix` connection from the locator used to control the SRT of the field.  This needs to be connected in the node editor. 

### `magnitude`
A multiplier to adjust the overall magnitude of the field.

### `falloff`
An fCurve to control the shape of the falloff.

### `noise`
Add noise to the field.

### `noise_frequency`
The frequency of the added niose.

### `seed`
Seed for the random number generator.

### `display divisions`
Number of divisions in the resulting field display.

## Output

### `field`
The resulting field at it's magnitude.


