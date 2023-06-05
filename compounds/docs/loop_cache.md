### ***loop_cache***
Compound takes in a cache file as a .bob or .abc and outputs a seamless loop between `start_frame` and `end_frame`.<br />

***
## Input
<span style="color:#D9BE6C">***incoming_cache***</span>
<br />A string containing the address of your cache on disk, can be a .bob cache or an .abc cache.

<span style="color:#82D99F">***start_frame***</span>
<br />The frame at which you want to start the loop.<br />**This has to be greater than the start frame of the cache on disk.**

<span style="color:#82D99F">***end_frame***</span>
<br />The frame at which you want to end the loop.<br />**This has to be less than the end frame of the cache on disk.**

***
## Output
<span style="color:#90A3F4">***out_mesh***</span>
<br />The cached points, seamlessly looped from `start_frame` to `end_frame`.

