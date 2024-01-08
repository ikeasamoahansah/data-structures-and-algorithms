import java.util.*;

class Heap{
    int[] arr;
    int arr_size = arr.length;
    int last_index;

    Heap(int[] arr, int arr_size, int last_index){
    }

    void HeapInsert(Heap heap, int value){
        if(this.last_index == this.arr_size - 1){
            this.arr_size * 2;
        }
        this.last_index = this.last_index + 1;
        this.arr[this.last_index] = value;
        HeapifyUp(heap);
    }
}


Object HeapRemoveMax(Heap heap){
    if (heap.last_index == 0){
        return null;
    }
    int result = heap.arr[1];
    heap.arr[1] = heap.arr[heap.last_index];
    heap.arr[last_index] = (Integer) null;
    heap.last_index = heap.last_index - 1;
    return HeapifyDown(heap, 1);
}

int parent(int current){
    return current / 2;
}

void HeapifyUp(Heap heap){
    int current = heap.last_index;
    int parent = parent(current);

    while(parent>=1 && heap.arr[parent] < heap.arr[current]){
        int temp = heap.arr[parent];
        heap.arr[parent] = heap.arr[current];
        heap.arr[current] = temp;
        current = parent;
        parent = parent(current);
    }
}

int HeapifyDown(Heap heap, int idx){
    int lidx = leftChild(idx);
    int ridx = rightChild(idx);
    
    while(idx <= heap.last_index){
        int swap = idx;
        if(lidx <= heap.last_index && heap.arr[swap] < heap.arr[lidx]){
            swap = lidx;
        }
        if(ridx <= heap.last_index && heap.arr[swap] < heap.arr[ridx]){
            swap = ridx;
        }
        if(idx != swap){
            int temp = heap.arr[idx];
            heap.arr[idx] = heap.arr[swap];
            heap.arr[swap] = temp;
            idx = swap;
        } else {
            break;
        }
    }
}

int leftChild(int idx){
    return idx * 2;
}

int rightChild(int idx){
    return idx * 2 + 1;
}
