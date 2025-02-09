# WARNO ACTUAL Mod Patcher

A mod patcher to build WARNO ACTUAL from scratch, using ndf parse.

## Configuration

To configure the project, copy the template configuration file using one of these commands:

### Windows (Command Prompt)
```batch
copy config\config.template.YAML config\config.YAML
```

### Windows (PowerShell)
```powershell
Copy-Item -Path config\config.template.YAML -Destination config\config.YAML
```

### Linux/macOS
```bash
cp config/config.template.YAML config/config.YAML
```

Then, edit `config/config.YAML` to customize your settings according to your preferences.

### Important Notes
- there is an NDF Parser file in the root directory, which fixes a limitation with ndf parse. You will need to
replace the converter.py file in your ndf parse library installation with this one. It was written by
Ulibos but he hasn't updated the parser yet.
- Ensure that you have the necessary permissions to create and edit files in the project directory.
- Refer to the template configuration file for guidance on the available settings and their expected values.

