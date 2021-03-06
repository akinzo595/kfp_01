# kfp  provides a set of Python packages that you can use to specify and run your machine learning (ML) workflows. #
# components: includes classes and methods for interacting with pipeline components. Methods in this package include #

import kfp
from kfp import components

# This defines the Url to the component that contains the components and pipelines. Google cloud storage bucket could also be an option #
COMPONENT_URI = 'https://raw.githubusercontent.com/MavenCode/kfp_01/master/components'

# Data ingestion that loads the dataset for the chicago trip and panda transform csv using components to load and transform#

chicago_taxi_dataset_op = components.load_component_from_url(f'{COMPONENT_URI}/chicago_taxi_trips/component.yaml')
pandas_transform_csv_op = components.load_component_from_url(f'{COMPONENT_URI}/pandas_transform_df/component.yaml')

# Loading components and training for  regression, classifier, preddict_classes and predict_values #
# Exporting model to AppleCoreML for prediction using the component URL
# Exporting model to ONYX #

train_classifier_op = components.load_component_from_url(f'{COMPONENT_URI}/train_classifier/component.yaml')
train_regression_op = components.load_component_from_url(f'{COMPONENT_URI}/train_regression/component.yaml')
predict_classes_op = components.load_component_from_url(f'{COMPONENT_URI}/predict_classes/component.yaml')
predict_values_op = components.load_component_from_url(f'{COMPONENT_URI}/predict_values/component.yaml')
predict_class_probabilities_op = components.load_component_from_url(
    f'{COMPONENT_URI}/predict_class_probabilities/component.yaml')
export_model_to_AppleCoreML_op = components.load_component_from_url(
    f'{COMPONENT_URI}/export_model_to_AppleCoreML/component.yaml')
export_model_to_ONNX_op = components.load_component_from_url(f'{COMPONENT_URI}/export_model_to_ONNX/component.yaml')

# This funtion defines the Pipelines for chicago dataset. Training data input parameters is from raining_data_in_csv #
# Training data set for classification and transformation. Input parameters is from pandas_transform_csv_op #
# Setting output parameters #

def chicago_taxi_pipeline():
    training_data_in_csv = chicago_taxi_dataset_op(
        where='trip_start_timestamp >= "2019-01-01" AND trip_start_timestamp < "2019-02-01"',
        select='tips,trip_seconds,trip_miles,pickup_community_area,dropoff_community_area,fare,tolls,extras,trip_total',
        limit=10000,
    ).output

    training_data_for_classification_in_csv = pandas_transform_csv_op(
        table=training_data_in_csv,
        transform_code='''df.insert(0, "was_tipped", df["tips"] > 0); del df["tips"]''',
    ).output

    evaluation_data_for_regression_in_csv = training_data_in_csv
    evaluation_data_for_classification_in_csv = training_data_for_classification_in_csv

    train_regression_task = train_regression_op(
        training_data="training_data_in_csv",
        loss_function='RMSE',
        label_column=0,
        num_iterations=200,
    )

    regression_model = train_regression_task.outputs['model']



if __name__ == '__main__':
    kfp.compiler.Compiler().compile(chicago_taxi_pipeline, __file__ + '03.zip')
