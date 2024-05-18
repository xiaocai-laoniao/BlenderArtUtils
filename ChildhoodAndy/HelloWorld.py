import bpy

def hello_world():
    print("Blender Hello World!")
    print(f"Blender version: {bpy.app.version}")

if __name__ == "__main__":
    hello_world()