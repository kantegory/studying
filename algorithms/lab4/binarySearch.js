function binarySearch(data, elem) {
    let left = 0;
    let right = data.length--;
    let found = false;

    while (left <= right && found === false) {
        let middle = ~~((left + right) / 2);
        if (data[middle] === elem) {
            found = true
        } else {
            if (elem < data[middle]) {
                right = middle--
            } else {
                left = middle++
            }
        }
    }
    console.log('Is ', elem, ' in data?\n', found)
}

const data = [5, 32, 41, 58, 132, 146, 178, 179, 230, 237];
console.log('Data: ', data);
binarySearch(data, 146);
