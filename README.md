# Glasstiler
*A blurry-border image extender*

This tool can be used to extend images like album covers and posters to a specified aspect ratio, so they can be used as desktop backgrounds without having to crop or stretch/squeeze an image.

The image below, generated with [craiyon](https://www.craiyon.com/), has been processed to an apsect ratio of 1.5.
![psychedelic owl](craiyon_psychowl_two.jpg)


Script currently under development under the **dev** branch.
## Usage

```
positional arguments:
  IMAGE                 image file for tiling
  IMAGEOUT              output image file target

options:
  -h, --help            show this help message and exit
  -v, --verbose         increase output verbosity
  -r RATIO, --ratio RATIO
                        target aspect ratio for tiling

As an alternative to the commandline, params can be placed in a file, one per line, and specified on the commandline like 'glasstiler.py @params.conf'.
```

## Example
Runs the script in verbose mode, tiles the image to a 1.7 aspect ratio.

`./glasstiler.py -v -r 1.7 /path/to/my/image.jpg /path/to/my/newimage.jpg`
