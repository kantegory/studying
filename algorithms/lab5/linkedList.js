function prepend(x, xs) {
    return function (select) {
        return select(x, xs)
    }
}
function select_head(x, xs) { return x }
function select_tail(x, xs) { return xs }

function head(a) { return a(select_head) }
function tail(a) { return a(select_tail) }
function nil() { return nil }

var linked_list = prepend('1', prepend('3', prepend('7', nil)));
// 'a' -> 'b' -> nil

head(linked_list); // => 'a'
head(tail(linked_list)); // => 'b'
head(tail(tail(linked_list))); // => nil

var arr = [];

while (linked_list !== nil) {
    console.log(head(linked_list));
    arr[arr.length] = head(linked_list);
    linked_list = tail(linked_list)
}

// console.log(arr);

for (i = 0; i < arr.length; i++) {
    if (arr[i] < arr[i - 1]) {
        var result = false
    } else { result = true }
}

console.log('Is sorted? ', result)
