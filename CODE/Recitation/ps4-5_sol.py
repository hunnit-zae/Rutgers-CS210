# open output file, write mode
outf = open("ps4-5_out.txt","w")

# iterate throuugh input file
for line in open("ps4-5_in.txt"):
    # split on comma
    fields = line.split(',')
   
    # check if person name (first field) starts with 'a'
    if fields[0].strip()[0] != 'a':
        continue
        
    # check if profession (second field) is 'student'
    if fields[1].strip() != 'student':
        continue
    
    outf.write(line)

outf.close()

