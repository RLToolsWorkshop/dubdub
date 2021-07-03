from colorama import Fore, init

init(autoreset=True)

success = lambda input: f"{Fore.GREEN}{input}"
failure = lambda input: f"{Fore.RED}{input}"


def run_repl() -> None:
    print(success("Welcome to python nano-REPL"))
    print(success("crtl-c to quit"))
    try:
        while True:
            try:
                _in = input(">>> ")
                try:
                    print(success(eval(_in)))
                except:
                    out = exec(_in)
                    if out != None:
                        print(success(out))
            except Exception as e:
                print(failure(f"Error: {e}"))
    except KeyboardInterrupt as e:
        print("\nExiting...")
