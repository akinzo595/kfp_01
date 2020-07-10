# kfp  provides a set of Python packages that you can use to specify and run your machine learning (ML) workflows. #
# kfp.dsl: contains the domain-specific language (DSL) that you can use to define and interact with pipelines and components #
# components: includes classes and methods for interacting with pipeline components. Methods in this package include #
# GCP secret: Secrets are secure objects which store sensitive data, such as passwords, OAuth tokens, and SSH keys, in your clusters #

import kfp
import kfp.dsl as dsl
from kfp import components
from kfp.gcp import use_gcp_secret

# This defines the Url to the component that contains the components and pipelines. Google cloud storage bucket could also be an option #
COMPONENT_URI = 'https://raw.githubusercontent.com/MavenCode/kfp_01/master/components_v2'

#This line of code does the ingestion, loading and transformation pulling data from the component directory/folder #
chicago_taxi_dataset_op = components.load_component_from_url(
    f'{COMPONENT_URI}/chicago_taxi_trips_gs_download/component.yaml')
pandas_transform_csv_op = components.load_component_from_url(f'{COMPONENT_URI}/pandas_transform_df/component.yaml')
visualization_op = components.load_component_from_url(f'{COMPONENT_URI}/visualize_table/component.yaml')


@dsl.pipeline(
    name="Chicago Taxi Cab Pipeline",
    description="Pipeline Downloading Data from Google Storage Bucket and Running Training Model in R"
)

#This funtion defines the Pipelines for dowloading chicago dataset. Paths to storage bucket for the csv file is alo defined.# 
#service account access will be applied based on the funtions . The training data will be taken fron the panda transformed csv file #
# output parameters is also defined as Tip in this case #
#This file can be run from the command line as "python chicago_taxi_pipeline" it should generate a .zip file if it runs succesfully #

def chicago_taxi_pipeline():
    gs_download_training_data_in_csv = chicago_taxi_dataset_op(
        gcs_path='gs://kf-demo-data-bucket/taxi_data.csv'
    ).apply(use_gcp_secret('user-gcp-sa')).output

    training_data_for_regression_in_csv = pandas_transform_csv_op(
        table=gs_download_training_data_in_csv,
        transform_code='''df.insert(0, "was_tipped", df["tips"] > 0); del df["tips"]''',
    ).output

    regression_data_visualization = visualization_op(
        train_file_path=training_data_for_regression_in_csv
    ).apply(use_gcp_secret('user-gcp-sa'))


if __name__ == '__main__':
    kfp.compiler.Compiler().compile(chicago_taxi_pipeline, __file__ + '03.zip')
