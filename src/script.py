import tensorflow as tf


def build_writer(path):
    return tf.io.TFRecordWriter(path)


def use_writer(path):
    writer = build_writer(path)
    writer.write("Some record")
    writer.close()


if __name__ == "__main__":
    use_writer("output/new.tfrecord")
