### ***tag_by_string***
This compound allows you to select components to tag.  The components can be selected by single number, ranges and ranges by step, see description below.<br />

***
## Input
<span style="color:#90A3F4">***mesh***</span>
<br />The mesh you wish to tag.

<span style="color:#D9BE6C">***string_input***</span>
<font size =3><br />This is the string that will construct the tags.  Input options are:</font>
>***Single Index:***<br />
><font size =3>A comma separated list of indicies. [0,1,2,3 ...], this will tag a list of the indices provided.</font>
>
>***Index Range:***<br />
><font size =3>Two indices separated by a dash. [0-10], this will tag a range of indicies from first to last.</font>
>
>***Less than an Index:***<br />
><font size =3>Less than chevron followed by the index number. [<10], this will tag all verticies less than the index provided.</font>
>
>***Greater than an Index:***<br />
><font size =3>Greater than chevron followed by the index number. [>10], this will tag all verticies greater than the index provided.</font>
>
>***Range with Step:***<br />
><font size =3>You can get a step on any range of indices you require by adding a colon then the step-size. [<50:10, >10:3, 10-100:4], this will tag the ranges with their steps, so [<50:10] will return 0,10,20,30,40</font>
>
>***Combinations:***<br />
><font size =3>Any and all of the above can be combined to generate more complex selections. [<10:2, 15, 16, 20-30, >40] is a valid string input value for example.</font>
>

<span style="color:#E69963">***faces***</span>
<br />When true, will return the **face** indicies based on the string input.

<span style="color:#D9BE6C">***tag_name_faces***</span>
<br />The tag name used when tagging by faces.

<span style="color:#E69963">***points***</span>
<br />When true, will return the **point** indicies based on the string input.

<span style="color:#D9BE6C">***tag_name_points***</span>
<br />The tag name used when tagging by points.

<span style="color:#82D99F">***component_id_display_offset***</span>
<br />When the *display* flag is on, the compound will display the relevant indices in the viewport.  This controls how far off the surface of the object these will be.

***
## Output
<span style="color:#D9BE6C">***input_string***</span>
<br />This is the input string, output here for use in display or other compounds.

<span style="color:#62CFD9">***indicies***</span>
<br />The indicies selected by the string input.

<span style="color:#E69963">***tag_data***</span>
<br />The tag data array.

<span style="color:#90A3F4">***tagged_geo***</span>
<br />The geo with the tags included.

