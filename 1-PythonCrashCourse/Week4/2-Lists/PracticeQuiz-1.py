# Given a list of filenames, we want to rename all the files with the extension 
# hpp to the extension h by generating a list of tuples of the form 
# (old_name, new_name).

# That is, given the following list of filenames
# filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# complete the starter code to generate the following newfilenames list of tuples

# newfilenames = [('program.c', 'program.c'), ('stdio.hpp', 'stdio.h'), ('sample.hpp', 'sample.h'), ('a.out', 'a.out'), ('math.hpp', 'math.h'), ('hpp.out', 'hpp.out')]

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
newfilenames = []

for file in filenames:
    if file[-3:] == "hpp":
        newfilenames.append((file, file[:-3] + "h"))
    else:
        newfilenames.append((file, file))

print(newfilenames)