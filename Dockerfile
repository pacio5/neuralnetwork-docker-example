# Use NVIDIA NGC TensorFlow image with GPU support.
FROM nvcr.io/nvidia/tensorflow:23.02-tf2-py3

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the train.py script (and any other necessary files) into the container.
COPY train.py ./

# Run the script with Python when the container is started.
CMD ["python", "train.py"]
