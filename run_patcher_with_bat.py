import sys
import webbrowser  # noqa
from datetime import datetime
from src import ModConfig
from src.data import build_database, load_database_from_disk
from src.utils.database_utils import verify_database
from src.utils.dictionary_utils import initialize_dictionary_files
from src.utils.logging_utils import setup_logger
from src.utils.config_utils import get_mod_dst_path
from subprocess import Popen

logger = setup_logger('patcher')


def confirm_release_build() -> bool:
	"""Prompt user to confirm release build."""
	while True:
		response = input("Are you sure you want to write the release build? (y/n): ").lower()
		if response == 'y':
			return True
		elif response == 'n':
			return False
		print("Please enter 'y' or 'n'")


def confirm_database_rebuild() -> bool:
	"""Prompt user to confirm database rebuild."""
	while True:
		response = input("Database is out of date. Rebuild database? (y/n): ").lower()
		if response == 'y':
			return True
		elif response == 'n':
			return False
		print("Please enter 'y' or 'n'")


if __name__ == "__main__":
	run_bat = input("Run GenerateMod.bat automatically after patcher? (y/n): ").lower() == "y"
	# run_game = input("Run WARNO automatically after GenerateMod.bat? (y/n): ").lower() == "y" if run_bat else False

	try:
		logger.info("Starting WARNO mod patcher")

		# Load configuration first
		config = ModConfig.get_instance()

		# Check if this is a release build
		if not config.config_data['build_config']['write_dev']:
			if not confirm_release_build():
				logger.info("Release build cancelled by user")
				sys.exit(0)
			logger.info("Release build confirmed by user")

		# Initialize dictionary files
		initialize_dictionary_files()

		# Verify database status
		if not verify_database(config.config_data):
			if config.config_data['data_config']['build_database']:
				logger.info("Rebuilding outdated database...")
			elif confirm_database_rebuild():
				config.config_data['data_config']['build_database'] = True
				logger.info("User confirmed database rebuild...")
			else:
				logger.warning("Continuing with outdated database...")

		# Always load or build the database
		if config.config_data['data_config']['build_database']:
			config.config_data['game_db'] = build_database(config.config_data)
		else:
			config.config_data['game_db'] = load_database_from_disk(config.config_data)

		# Always build constants precomputation data (regenerates on every run)
		from src.data.constants_precomputation import build_constants_precomputation_data
		constants_data = build_constants_precomputation_data(config.config_data, game_db=config.config_data['game_db'])
		config.config_data['game_db']['deck_pack_mappings'] = constants_data

		# Import and run main after database is loaded
		from src.main import main

		main()

		logger.info(f"Patcher completed successfully at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

	except Exception as e:
		run_bat = False
		logger.error(f"Patcher failed: {str(e)}")
		raise

	if run_bat:
		logger.info("Running GenerateMod.bat")
		try:
			dst_path = get_mod_dst_path(config.config_data)
			p = Popen(f"{dst_path}\\GenerateMod.bat", cwd=dst_path)
			stdout, stderr = p.communicate()
			logger.info("Finished running GenerateMod.bat")
		except Exception as e:
			logger.error(f"Failed to run GenerateMod.bat: {str(e)}")
			run_game = False
		# if run_game:
		# 	try:
		# 		logger.info("Starting WARNO through Steam")
		# 		webbrowser.open("steam://rungameid/1611600", new=0, autoraise=True)
		# 	except Exception as e:
		# 		logger.error(f"Failed to start game: {str(e)}")
