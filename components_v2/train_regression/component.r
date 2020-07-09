library("optparse")
library("RDS")
#Training parameters
regression_model <- function(training_data, loss_function, num_iterations, learning_rate, depth, output_model_path) {
    print('hello ML training...')
    output_model_path
}
#Place holder for input parameters
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
