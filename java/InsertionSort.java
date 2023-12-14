public class InsertionSort {
    public static void main(String[] args) {
        int s[] = {6, 8, 30, 1, 4, 9};
        insert_sort(s);

        for(int i : s){
            System.out.print(i + "");
        }
    }

    static int[] insert_sort(int[] s){
        int n = s.length;

        for(int i =1; i<n; i++){
            int temp = s[i];
            int j = i - 1;

            while(j>=0 && s[j]>temp){
                s[j+1] = s[j];
                j--;
            }
            s[j+1] = temp;
        }
        return s;
    }
}
