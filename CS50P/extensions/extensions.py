def main() :
    str = input("File name: ")

    if ".gif" in str :
        print("image/gif")
    elif ".jpg" in str :
        print("image/jpeg")
    elif ".jpeg" in str :
        print("image/jpeg")
    elif ".png" in str :
        print("image/png")
    elif ".pdf" in str :
        print("image/pdf")
    elif ".txt" in str :
        print("image/txt")
    elif ".zip" in str :
        print("image/zip")
    else :
        print("application/octet-stream")

main()