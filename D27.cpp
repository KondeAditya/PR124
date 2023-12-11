#include<iostream>
#include<stack>
#include<climits>
using namespace std;
class stck{
    public:
    int top,MAX,*a;
    stck(int size){
        top=-1;
        MAX=size;
        a = new int[MAX];
    }
    bool isempty(){
            return(top<0);
        }   
    bool isfull(){
        return(top==MAX-1);
    }
    bool push(int x){
        top++;
        a[top]=x;
        return true;
    }
    int pop(){
        int x = a[top];
        top--;
        return x;
    }
    int peek(){ 
        return a[top];
        }
};

int priority(char ch){
    if(ch=='+'||ch=='-')
        return 1;
    if(ch=='*'||ch=='/')
        return 2;
    if(ch=='^')
        return 3;
    return 0;
}

string cnvrsion(string infix){
    int i=0;
    string postfix;
    stck s(20);
    while(i<infix.length()){
        if(isalpha(infix[i])){
            postfix+=infix[i];
            i++;
        }else if(infix[i]=='('){
            s.push(infix[i]);
            i++;
        }else if(infix[i]==')'){
            while(s.peek()!='(')
                postfix+=s.pop();
            s.pop();
            i++;
        }else{
            while(!s.isempty() && priority(infix[i])<=priority(s.peek())){
                postfix+=s.pop();
            }
            s.push(infix[i]);
            i++;
        }
    }
    while(!s.isempty()){
        postfix+=s.pop();
    }
    return postfix;
}

int eval(string pstfx){
    stack<int> s;
    for(int i =0; i<pstfx.size();++i){
        char c = pstfx[i];
        if(isalpha(c)){
            cout<<"Enter Val of "<<c<<": ";
            int val;
            cin>>val;
            s.push(val);
        }
        else{
            int opre2=s.top();
            s.pop();
            int opre1= s.top();
            s.pop();
            switch(c){
                case '+':
                    s.push(opre1+opre2);
                    break;
                case '-':
                    s.push(opre1-opre2);
                    break;                
                case '*':
                    s.push(opre1*opre2);
                    break;                
                case '/':
                    s.push(opre1/opre2);
                    break;    
            }
        }
    }
    return s.top();
}
int main(){
    string infix;
    cout<<"Enter Infix Expression : "<<endl;
    cin>>infix;
    string postfix = cnvrsion(infix);
    cout<<"PostFix: "<<postfix<<endl;

    cout<<"Evaluation: "<<eval(postfix)<<endl;
    return 0;
}