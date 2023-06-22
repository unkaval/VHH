### ***scatter_on_scatter***
A scattered clustering system based on `scatter_on_points`.  This allows control by distance and distribution.  The compound requires input points, and if a mesh is provided will snap the resulting clusters to the mesh.  Without the mesh it will revert to `scatter_on_points` behaviour, and scatters spheres.

***
## Input
<span style="color:#90A3F4">***geo_to_scatter_on***</span>
<br />A mesh input to scatter your clusters on.

<span style="color:#A8D977">***input_points***</span>
<br />This is the required input - these are the point positions that you will scatter clusters around.  These positions can come from any source, a primary scatter, an object, some strands, float3 values, etc.

<span style="color:#82D99F">***density_weights***</span>
<br />This is the culling weights, it is an auto port and therefore can accept floats, float arrays, scalar fields, etc.

***Clusters***<br />
<span style="color:#E69963">***randomise_per_cluster***</span>
<br />When this is checked. The number of points, the seeds and the radius will all be randomized, based on the inputs and according to the seed.  When it is not checked, these values will be static based on the inputs.

<span style="color:#62CFD9">***number_of_points_per_cluster***</span>
<br />The number of points you wish to scatter in each cluster.

<span style="color:#82D99F">***cluster_radius***</span>
<br />The radius of each cluster.

<span style="color:#62CFD9">***cluster_seed***</span>
<br />The seed for the clusters random generator.

*Culling*<br />
<span style="color:#E69963">***cull_overlapping***</span>
<br />Culls overlapping points based on the `overlapping_radius`.

<span style="color:#82D99F">***overlapping_radius***</span>
<br />The radius within which, any points will be culled.

***Point Distribution***<br />
These are several ways to distribute the points around the center point (primary scatter point).  These options are all additive, which means, when enabled, the distributions are added to each other.

*curve*<br />
<span style="color:#E69963">***use_distribution_curve***</span>
<br />Enables curve distribution.  When this is checked, the points will be distributed out from the center according to the `distribution_curve`.  The 0 point of the curve represents the center, the 1 point the radius.

<span style="color:#82D99F">***distribution_curve_magnitude***</span>
<br />A multiplier to the distribution curve.

<span style="color:#A8D977">***distribution_curve***</span>
<br />The master distribution curve.

*exponent*<br />
<span style="color:#E69963">***use_exponential_distribution***</span>
<br />Enables exponential distribution.  When this is checked, the points are distributed exponentially out from the center.

<span style="color:#82D99F">***exponent***</span>
<br />The exponent for distribution.

*gaussian*<br />
<br />A gaussian distribution is also known as a "bell curve". This distribution gathers the points around the center based on the gaussian distribution, there are two options of slightly different distributions.

<span style="color:#E69963">***use_gaussian_distribution_A***</span>
<br />Enables Gaussian A distribution.

<span style="color:#E69963">***use_gaussian_distribution_B***</span>
<br />Enables Gaussian B distribution.

<span style="color:#000000">***gaussian_mean***</span>
<br />The mean is the "average" of the data - this represents the most likely positioning of the points.

<span style="color:#000000">***gaussian_standard_deviation***</span>
<br />The standard deviation is a summary measure of the differences of each observation from the mean. If the differences themselves were added up, the positive would exactly balance the negative and so their sum would be zero.

***display***<br />
<span style="color:#A8D977">***cluster_color***</span>
<br />Display colour for your cluster points.

<span style="color:#82D99F">***cluster_size***</span>
<br />Display size for your cluster points.

<span style="color:#A8D977">***incoming_scatter_color***</span>
<br />Display colour for the incoming (primary) points.

<span style="color:#82D99F">***incoming_scatter_size***</span>
<br />Display size for the incoming (primary) points.

***
### Output
<span style="color:#82D99F">***output***</span>
<br />Your cluster points in a points object.

