
def run_command(command: str) -> None:
    match command:
        case "quit":
            print("quitting the program")
            quit()
        case "reset":
            print("resetting the program")
        case other:                     # !r means that it takes care of printing single and double quotes
            print(f"Unknown command: {other!r}.")

def main() -> None:
    while 1:
        command = input("$ ")
        run_command(command)
        
        
if __name__ == "__main__":
    main()