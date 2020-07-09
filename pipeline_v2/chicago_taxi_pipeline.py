import kfp
import kfp.dsl as dsl
from kfp import components
from kfp.gcp import use_gcp_secret

#Url to the component that contains the components and pipelines
COMPONENT_URI = 'https://raw.githubusercontent.com/MavenCode/kfp_01/master/components_v2'

#Data ingestion and transformation
chicago_taxi_dataset_op = components.load_component_from_url(
    f'{COMPONENT_URI}/chicago_taxi_trips_gs_download/component.yaml')
pandas_transform_csv_op = components.load_component_from_url(f'{COMPONENT_URI}/pandas_transform_df/component.yaml')
visualization_op = components.load_component_from_url(f'{COMPONENT_URI}/visualize_table/component.yaml')


@dsl.pipeline(
    name="Chicago Taxi Cab Pipeline",
    description="Pipeline Downloading Data from Google Storage Bucket and Running Training Model in R"
)

#Pipelines for chicago dataset, transformation and training . 
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
