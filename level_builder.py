# Build script to generate new XML challenge definitions
#
# @Author: Pierre-Yves BRULIN
# @Date: 27-10-2022

from typing import Union


def object_to_xml(
    data: Union[dict, bool],
    root: str = "root",
    default: str = "item",
    spacer: str = "\t",
    level: int = 0,
) -> str:
    """Recursive function to build an XML tree from a Python Iteable (dictionnary or list)
    This is a modified version of https://stackoverflow.com/a/64627138

    Args:
        data (Union[dict, bool]): Data to convert to XML
        root (str, optional): Root of the XML tree. Defaults to "root".
        default (str, optional): Default attribute name if not specified (if given a list). Defaults to "item".
        spacer (str, optional): Space character used to indent the XML tree. Defaults to "[tabulation]".
        level (int, optional): Level of children, this argument is only used by the recursion and should not be specified manually. Defaults to 0.

    Returns:
        str: Converted XML tree
    """
    xml = f"<{root}>"

    if isinstance(data, dict):
        for key, value in data.items():
            xml += (
                "\n"
                + spacer * (level + 1)
                + object_to_xml(
                    value, key, default=default, spacer=spacer, level=level + 1
                )
            )
        xml += "\n" + spacer * level + f"</{root}>"

    elif isinstance(data, (list, tuple, set)):
        for item in data:
            xml += (
                "\n"
                + spacer * (level + 1)
                + object_to_xml(item, default, spacer=spacer, level=level + 1)
            )
        xml += "\n" + spacer * level + f"</{root}>"

    else:
        xml += str(data)
        xml += f"</{root}>"

    return xml


# This dictionnary reproduce the architecture of the Challenge 0
levelData = {
    "name": "New Challenge 0",
    "respawnPoint": {
        "position": {"x": 0, "y": 0, "z": 0},
        "rotation": {"x": 0, "y": 0, "z": 0},
    },
    "startLine": {
        "position": {"x": 0, "y": 0, "z": 6},
        "rotation": {"x": 0, "y": 0, "z": 0},
    },
    "finishLine": {
        "position": {"x": 0, "y": 0, "z": 38},
        "rotation": {"x": 0, "y": 0, "z": 0},
    },
    "gates": [
        {
            "index": i,
            "type": 0,
            "position": {"x": 0, "y": 0, "z": 12 + i * 8},
            "rotation": {"x": 0, "y": 0, "z": 0},
        }
        for i in range(4)
    ],
}

with open("new_challenge_0.xml", "w") as xml:
    xml.write(
        object_to_xml(levelData, root="LevelData", default="gate", spacer=" " * 4)
    )
