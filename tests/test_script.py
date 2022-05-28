import os
from unittest.mock import MagicMock

import src
from src import script


def test_build_writer(tmp_path):
    mock_writer = MagicMock()
    src.script.tf.io.TFRecordWriter = mock_writer
    filename = "test.tfrecord"
    src.script.build_writer(os.path.join(tmp_path, filename))
    mock_writer.assert_called_with(os.path.join(tmp_path, filename))


def test_use_writer(tmp_path):
    tfrecord_filename = "test.tfrecord"
    script.use_writer(os.path.join(tmp_path, tfrecord_filename))
    output_files = list(os.listdir(tmp_path))
    assert len(output_files) == 1
    assert output_files[0] == tfrecord_filename
