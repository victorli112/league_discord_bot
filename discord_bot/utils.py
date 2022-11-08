import os 

class Utils:
    global BUILD_LINK
    global BUILD_AND_ROLE_LINK
    global ICON_SIZE
    global get_link
    global delete_files
    
    BUILD_LINK = "https://u.gg/lol/champions/{champion_name}/build"
    BUILD_AND_ROLE_LINK = "https://u.gg/lol/champions/{champion_name}/build?role={role}"
    ARAM_LINK = "https://u.gg/lol/champions/aram/{champion_name}-aram"

    def get_link(champion_name: str, role: str) -> str:
        if role == "":
            return BUILD_LINK.format(champion_name=champion_name)
        elif role == "aram":
            return "https://u.gg/lol/champions/aram/{champion_name}-aram".format(champion_name=champion_name)
        else:
            return BUILD_AND_ROLE_LINK.format(champion_name=champion_name, role=role)

    def delete_files(files: list):
        for file in files:
            os.remove(file)
