public class QuickSort{
    public static void main(String[] args) {
        int[] array = {8, 2, 3, 4, 7, 9, 1, 5, 6};

        sort(array, 0, array.length - 1);

        for(int i: array){
            System.out.print(i + " ");
        }
    }

    private static void sort(int[] array, int start, int end){
        if(end<= start) return;
        int pivot = partition(array, start, end);

        sort(array, start, pivot - 1);
        sort(array, pivot + 1, end);
    }

    private static int partition(int[] array, int start, int end){
        int pivot = array[end];
        int i = start-1;

        for(int j=start; j<=end - 1; j++){
            if(array[j] < pivot){
                i++;
                int temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
        i++;
        int temp = array[i];
        array[i] = array[end];
        array[end] = temp;
        return i;
    }
}