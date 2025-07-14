import os

def main():
    print("=== Running My Sample App ===")
    if os.path.exists("index.html"):
        with open("index.html", "r") as file:
            content = file.read()
            print("HTML File Content:")
            print(content)
    else:
        print("index.html not found!")

if __name__ == "__main__":
    main()
