### ***bf_connectivity***
When a mesh or object has islands (connected pieces of the mesh that may not be connected to each other) this compound will assign an id to each of the points or the faces in those islands, per island.  This is a similar result to Houdini's `connectivity` node<br />

***
## Input
<span style="color:#90A3F4">***in_mesh***</span>
<br />The mesh coming in, that contains islands.

<span style="color:#D9BE6C">***island_id_point_property***</span>
<br />The property that will be assigned to the points in each island.

<span style="color:#D9BE6C">***island_id_face_property***</span>
<br />The property that will be assigned to the faces in each island..

***
## Output
<span style="color:#90A3F4">***out_mesh***</span>
<br />Description.

<span style="color:#62CFD9">***point_id_per_island***</span>
<br />The point ID array.

<span style="color:#62CFD9">***face_id_per_island***</span>
<br />The face ID array.

