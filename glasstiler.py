#!/usr/bin/env python
#

# import modules used here -- sys is a very standard one
import sys, argparse, logging
import cv2 as cv
import numpy as np

# Gather our code in a main() function
def main(args, loglevel):
  logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)
 

  logging.info("Reading %s", args.image)
  img = cv.imread(args.image)
  #logging.info("You passed an argument.")
  #logging.debug("Your Argument: %s" % args.argument)
  tiled = img

  if tiled.shape[1]/tiled.shape[0] != args.ratio:
      logging.info("Tiling image...")
      flipped = cv.flip(img,1)
      flippedblurred = cv.blur(flipped,(45,45),cv.BORDER_DEFAULT)
      
      imgblurred = cv.blur(img,(45,45),cv.BORDER_DEFAULT)
  
      overlay = np.zeros(flipped.shape,dtype="uint8")
      overlay.fill(100)
      glassimg = cv.addWeighted(imgblurred,1,overlay,0.3,0.0)
      glassflipped = cv.addWeighted(flippedblurred,1,overlay,0.3,0.0)
      
      useFlipped = True
      
      while tiled.shape[0]*args.ratio > tiled.shape[1]:
          
          if useFlipped:
              tiled = np.concatenate((glassflipped,tiled,glassflipped),axis=1)
          else:
              tiled = np.concatenate((glassimg,tiled,glassimg),axis=1)
              
          useFlipped = not useFlipped
      
      if tiled.shape[0]*args.ratio != tiled.shape[1]: 
        trimPixels = - (tiled.shape[0]*args.ratio - tiled.shape[1])
        leftTrim, rightTrim = [trimPixels / 2]*2
        if trimPixels % 2 != 0:
          leftTrim = leftTrim - 0.5
          rightTrim = rightTrim - 0.5
      
        leftTrim, rightTrim = [int(leftTrim), int(rightTrim)]
      
        tiled = np.hsplit(tiled,(leftTrim,tiled.shape[1]-rightTrim))[1]
  
  logging.info("Writing to file...")
  cv.imwrite(args.imageout,tiled)
 
# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  parser = argparse.ArgumentParser( 
                                    description = "Tiles an image horizontally with flipped and frosted-glass-blurred copies of the image to fit a specified aspect ratio.",
                                    epilog = "As an alternative to the commandline, params can be placed in a file, one per line, and specified on the commandline like '%(prog)s @params.conf'.",
                                    fromfile_prefix_chars = '@' )
  # TODO Specify your real parameters here.
  parser.add_argument(
                      "image",
                      help = "image file for tiling",
                      metavar = "IMAGE")
  parser.add_argument(
                      "imageout",
                      help = "output image file target",
                      metavar = "IMAGEOUT")
  parser.add_argument(
                      "-v",
                      "--verbose",
                      help="increase output verbosity",
                      action="store_true")
  parser.add_argument(
                      "-r",
                      "--ratio",
                      help = "target aspect ratio for tiling",
                      metavar = "RATIO",
                      action="store",
                      default=1.5)
  args = parser.parse_args()
  
  # Setup logging
  if args.verbose:
    loglevel = logging.DEBUG
  else:
    loglevel = logging.INFO
  
  main(args, loglevel)
