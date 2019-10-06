function merge_sort(data) {
    if (data.length > 1) {

        const middle = ~~(data.length / 2);
        const left_half = data.slice(0, middle);
        const right_half = data.slice(middle);

        console.log('break:', left_half, right_half);

        merge_sort(left_half);
        merge_sort(right_half);

        let i = 0;
        let j = 0;
        let k = 0;
        
        while (i < left_half.length && j < right_half.length) {
            if (left_half[i] < right_half[i]) {
                data[k] = left_half[i];
                i++
            } else {
                data[k] = right_half[j];
                j++
            }
            k++
        }

        while (i < left_half.length){
            data[k] = left_half[i];
            i++;
            k++;
        }

        while (j < right_half.length) {
            data[k] = right_half[j];
            j++;
            k++;
        }

        console.log('merge:', data)

    }
}

merge_sort([5,7,4,2,8,6,1,3]);
