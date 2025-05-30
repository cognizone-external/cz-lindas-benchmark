import fileinput
import re

example = "<https://lod.opentransportdata.swiss/didok/8516901> <#is_bedienpunkt> \"0\" <https://lindas.admin.ch/sbb/didok> .\n<https://lod.opentransportdata.swiss/didok/8516921> <#is_bedienpunkt> \"0\" <https://lindas.admin.ch/sbb/didok> ."
print(example)
pattern = re.compile("<#(.*)>", flags=re.M)
print(pattern.sub("<\\1>", example))

# Replace the file needed on the following line.
myfile = fileinput.FileInput("lindas.nq", inplace=True)
counter = 0
for line in myfile:
    line = pattern.sub("<https://schema.ld.admin.ch/\\1>", line.rstrip())
    print(line)