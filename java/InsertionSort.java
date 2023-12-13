public class InsertionSort {
    public static void main(String[] args) {
        int [] s = {6, 8, 30, 1, 4, 9};
        insert_sort(s);
    }

    static int[] insert_sort(int[] s){
        int i = 1;
        int n = s.length;

        while(i<n){
            int current = s[i];
            int j = i - 1;

            while(j>=0 && s[j]>current){
                s[j+1] = s[j];
                j = j-1;
            }
            s[j+1] = current;
            i++;

        }
        return s;
    }
}
