from kfp.components import create_component_from_func

def run_spark_job() -> str:
    """
    Run the Spark job using the Docker image.
    """
    import subprocess

    # Command to run the Docker container
    result = subprocess.run(
        [
            "docker",
            "run",
            "-v",
            "/app/data:/app/data",
            "spark-weather-job:latest"
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return result.stdout

# Create a Kubeflow pipeline component
spark_component = create_component_from_func(
    run_spark_job,
    base_image="python:3.8",
    packages_to_install=["subprocess"],
)
