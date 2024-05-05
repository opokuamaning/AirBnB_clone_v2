from fabric.api import *

# Import your script (assuming it's in the same directory)
from path.to.your.script import do_pack  # Replace with actual path

def pack_web_static():
  """Packs web_static directory into a .tgz archive"""
  archive_path = do_pack()
  if archive_path:
      print(f"Archive created successfully: {archive_path}")
  else:
      print("Error creating archive!")

# Run the pack_web_static function when you execute 'fab'
task(pack_web_static)
