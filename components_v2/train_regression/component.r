#Import required libraries for r component
library("optparse")
library("RDS")
#Training parameters
regression_model <- function(training_data, loss_function, num_iterations, learning_rate, depth, output_model_path) {
    print('hello ML training...')
    output_model_path
}
#The step below is responsible for running regression model, defining the requirement for this specific requirement
option_list = list(
  make_option(
    "-t","--trainingdata", type="character", default=NULL, metavar="character"),
  make_option("-l","--lossfunction", type="character", metavar="character"),
  make_option("-n","--numIterations", type="character", metavar="character"),
  make_option("-n","--learningRate", type="character", metavar="character"),
  make_option("-d","--depth", type="character", metavar="character"),
  c("-m
  ", "--modelOutpath"), type="character", default=NULL, metavar="character")
 
opt_parser = OptionParser(option_list=option_list);
opt = parse_args(opt_parser);

output = regression_model(opt$trainingdata, opt$lossfunction, opt$numIterations, opt$learningRate, opt$depth, opt$modelOutpath )

#implementation
