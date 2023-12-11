#include <iostream>
#define size 5
using namespace std;
class queue{
public: 
    int f=-1,r=-1;
    string q[size];

    int is_full(){
        return (r>=size-1)?1:0;
    }
    int is_empty(){
        return(f==-1)?1:0;
    }
    void enqueue(string x){
        if(is_full()==1){
            cout<<"Overflow\n";
        }else{
            if(f==-1){
                f++;   
            }
            r++;
            q[r]=x;
        }
    }
    void dequeue(){
        if (is_empty()==1){
            cout<<"Underflow\n";
        }else{
            if(f==r){
                f=r=-1;
            }else{
                cout<<q[f]<<"Deleted\n ";
                f++;
            }
        }
    }
    void display(){
        if (is_empty()==1){
            cout<<"Underflow\n";
        }else{
            for(int i=f;i<=r;i++){
                cout<<q[i]<<" ";
            }
            cout<<endl;
        }
    }
};
int main(){
    queue o;
    int ch;
    string str1;
    int flag=0;
    while (flag==0){
        cout<<"1.Add\n2.Delete\n3.Display\n4.Exit\n";
        cout<<"\nEnter Choice: ";
        cin>>ch;
        switch(ch){
        case 1:
            cout<<"\nEnter Ele to add: ";
            cin>>str1;
            o.enqueue(str1);
            break;
        case 2:
            o.dequeue();
            break;
        case 3:
            o.display();
            break;
        case 4:
            cout<<"Terminated\n";
            flag=1;
            break;       
        default:
            cout<<"Invalid Choice!!\n"; 
        }
    }
    
    return 0;
}