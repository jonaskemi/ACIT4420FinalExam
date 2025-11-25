import sys
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    print("=" * 60)
    print(" " * 10 + "WELCOME TO SCRIPTING WITH PYTHON - H25")
    print("=" * 60)
    print(" " * 20 + "by Jonas Kemi")
    print()

def main_menu():
    print("\nMain Menu:")
    print("-" * 40)
    print("1. SmartCourier - Package Delivery System")
    print("2. GameOfLife - Conway's Game of Life Simulator")
    print("3. Exit")
    print("-" * 40)
    
    choice = input("\nEnter your choice (1-3): ").strip()
    return choice

def run_smart_courier():
    try:
        from SmartCourier.smart_courier.main import main as smart_courier_main
        clear_screen()
        print("Starting SmartCourier...")
        print("=" * 60)
        smart_courier_main()
    except ImportError as e:
        print(f"Error: Could not import SmartCourier module: {e}")
        print("Make sure SmartCourier package is properly installed.")
    except Exception as e:
        print(f"Error running SmartCourier: {e}")
    
    input("\nPress Enter to return to main menu...")

def run_game_of_life():
    try:
        from GameOfLife.game_of_life.main import main as game_of_life_main
        clear_screen()
        print("Starting Game of Life...")
        print("=" * 60)
        game_of_life_main()
    except ImportError as e:
        print(f"Error: Could not import GameOfLife module: {e}")
        print("Make sure GameOfLife package is properly installed.")
    except Exception as e:
        print(f"Error running GameOfLife: {e}")
    
    input("\nPress Enter to return to main menu...")

def main():
    while True:
        clear_screen()
        print_banner()
        
        choice = main_menu()
        
        if choice == '1':
            run_smart_courier()
        elif choice == '2':
            run_game_of_life()
        elif choice == '3':
            clear_screen()
            print("\nThank you for using my project!")
            print("Goodbye! 👋\n")
            sys.exit(0)
        else:
            print("\n❌ Invalid choice. Please enter 1, 2, or 3.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
    