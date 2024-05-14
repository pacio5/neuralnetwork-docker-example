# Neural Network Docker Example

Example of how to use docker to run a neural network on NVIDIA GPUs

## Structure of the project

The project is structured as follows:

- **Dockerfile**: Docker creation file containing parameters and definitions to run the algorithm
- **train.py**: Contains the script to train the model.
- **LICENSE**: code use license

## Instructions for running the code

### 1. Build the image

Once a Dockerfile has been defined for the project to be executed, the next step is to create the container image. The following command is employed to generate the image:

```docker build -t [image-name] .```

It is necessary to select an image name ([image-name]) and to place it in the Dockerfile folder when the build is initiated. 

### 2. Create and run the container 

Once the image has been created, the container can be run. This is achieved by executing the following command: 

```docker run --gpus all -v my-host-path:/usr/src/app/logs [image-name] > my-host-path/log.txt 2>&1```

This command instructs Docker to execute a new container on the available GPUs. A volume is mounted, connecting a folder on the host with a specific folder in the container. Standard output (stdout) and standard errors (stderr) are redirected to a log file.

Once the process has been completed, the container can be deleted and the results can be viewed in the host folder that was specified.