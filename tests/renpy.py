from src import *

displayable = File(
    "displayable",
    items=[
        Class("Displayable"),
    ]
)

core = File(
    "core",
    imports=[
        Import.of(displayable, relative=1, imports=["Displayable"]),
    ]
)

image = File(
    "image",
    items=[
        Function("get_registered_image", params=['name'])
    ]
)

transform = File(
    "transform",
    items=[
        Class("ATLTransform")
    ]
)

im = File(
    "im",
    imports=[
        Import(
            "displayable",
            imports=("Displayable",),
            relative=1
        ),
    ],
    items=[
        Class(
            "Surfer",
            methods=[
                ClassMethod("get_size", return_value=(1920, 1080)),
            ]
        ),
        Class(
            "Image",
            superclass="Displayable",
            methods=[
                ClassMethod.init(("path",)),
                ClassMethod("load", return_value=Value.callable("Surfer"))
            ]
        ),
        Class(
            "Scale",
            superclass="Displayable",
            methods=[
                ClassMethod.init(("path", "width", "height", Parameter.args(), Parameter.kwargs()))
            ]
        ),
        Class(
            "Composite",
            methods=[
                ClassMethod.init(("size", "positions", "displayable"))
            ]
        )
    ]
)

display = Package(
    "display",
    packages=[
        im,
        transform,
        core,
        displayable,
        image
    ]
)

config = File(
    "config",
    items=[
        Variable("basedir", value=Value.str("/")),
        Variable("gamedir", value=Value.str("/game"))
    ]
)

renpy = Package(
    "renpy",
    packages=[
        config,
        display
    ],
    items=[
        Function(
            "loadable",
            params=["path"],
            return_value=True
        )
    ]
)

renpy.create()
