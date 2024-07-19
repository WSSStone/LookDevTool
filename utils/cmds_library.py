import os

UNREAL_BUILD_TOOL = "E:/UE_5.4.1/Engine/Binaries/DotNET/UnrealBuildTool/UnrealBuildTool.exe"
WINRAR = 'D:/"Program Files"/WinRAR/WinRAR.exe'

class cmd_fab:
    @classmethod
    def fabric_unzip_cmd(cls, compress_path:str, uncompress_path:str) -> str:
        return f'{WINRAR} x "{compress_path}" "{uncompress_path}/"'

    @classmethod
    def fabric_generate_sln_cmd(cls, proj_absname:str) -> str:
        return f'{UNREAL_BUILD_TOOL} -ProjectFiles -project="{proj_absname}" -game -engine'

    @classmethod
    def fabric_softlink_cmd(cls, target_content:str, current_dir:str, targetdirname: str) -> str:
        return cls.fabric_softlink_cmd(target_content, current_dir, targetdirname, targetdirname)

    @classmethod
    def fabric_softlink_cmd(cls, target_content:str, current_dir:str, targetdirname: str, dirname:str) -> str:
        return f'mklink /J "{os.path.join(target_content, targetdirname)}" "{os.path.join(current_dir, dirname)}"'