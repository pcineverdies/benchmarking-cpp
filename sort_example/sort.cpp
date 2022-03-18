void swap(int& a, int& b){
    int c = a;
    a = b; 
    b = c;
}
 
void sort(int array[], int n){
    for (int i = 0; i < n-1; i++){
        for (int j = 0; j < n-i-1; j++){
            if (array[j] > array[j+1])
                swap(array[j], array[j+1]);
        }
    }
}