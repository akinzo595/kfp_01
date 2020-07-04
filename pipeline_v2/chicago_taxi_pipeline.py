import kfp
from kfp import components

COMPONENT_URI = 'https://raw.githubusercontent.com/MavenCode/kfp_01/master/components_v2'

chicago_taxi_dataset_op = components.load_component_from_url(
    f'{COMPONENT_URI}/chicago_taxi_trips_gs_download/component.yaml')
pandas_transform_csv_op = components.load_component_from_url(f'{COMPONENT_URI}/pandas_transform_df/component.yaml')


def chicago_taxi_pipeline():
    gs_download_training_data_in_csv = chicago_taxi_dataset_op(
        gcs_path='gs://kf-demo-data-bucket/taxi_data.csv'
    ).output

    training_data_for_classification_in_csv = pandas_transform_csv_op(
        table=gs_download_training_data_in_csv,
        transform_code='''df.insert(0, "was_tipped", df["tips"] > 0); del df["tips"]''',
    ).output


if __name__ == '__main__':
    kfp.compiler.Compiler().compile(chicago_taxi_pipeline, __file__ + '02.zip')
