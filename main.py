"""
Main entry point for the CODE project.
Provides CLI navigation between SmartCourier and GameOfLife packages.
"""

import sys
import os

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Print welcome banner."""
    print("=" * 60)
    print(" " * 15 + "WELCOME TO CODE PROJECT")
    print("=" * 60)
    print()

def main_menu():
    """Display main menu and get user choice."""
    print("\nMain Menu:")
    print("-" * 40)
    print("1. SmartCourier - Package Delivery System")
    print("2. GameOfLife - Conway's Game of Life Simulator")
    print("3. Exit")
    print("-" * 40)
    
    choice = input("\nEnter your choice (1-3): ").strip()
    return choice

def run_smart_courier():
    """Run the SmartCourier application."""
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
    """Run the GameOfLife application."""
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
    """Main program loop."""
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
            print("\nThank you for using CODE Project!")
            print("Goodbye! 👋\n")
            sys.exit(0)
        else:
            print("\n❌ Invalid choice. Please enter 1, 2, or 3.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        print("\n\nProgram interrupted by user.")
        print("Goodbye! 👋\n")
        sys.exit(0)