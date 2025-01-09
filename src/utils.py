from . import ndf


def process_mod(src_path, dst_path):
    """Process mod with given paths"""
    mod = ndf.Mod(src_path, dst_path)
    mod.check_if_src_is_newer()
