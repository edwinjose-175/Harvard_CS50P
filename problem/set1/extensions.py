# strip file_name off whitespaces and convert to lower case for case and space insensitivity
file_name = input("File name: ").lower().strip()

# split file_name at "." and retrieve last element from list
extension = file_name.split(".")[-1]


match extension:
    case "gif" | "png":
        print(f"image/{extension}")
    case "jpeg" | "jpg":
        print(f"image/jpeg")
    case "zip" | "pdf":
        print(f"application/{extension}")
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")