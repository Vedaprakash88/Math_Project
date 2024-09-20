s = "ssssss"

sub_str = []
count = 0

for c in s:
    if c in sub_str:
        count += 1
        sub_str = []
        sub_str.append(c)
    else:
        sub_str.append(c)
count += 1
