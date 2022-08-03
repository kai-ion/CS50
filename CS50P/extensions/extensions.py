def main() :
    str = input("File name: ").lower()

    if ".gif" in str :
        print("image/gif")
    elif ".jpg" in str :
        print("image/jpeg")
    elif ".jpeg" in str :
        print("image/jpeg")
    elif ".png" in str :
        print("image/png")
    elif ".pdf" in str :
        print("application/pdf")
    elif ".txt" in str :
        print("text/plain")
    elif ".zip" in str :
        print("application/zip")
    else :
        print("application/octet-stream")

main()