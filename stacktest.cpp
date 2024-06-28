#include <iostream>
#include <string>
using namespace std;

class Stack {
private:
    int top;
    int maxSize;
    char *stackArray;

public:
    Stack(int size) {
        maxSize = size;
        stackArray = new char[maxSize];
        top = -1;
    }

    ~Stack() {
        delete[] stackArray;
    }

    void push(char c) {
        if (top < maxSize - 1) {
            stackArray[++top] = c;
        } else {
            cout << "Stack already full!" << endl;
        }
    }

    char pop() {
        if (top >= 0) {
            return stackArray[top--];
        } else {
            cout << "Stack empty!" << endl;
            return '\0';
        }
    }

    bool isEmpty() {
        return top == -1;
    }
};

int main() {
    string str;
    cout << "Enter string: ";
    getline(cin, str);

    int size = str.length();
    Stack stack(size);

    for (int i = 0; i < size; ++i) {
        stack.push(str[i]);
    }

    cout << "String before popping: " << str << endl;

    for (int i = 0; i < size; ++i) {
        str[i] = stack.pop();
    }

    cout << "String after popping: " << str << endl;
    

    return 0;
}

//    Observation: This string was just reversed showing that stacks are used for reversal of strings as one of their importance.
