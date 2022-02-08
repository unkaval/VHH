# `weighted_average`
Similar to a "normal" average, except that instead of each of the inputs contributing equally to the final average, one input contributes more than the other.  Average with bias.

## Inputs

### `point_A`
the first position

### `point_B`
the second position

### `midpoint_weight`
the weight of the two inputs, 0.5 is both inputs having equal weight.  Lower values weight `point_A`, higher values weight `point_B`

## Output

### `output`
the weighted average value
