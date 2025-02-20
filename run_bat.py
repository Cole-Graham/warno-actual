from src import ModConfig
from src.utils.config_utils import get_mod_dst_path
from subprocess import Popen

print("Running GenerateMod.bat")
config = ModConfig.get_instance()
dst_path = get_mod_dst_path(config.config_data)
try:
	p = Popen(f"{dst_path}\\GenerateMod.bat", cwd=dst_path)
	stdout, stderr = p.communicate()
	print("Finished running GenerateMod.bat")
except Exception as e:
	print(f"Failed to run GenerateMod.bat: {str(e)}")
