function bubble_sort(data){
    let sorted = false;
    while (!sorted) {
        sorted = true;
        data.forEach(function (element, index, array){
            if (element > array[index+1]) {
                array[index] = array[index + 1];
                array[index + 1] = element;
                sorted = false;
      }
    });
  }
  return data;
}

const data = [7, 4, 3, 8, 2, 1, 5, 9];
console.log('Before:', data);
console.log('After:', bubble_sort(data));
