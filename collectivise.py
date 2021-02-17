
import sys
import zipfile
import os

# https://stackoverflow.com/a/1855118/8219760
def zip_directory(path, fobj):
    for root, dirs, files in os.walk(path):
        for file in files:
            fobj.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(path, '..')))

if __name__=="__main__":
    args = sys.argv
    print(args)
    source = args[1]
    source = os.path.realpath(source)
    print(source)
    if len(args) < 3:
        dest = "collectivised_" + os.path.basename(os.path.normpath(source)) + ".zip"
    else:
        dest = args[2]

    with zipfile.ZipFile(dest, "w") as fobj:
        if os.path.isdir(source):
            print("is directory")
            zip_directory(source, fobj)
        elif os.path.isfile(source):
            print("Is file")
            fobj.write(source)
        else:
            raise ValueError(f"Invalid source '{source}'.")

        image_path = os.path.join(os.path.dirname(__file__), "I_serve_the_soviet_union.jfif")
        fobj.write(image_path)
    
    print(f"Wrote to {dest}.")
