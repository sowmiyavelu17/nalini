int main() 
{ 
    int arr[] ={ 1, 2, 3, 4, 5 }; 
    int n=sizeof(arr)/sizeof(arr[0]); 
    int k =2; 
    cout << (kthOdd(arr, n, k)); 
    return 0; 
} 
