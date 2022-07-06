class Utils:
    global BUILD_LINK
    global BUILD_AND_ROLE_LINK
    global ICON_SIZE
    global get_link
    
    BUILD_LINK = "https://u.gg/lol/champions/{champion_name}/build"
    BUILD_AND_ROLE_LINK = "https://u.gg/lol/champions/{champion_name}/build?role={role}"

    def get_link(champion_name: str, role: str) -> str:
        if role == "":
            return BUILD_LINK.format(champion_name=champion_name)
        else:
            return BUILD_AND_ROLE_LINK.format(champion_name=champion_name, role=role)