#include<iostream>
using namespace std;
int pivot(int arr[],int low,int high);
void quick_sort(int arr[],int low,int high)
{
    if(low<high)
    {
       int partion= pivot(arr,low,high);
        quick_sort(arr,low,partion-1);
        quick_sort(arr,partion+1,high);
    }
}
int pivot(int arr[],int low,int high)
{
    int i=low;
    int j=high;
   int element=arr[low];
   while(i<j)
   {
     while( i<=high && arr[i]<=element )
     {
        i++;
     }
     while( j>=low && arr[j]>element)
     {
        j--;
     }
     if(i<j)
     {
        int temp=arr[i];
        arr[i]=arr[j];
        arr[j]=temp;

     }

   }
   
   arr[low]=arr[j];
   arr[j]= element;
   return j;
}
int main()
{
     int n;
    cout<<"ENTER THE SIZE OF ARRAY : ";
    cin>>n;
    int arr[n];
    
    cout<<"ENTER THE ARRAY: ";
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
    }
    cout<<"ARRAY BEFORE SORTING: ";
    for(int i=0;i<n;i++)
    {
        cout<<arr[i]<< " ";
    }
    quick_sort(arr,0,n-1);
     cout<<"ARRAY AFTER SORTING: ";
    for(int i=0;i<n;i++)
    {
        cout<<arr[i]<<" ";
    }

} 