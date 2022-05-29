import os
from unittest.mock import patch

from src import script


def test_build_writer(tmp_path):
    with patch("src.script.tf.io.TFRecordWriter") as mock_writer:
        filename = "test.tfrecord"
        script.build_writer(os.path.join(tmp_path, filename))
        mock_writer.assert_called_with(os.path.join(tmp_path, filename))


def test_use_writer(tmp_path):
    tfrecord_filename = "test.tfrecord"
    script.use_writer(os.path.join(tmp_path, tfrecord_filename))
    output_files = list(os.listdir(tmp_path))
    assert len(output_files) == 1
    assert output_files[0] == tfrecord_filename
