# AirBnB Clone Console

Welcome to the AirBnB Clone Console! This project aims to create a command-line interface (CLI) for managing an AirBnB clone website. The console will allow users to perform various tasks related to user management, property listing management, booking management, and more.

## Command Interpreter

The command interpreter is a Python-based console application that allows users to interact with the AirBnB clone backend through a command-line interface.

### How to Start

To start the AirBnB Clone Console, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the console application using the following command: python console.py

### How to Use

Once the console is running, you can use various commands to manage the AirBnB clone website. Here are some examples:

- `user create <email> <password>`: Create a new user with the specified email and password.
- `property list`: List all properties available on the website.
- `booking create <property_id> <start_date> <end_date>`: Book a property for a specific date range.

For a full list of available commands and their usage, refer to the documentation or use the `help` command within the console.

### Examples

Here are some examples of how to use the AirBnB Clone Console:

- Creating a new user:$ user create example@example.com password123
User created successfully.

- Listing properties:
$ property list
ID | Name | Location | Price
1 | Cozy Apartment | New York, NY | $100/night
2 | Beach House | Malibu, CA | $200/night

- Making a booking:
$ booking create 1 2024-03-10 2024-03-15
Booking successful. Confirmation ID: ABC123

## Contributing

Contributions to the AirBnB Clone Console are welcome! If you have any ideas, bug fixes, or improvements, feel free to submit a pull request. For major changes, please open an issue first to discuss the proposed changes.
