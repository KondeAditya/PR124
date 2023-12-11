#include<iostream>
#define size 10
using namespace std;
class dque{
    public:
        int f=-1,r=-1;
        int q[size];
    int isfull(){
        return(r>=size-1)?1:0;
    }
    int isempty(){
        return(f==-1)?1:0;
    }

    void add_front(int x){
        if(isfull()==1){
            cout<<"OverFLow\n";
        }else{
            if (f==-1){
                f++;
                r++;
                q[r]=x;
            }else if(f!=0){
                f--;
                q[f]=x;
            }
            
        }        
    }
    void add_rear(int x){
        if(isfull()==1){
            cout<<"OverFLow\n";
        }else{
            if(f==-1){
                f++;
            }
            r++;
            q[r]=x;
        }
    }
    void del_front(){
        if(isempty()==1){
            cout<<"Underflow\n";
        }else{
            if(f==r){
                f=r=-1;               
            }else{
                cout<<q[f]<<"Deleted\n";
                f++;
            }
        }
    }
    void del_rear(){
        if(isempty()==1){
            cout<<"Underflow\n";
        }else{
            if(f==r){
                f=r=-1;               
            }else{
                cout<<q[r]<<"Deleted\n";
                r--;
            }
        }        
    }
    void display(){
        if (isempty()==1){
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
    dque o;
    int ch;
    int num;
    int flag=1;
    while(flag==1){
        cout<<"1.addF\n2.addR\n3.remF\n4.remR\n5.Display\n6.exit\n";
        cout<<"\nEnter Choice: ";
        cin>>ch;
        switch(ch){
            case 1:
                cout<<"\nENter Ele to add Front: ";
                cin>>num;
                o.add_front(num);
                break;
            case 2:
                cout<<"\nENter Ele to add Rear: ";
                cin>>num;
                o.add_rear(num);   
                break;
            case 3:
                o.del_front();
                break;
            case 4: 
                o.del_rear();
                break;
            case 5:
                o.display();
                break;
            case 6:
                cout<<"\nTerminated";
                flag=0;
                break;
            default:
                cout<<"\nInvalid choice!!!\n";         
        }
    }
    return 0;
}