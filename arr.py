int main() 
{ 
    int arr[]={12, 3, 5, 7, 19}; 
    int n = sizeof(arr)/sizeof(arr[0]), k=2; 
    cout << "K'th smallest element is " <<  kthSmallest(arr, n, k); 
    return 0; 
} 
