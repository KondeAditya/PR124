#include<iostream>
#define size 10
using namespace std;
class pizza{
    int f,r,q[size];
    public:
    pizza(){
        f=-1;
        r=-1;
    }
    int isfull(){
        return(f==r+1)?1:0;
    }
    int isempty(){
        return(f==-1)?1:0;
    }
    void addO(){
        int ch;
            if(isfull()==0){
                cout<<"\nEnter Pizza ID: ";
                if(f==-1&&r==-1){
                    f=0;
                    r=0;
                    cin>>q[r];
                }else{
                    r=(r+1)%size;
                    cin>>q[r];
                }
            char c;
            cout << "\nDo you want to add another order ? ";
            cin >> c;
            if (c == 'y' || c == 'Y')
                addO();
            }else{
                cout<<"orders are full\n";
            }
    }

    void serve(){
        if (isempty()==0){
            if(f==r){
                cout<<"Order served is "<<q[f];
                cout<<endl;
                f=-1,r=-1;
            }else{
                cout<<"Order served is "<<q[f];
                cout<<endl;
                f=(f+1)%size;
            }
        }else{
            cout<<"Orders are empty!!!\n";
        }
    }

    void display(){
        if (isempty()==0){
            int temp=f;
            while(temp!=r){
                cout<<q[temp]<<"<-";
                temp=(temp+1)%size;
            }
            cout<<q[temp]<<" ";
            cout<<endl;
        }else{
            cout<<"EMpty";
        }
        
    }

};

int main(){
    pizza o;
    int ch;
    int num;
    int flag=1;
    while(flag==1){
        cout<<"1.addO\n2.serve\n3.display\n4.exit\n";
        cout<<"\nEnter Choice: ";
        cin>>ch;
        switch(ch){
            case 1:
                o.addO();
                break;
            case 2:
                o.serve();
                break;
            case 3:
                o.display();
                break;
            case 4:
                cout<<"\nTerminated";
                flag=0;
                break;
            default:
                cout<<"\nInvalid choice!!!\n";         
        }
    }
    return 0;
}