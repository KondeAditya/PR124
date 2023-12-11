#include <iostream>
#include <stack>
using namespace std;
bool isWellParenthesized(string expression) {
    stack<char> s;
    for (int i = 0; i < expression.length(); ++i) {
        char ch = expression[i];
        if (ch == '(' || ch == '[' || ch == '{') {
            s.push(ch);
        } else if (ch == ')' || ch == ']' || ch == '}') {
            if (s.empty() || !((ch == ')' && s.top() == '(') || (ch == ']' && s.top() == '[') || (ch == '}' && s.top() == '{'))) {
                return false;
            }
            s.pop();
        }
    }
    return s.empty();
}
int main() {
    string expression;
    cout << "Enter an expression: ";
    getline(cin, expression);
    if (isWellParenthesized(expression)) {
        cout << "The expression is well parenthesized." << endl;
    } else {
        cout << "The expression is NOT well parenthesized." << endl;
    }
    return 0;
}
