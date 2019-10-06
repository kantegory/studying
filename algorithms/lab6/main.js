function sortIt(dict) {

    let keys = [];

    for (let key in dict) {
        keys[keys.length] = key
    }

    let values = [];

    for (key = 0; key < keys.length; key++) {
        values[values.length] = dict[keys [key]]
    }

    let sortedValues = values.sort(sortNumber);
    console.log(sortedValues);

    // create sorted_dict from sorted_values
    // let sorted_dict = {};
    //
    // for (i = 0; i < dict.length; i++) {
    //     for (j = 0; j < sorted_values.length; j++) {
    //         if (dict[i] === sorted_values[j]) {
    //             if (dict[i] in sorted_dict) {
    //                 sorted_dict[dict[i]]++;
    //                 console.log(dict[i])
    //             } else {
    //                 sorted_dict[dict[i]] = 1;
    //                 console.log(dict[i])
    //             }
    //         }
    //     }
    //
    // console.log(sorted_dict)
    // }
}

function sortNumber(a, b) {
    return a - b
}

function counter(message) {

    let freqs = {};

    for (char = 0; char < message.length; char++) {
        if (message[char] in freqs) {
            freqs[message[char]]++
        } else {
            freqs[message[char]] = 1
        }
    }

    sortIt(freqs);
    return freqs
}

function shift(message) {

    let shift_message = '';

    for (char = 0; char < message.length; char++) {
        if (message[char] !== ' ') {
            shift_message += String.fromCharCode(message[char].charCodeAt() + ('E'.charCodeAt() - 'A'.charCodeAt()));
        } else {
            shift_message = ' '
        }

    }

    console.log(shift_message)
}

function main(message) {

    let c = counter(message);
    console.log(c);
    shift(message)

}

main('bsajadjdsha');
