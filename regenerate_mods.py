import os.path
import shutil

from src import ModConfig
from subprocess import Popen

# run after game patches to regenerate all mod folders

config = ModConfig.get_instance()
base_path = config.config_data['directories']['warno_mods']
directories = config.config_data['directories']

# CreateNewMod copies from the installed game. VIP preview and public WARNO
# cannot generate each other's mods. Same split as CreateWAvipMods.bat / CreateWAMods.bat.
# ui_only_dev is a public-track folder; the VIP bat does not recreate it.
vip_keys = ("base_vip", "vip_dev")
public_keys = (
	"base_game",
	"gameplay_dev",
	"ui_only_dev",
	"gameplay_release",
	"ui_only_release",
)

while True:
	answer = input("Are you on the VIP preview build? (y/n): ").strip().lower()
	if answer in ("y", "yes"):
		selected_keys = vip_keys
		break
	if answer in ("n", "no"):
		selected_keys = public_keys
		break
	print("Enter y or n.")

dirs = [directories[key] for key in selected_keys]
print("Will recreate:")
for d in dirs:
	print(f"  {d}")

flag = None
for d in dirs:
	mod_path = f"{base_path}/{d}"
	if os.path.isdir(mod_path) and flag is None:
		flag = input("Overwrite existing mod folders? (y/n): ").strip().lower() in ("y", "yes")
	if flag and os.path.isdir(mod_path):
		shutil.rmtree(mod_path)
		print(f"Deleted mod folder {d}")

create_new_mod = os.path.join(base_path, "CreateNewMod.bat")
for d in dirs:
	try:
		print(f"Running CreateNewMod.bat with for mod {d}")
		p = Popen([create_new_mod, d], cwd=base_path)
		stdout, stderr = p.communicate()
	except Exception as e:
		print(f"Failed to run CreateNewMod.bat with for mod {d}: {str(e)}")
