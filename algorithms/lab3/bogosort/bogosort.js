function shuffle(data){
    var count = data.length, temp, index;

    while(count > 0) {
        index = ~~(Math.random() * count);
        count--;

        temp = data[count];
        data[count] = data[index];
        data[index] = temp;
    }

    return data;
}

function bogosort(data) {
  while(!correct_order(data)) {
    data = shuffle(data);
  }

  return data;
}

function correct_order(data) {
  let sorted = true;

  for(let i = 0; i < data.length -1; i++) {
    if(data[i + 1] < data[i]) {
      sorted = false;
    }
  }

  return sorted;
}

const data = [7, 4, 3, 8, 2, 1, 5, 9];
console.log('Before:', data);
console.log('After:', bogosort(shuffle(data)));
