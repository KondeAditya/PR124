#include<iostream>
#include<string.h>
using namespace std;
int top;
char str[20];
void push(char x){
    top++;
    str[top]=x;
}

void pop(){
    top--;
}

void inp(){
    char ch[20];
    top=-1;
    int i=0,flag=0;
    cout<<"Enter expression: ";
    cin>>ch;
    while(i<strlen(ch)){
        if((ch[i]=='(')||(ch[i]=='[')||(ch[i]=='{')){
            push(ch[i]);
        }
        if(ch[i]==')'){
            if(str[top]=='('){
                pop();
            }
            else{
                cout<<"'(' is absent";
                flag=1;
                break;
            }
        }

        if(ch[i]==']'){
            if(str[top]=='['){
                pop();
            }
            else{
                cout<<"'[' is absent";
                flag=1;
                break;
            }
        }

        if(ch[i]=='}'){
            if(str[top]=='{'){
                pop();
            }
            else{
                cout<<"'{' is absent";
                flag=1;
                break;
            }
        }
        i++;
    }
    if((str[top]==-1) && (flag==0)){
        cout<<"\nEmpty\nWELL BALANCED EXP";
    }
    else{
        cout<<"NOT WELL PARENRTHESIZED";
        while(str[top]!=-1){
            if(str[top]=='('){
                pop();
                cout<<"')' is absent";
            }

            if(str[top]=='['){
                pop();
                cout<<"']' is absent";
            }

            if(str[top]=='{'){
                pop();
                cout<<"'}' is absent";
            }
        }
    }
}

int main(){
    inp();
    return 0;
}
