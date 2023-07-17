import subprocess 

data = ( #variable
    subprocess.check_output(["netsh", "wlan", "show", "profiles"])
    .decode("utf-8") # converts the byte string into a Unicode string using the UTF-8 encoding
    .split("\n")
)

profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i] #this line is a list comprehension, which iterates over each element i in the data list
for i in profiles:
    results = (
        subprocess
        .check_output(["netsh", "wlan", "show", "profile", i, "key=clear"])
        .decode("utf-8")
        .split("\n")
    )
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        print("{:<30}|   {:<}".format(i, results [0]))
    except IndexError:
        print("{:<30}|  {:<}".format(i, ""))