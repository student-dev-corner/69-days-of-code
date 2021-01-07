#include<stdio.h>
void main(){
    int a[10],i,n;
    scanf("%d",&n);
    for (i=0;i<n;i++){
        if(i==0)
            scanf("%d",&a[i]);
        else{
            scanf("%d",&a[i]);
            a[i] = a[i-1]^a[i];
        }
    }
    printf("%d",a[n-1]);
}