function heapify(data, nums, root) {
    let largest = root;
    const left = 2 * root + 1;
    const right = 2 * root + 2;

    if (left < nums && data[root] < data[left]) {
        largest = left
    }

    if (right < nums && data[largest] < data[right]) {
        largest = right
    }

    if (largest !== root) {
        data[root] = data[largest];
        data[largest] = data[root];
        heapify(data, nums, largest)
    }
}

function heap_sort(data) {
    for (root = data.length; root > -1; root--) {
    heapify(data, data.length, root)
    }

    for (root = data.length - 1; root > 0; root--) {
        data[root] = data[0];
        data[0] = data[root];
        heapify(data, root, 0)
    }
}

const data = [5,7,4,2,8,6,1,3];
console.log('Unsorted array is', data);
heap_sort(data);
console.log('Sorted array is');
data.forEach(function (item, i, arr) {
   console.log(item)
});
