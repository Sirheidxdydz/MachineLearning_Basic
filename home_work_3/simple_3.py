def create_full_path(disk_name, *folders, ext, sep = "\\"):
    if not folders:
        return disk_name

    result_path = disk_name + sep + sep.join(folders) + "." + ext

    return result_path

ful_path = create_full_path('C:', "HomeWork3", "simple_3", ext = "py")
print(ful_path)