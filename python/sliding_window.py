def fixed_sliding_window(k, arr):
    # Usually given in the question with a 'k' value or so
    #Let's use a subarray problem in which we get the max sub array
    
    curr = sum(arr[:k])
    count = [curr]

    for i in range(len(arr)-k+1):
        # Subtract the first element
        curr -= arr[i-1]
        # Move to the next element
        curr += arr[i+k-1]

        count.append(curr)
    return count


def dynamic_sliding_window(k, arr):
    min_length = float('inf')

    start = 0
    end = 0
    curr_sum = 0

    while end < len(arr):
        curr_sum += arr[end]
        end +=1

        while start < end and curr_sum >= k:
            curr_sum += arr[start]
            start +=1

            min_length = min(min_length, end-start+1)
    return min_length
