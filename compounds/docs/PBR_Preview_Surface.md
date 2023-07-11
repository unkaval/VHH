### ***PBR_Preview_Surface***
This compound creates a prim that defines a PBR material with a UsdPreviewSurface shader.  It allows you to connect textures up to the various inputs that make up the shader.  This compound is intended to make and export PBR game shaders and materials to game engines like Unreal or Unity, or systems like Omniverse.  It is designed to create a prim definition to be plugged into an existing USD system.<br />

***
## Input
<span style="color:#D9BE6C">***path***</span>
<br />The path for the new material.  If the output of this node is connected to the `children` port of a prim definition downstream, this path will be appended to the path specified there.
***

***Color***<br />
<span style="color:#A8D977">***diffuse_color***</span>
<br />When there is no texture file connected to the `diffuse_map`, this is the color value used.

<span style="color:#D9BE6C">***diffuse_map***</span>
<br />The path to a texture file to use instead of `diffuse_color`.

<span style="color:#62CFD9">***diffuse_color_space***</span>
<br />The color space of the incoming diffuse texture.
* `auto` - Check for gamma/color space metadata in the texture file itself; if metadata is indicative of sRGB, mark texture as sRGB.
* `sRGB` - Mark texture as sRGB when reading.
* `raw` - Use texture data as it was read from the texture and do not mark it as using a specific color space.

<span style="color:#A8D977">***diffuse_scale***</span>
<br />Scale to be applied to all components of the diffuse texture.

<span style="color:#A8D977">***diffuse_bias***</span>
<br />Bias to be applied to all components of the diffuse texture.

<span style="color:#A8D977">***emission_color***</span>
<br />When there is no texture file connected to the `emission_map`, this is the color value used.

<span style="color:#D9BE6C">***emission_map***</span>
<br />The path to a texture file to use instead of `emission_color`.

<span style="color:#62CFD9">***emission_color_space***</span>
<br />The color space of the incoming emission texture.
* `auto` - Check for gamma/color space metadata in the texture file itself; if metadata is indicative of sRGB, mark texture as sRGB.
* `sRGB` - Mark texture as sRGB when reading.
* `raw` - Use texture data as it was read from the texture and do not mark it as using a specific color space.

<span style="color:#A8D977">***emission_scale***</span>
<br />Scale to be applied to all components of the emission texture.

<span style="color:#A8D977">***emission_bias***</span>
<br />Bias to be applied to all components of the emission texture.
***

***Specular***<br />
<span style="color:#82D99F">***clearcoat***</span>
<br />When there is no texture file connected to the `clearcoat_map`, this is the color value used.

<span style="color:#D9BE6C">***clearcoat_map***</span>
<br />The path to a texture file to use instead of `clearcoat`.

<span style="color:#A8D977">***clearcoat_scale***</span>
<br />Scale to be applied to all components of the clearcoat texture.

<span style="color:#A8D977">***clearcoat_bias***</span>
<br />Bias to be applied to all components of the clearcoat texture.

<span style="color:#82D99F">***index_of_refraction***</span>
<br />Description.

<span style="color:#82D99F">***metallic***</span>
<br />When there is no texture file connected to the `metallic_map`, this is the color value used.

<span style="color:#D9BE6C">***metallic_map***</span>
<br />The path to a texture file to use instead of `metallic`.

<span style="color:#A8D977">***metal_scale***</span>
<br />Scale to be applied to all components of the metallic texture.

<span style="color:#A8D977">***metal_bias***</span>
<br />Bias to be applied to all components of the metallic texture.

<span style="color:#82D99F">***roughness***</span>
<br />When there is no texture file connected to the `roughness_map`, this is the color value used.

<span style="color:#D9BE6C">***roughness_map***</span>
<br />The path to a texture file to use instead of `roughness`.

<span style="color:#A8D977">***roughness_scale***</span>
<br />Scale to be applied to all components of the roughness texture.

<span style="color:#A8D977">***roughness_bias***</span>
<br />Bias to be applied to all components of the roughness texture.
***

***Normal***<br />
<span style="color:#D9BE6C">***normal_map***</span>
<br />The path to a texture file to be used as the normal map.

<span style="color:#62CFD9">***normal_color_space***</span>
<br />The color space of the incoming emission texture.
* `auto` - Check for gamma/color space metadata in the texture file itself; if metadata is indicative of sRGB, mark texture as sRGB.
* `sRGB` - Mark texture as sRGB when reading.
* `raw` - Use texture data as it was read from the texture and do not mark it as using a specific color space.
***

***Opacity***<br />
<span style="color:#82D99F">***opacity***</span>
<br />When there is no texture file connected to the `opacity_map`, this is the color value used.

<span style="color:#D9BE6C">***opacity_map***</span>
<br />The path to a texture file to use instead of `opacity`.

<span style="color:#A8D977">***opacity_scale***</span>
<br />Scale to be applied to all components of the opacity texture.

<span style="color:#A8D977">***opacity_bias***</span>
<br />Bias to be applied to all components of the opacity texture.
***

***Occlusion***<br />
<span style="color:#D9BE6C">***occlusion_map***</span>
<br />The path to a texture file to be used as the occlusion map.

<span style="color:#A8D977">***occlusion_scale***</span>
<br />Scale to be applied to all components of the occlusion texture.

<span style="color:#A8D977">***occlusion_bias***</span>
<br />Bias to be applied to all components of the occlusion texture.
***

***Stacked map***
<br />This is a texture where each channel (R,G,B,A) represents a different map.  This is to increase the efficiency of the textures in the game engine.

<span style="color:#D9BE6C">***stacked_map***</span>
<br />The path to a texture file that is a stacked texture, representing different channels.  *Note:* When this is used, it will override the single-channel maps above.  The scale and bias of `metallic`, `opacity`, `occlusion` and `roughness` in the single channel maps above will apply to the channels selected here.
 
<span style="color:#62CFD9">***red_is***</span>
<br />Which map is represented by the red channel of the incoming texture.
* `occlusion` - the channel represents the occlusion map.
* `roughness` - the channel represents the roughness map.
* `metallic` - - the channel represents the metallic map.
* `opacity` - - the channel represents the opacity map.

<span style="color:#62CFD9">***green_is***</span>
<br />Which map is represented by the green channel of the incoming texture.
* `occlusion` - the channel represents the occlusion map.
* `roughness` - the channel represents the roughness map.
* `metallic` - - the channel represents the metallic map.
* `opacity` - - the channel represents the opacity map.

<span style="color:#62CFD9">***blue_is***</span>
<br />Which map is represented by the blue channel of the incoming texture.
* `occlusion` - the channel represents the occlusion map.
* `roughness` - the channel represents the roughness map.
* `metallic` - - the channel represents the metallic map.
* `opacity` - - the channel represents the opacity map.

<span style="color:#62CFD9">***alpha_is***</span>
<br />Which map is represented by the alpha channel of the incoming texture.
* `occlusion` - the channel represents the occlusion map.
* `roughness` - the channel represents the roughness map.
* `metallic` - - the channel represents the metallic map.
* `opacity` - - the channel represents the opacity map.

<span style="color:#90A3F4">***attribute_definitions***</span>
<br />Optionally, connect one or more attribute definitions for the material. You can right-click on the port and choose Connect Node to quickly add and connect a `define_usd_attribute`.

***
## Output
<span style="color:#90A3F4">***material_definition***</span>
<br />The material prim definition. You can connect this into the `prim_definitions` port of an `add_to_stage` node, or to the `children` port of another `define_usd_prim` or similar node. You can also connect this into the material port of a `define_usd_prim` or similar node to bind the material to the prim. 

