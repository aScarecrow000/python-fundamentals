print("mau")
with open("/proc/cpuinfo", "r") as cpu_file:
    for line in cpu_file:
        if line.startswith("model name"):
            # Split the line into parts using ":" as the delimiter
            line_split = line.split(":")

            # print the second part (index 1) after stripping leading and trailing whitespace
            print(line_split[1].strip())
            break

with open("/proc/meminfo", "r") as mem_file:
    for line in mem_file:
        if line.startswith("MemTotal"):
            # 1. Split the line into parts using ":" as the delimiter
            parts_by_colon = line.split(":")

            # 2. Grab the second part (index 1) and split it into words using whitespace as the delimiter
            mem_parts = parts_by_colon[1].split()

            # 3. Isolate the memory value (first word) and convert it to an integer
            kb_string = mem_parts[0]

            # 4. Convert kb_string to an integer --> convert it to gigabytes by dividing by 1,000,000 (or 1024*1024 for mebibytes)
            gb_value = int(kb_string) / 1024**2
            print(f"Memory in GB: {gb_value:.2f} GB")

            break
