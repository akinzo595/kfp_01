library("optparse")

regression_model <- function(training_data, loss_function, num_iterations, learning_rate, depth, output_model_path) {
    print('hello ML training...')
    return output_model_path
}
option_list = list(
  make_option(
      c("--trainingdata"), type="character", default=NULL, metavar="character"),
	make_option(c("--lossfunction"), type="character", metavar="character"),
    make_option(c("--numIterations"), type="character", metavar="character"),
    make_option(c("--learningRate"), type="character", metavar="character"),
    make_option(c("--depth"), type="character", metavar="character"),
    c("--modelOutpath"), type="character", default=NULL, metavar="character")
); 
 
opt_parser = OptionParser(option_list=option_list);
opt = parse_args(opt_parser);

output = regression_model(opt$trainingdata, opt$lossfunction, opt$numIterations, opt$learningRate, opt$depth, opt$modelOutpath )

#implementation