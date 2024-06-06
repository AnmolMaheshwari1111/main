#include <iostream>
#include <string>

int main() {
    std::string username;
    std::string password;
    int attempts = 0;

    while (attempts < 3) {
        std::cout << "Enter your username: ";
        std::cin >> username;

        std::cout << "Enter your password: ";
        std::cin >> password;

        if (username == "admin" && password == "password") {
            std::cout << "Welcome, admin!\n";
            break;
        } else {
            std::cout << "Invalid username or password. Please try again.\n";
            attempts++;
        }
    }

    if (attempts == 3) {
        std::cout << "Too many failed login attempts. Exiting...\n";
    }

    return 0;
}