#include<iostream>
#include<string.h>
using namespace std;
int top;
char str[20];

void push(char x)
{
    top++;
    str[top]=x;
}

void pop()
{
    top--;
}

void input(){
    char ch[20];
    int i=0,flag=0;
    top=-1;
    cout<<"\nEnter the expression: ";
    cin>>ch;
    while(i<strlen(ch))
    {
        if((ch[i]=='(')||(ch[i]=='{')||(ch[i]=='['))
        {
            push(ch[i]);
        }

        if(ch[i]==')')
        {
            if(str[top]=='(')
                pop();
            else{
                cout<<"'(' is absent"<<endl;
                flag=1;
                break;
            }
        }

        if(ch[i]=='}')
        {
            if(str[top]=='{')
            {
                pop();
            }
            else{
                cout<<"'{' is absent"<<endl;
                flag=1;
                break;
            }
        }

        if(ch[i]==']')
        {
            if(str[top]=='[')
            {
                pop();
            }
            else{
                cout<<"'[' is absent"<<endl;
                flag=1;
                break;
            }
        }
     i++;
    }
    if((str[top]==-1) && (flag=0))
    {
        cout<<"\nSTACK EMPTY!!\nEXPRESSION BALANCED"<<endl;
    }
    else{
        cout<<"NOT WELL PARENTHESIZED"<<endl;
        while(str[top]!=-1)
        {
            if(str[top]=='{')
            {
                pop();
                cout<<"'}' is absent"<<endl;
            }
            if(str[top]=='[')
            {
                pop();
                cout<<"']' is absent";
            }
            if(str[top]=='(')
            {
                pop();
                cout<<"')' is absent";
            }
        }
    }
}

int main()
{
    input();
    return 0;
}
