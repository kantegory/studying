#include <iostream>
using namespace std;

struct Node
{
    Node *l, *r;
    int x;
};

void add(int x, Node *&MyTree) {
    if (NULL==MyTree) {
        MyTree=new Node;
        MyTree->x=x;
        MyTree->l=MyTree->r=NULL;
    }
    if (x<MyTree->x) {
        if (MyTree->l!=NULL) add(x, MyTree->l);
        else {
            MyTree->l=new Node;
            MyTree->l->l=MyTree->l->r=NULL;
            MyTree->l->x=x;
        }
    
    }
    if (x>MyTree->x) {
        if (MyTree->r!=NULL) add(x, MyTree->r);
        else {
            MyTree->r=new Node;
            MyTree->r->l=MyTree->r->r=NULL;
            MyTree->r->x=x;
        }
    }
}

void inorder(Node *&tree) {
    if (NULL==tree) return;
    inorder(tree->l);
    inorder(tree->r);
    cout<<tree->x<<endl;
}

void backorder(Node *&tree) {
    if (NULL==tree) return;
    backorder(tree->l);
    backorder(tree->r);
    cout<<tree->x<<endl;
}

int main() {
    int x;
    Node *MyTree=NULL;
    
    for (int i=0; i<7; i++) {
        cout<<"X=  "; cin>>x;
        add(x, MyTree);
    }
    
    inorder(MyTree);
    backorder(MyTree);
}
