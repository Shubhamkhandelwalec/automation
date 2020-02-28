 library(plumber)
 r <- plumb("loop.R")  # Where 'loop.R' is the location of the file shown above
 r$run(port=3000)