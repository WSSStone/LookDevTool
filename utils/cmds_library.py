import os
import enum

UNREAL_BUILD_TOOL_53 = "E:/UE_5.3/Engine/Binaries/DotNET/UnrealBuildTool/UnrealBuildTool.exe"
UNREAL_BUILD_TOOL_54 = "E:/UE_5.4/Engine/Binaries/DotNET/UnrealBuildTool/UnrealBuildTool.exe"
WINRAR = 'D:/"Program Files"/WinRAR/WinRAR.exe'

class cmd_fab:
    @classmethod
    def fabric_unzip_cmd(cls, compress_path:str, uncompress_path:str) -> str:
        return f'{WINRAR} x "{compress_path}" "{uncompress_path}/"'

    @classmethod
    def fabric_generate_sln_cmd(cls, proj_absname:str, version:str) -> str:
        unreal_build_tool = UNREAL_BUILD_TOOL_53 if version == "5.3" else UNREAL_BUILD_TOOL_54
        return f'{unreal_build_tool} -ProjectFiles -project="{proj_absname}" -game -engine'

    @classmethod
    def fabric_softlink_cmd(cls, target_content:str, current_dir:str, targetdirname: str, dirname:str=None) -> str:
        if dirname is None:
            dirname = targetdirname
        return f'mklink /J "{os.path.join(target_content, targetdirname)}" "{os.path.join(current_dir, dirname)}"'