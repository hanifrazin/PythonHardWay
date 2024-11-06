def run():
    print("VROOM")

corvette = {
    "color": "Red",
    "run": run
}

print("My", corvette.get("color"),"can go")

myrun = corvette.get("run")
myrun()
