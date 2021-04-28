def convert_rosout_to_mcu_test_format(old_file_path: str, new_file_path: str, callback_name: str) -> None:
  """
  Convert a log file generated by ROS logging (e.g. ROS_INFO) to a file
  with format 'speed angle\\n...'.
  """
  with open(new_file_path, "w") as out_fp, open(old_file_path, "r") as in_fp:
    for line in in_fp:
      if callback_name in line:
        speed, steering_angle = line.split()[-2:]
        out_fp.write("{} {}\n".format(speed, steering_angle))

if __name__ == "__main__":
  convert_rosout_to_mcu_test_format("rosout.log", "sim_launch_log", "dummy_cmd_callback")