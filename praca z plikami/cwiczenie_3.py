import sys
if len(sys.argv) != 3:
    print("podałes zła liczbe argumentow")
    exit()

_, file_in, file_out = sys.argv





with open(file_in) as f:
    unique_emails = set()
    for line in f:
        line = line.strip().lower()
        if line.count("@") == 1:
            unique_emails.add(line)

emails = (sorted(unique_emails))
with open(file_out, "w") as f:
    for email in emails:
        f.write(email + "\n")
    #lub:
    #out = "\n".join(emails)
    #f.write(out)
