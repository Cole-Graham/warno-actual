import os.path
import shutil

from src import ModConfig
from subprocess import Popen

config = ModConfig.get_instance()
base_path = config.config_data['directories']['warno_mods']

dirs = [d for k, d in config.config_data['directories'].items() if k != 'warno_mods']

flag = None
for d in dirs:
	if os.path.isdir(f"{base_path}/{d}") and flag is None:
		flag = input("Overwrite existing mod folders? (y/n):").lower() == "y"
	if flag:
		shutil.rmtree(f"{base_path}/{d}")
		print(f"Deleted mod folder {d}")

for d in dirs:
	try:
		print(f"Running CreateNewMod.bat with for mod {d}")
		p = Popen(f"{base_path}\\CreateNewMod.bat {d}", cwd=base_path)
		stdout, stderr = p.communicate()
	except Exception as e:
		print(f"Failed to run CreateNewMod.bat with for mod {d}: {str(e)}")
