import subprocess as sb

ramas = sb.check_output(["git", "branch"], text=True)
for rama in ramas.split("\n"):
    rama = rama[2:]  # Quitar los dos espacios que deja git branch
    if rama == "main" or rama == "":
        pass
    else:
        sb.run(["git", "checkout", rama])
        sb.run(["git", "pull", rama, "master"])
        sb.run(["git", "push", "-u", "origin", rama])