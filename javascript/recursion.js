function add(number) {
    if(number === 1){
        return 1;
    }
    return number + add(number-1);
}

console.log(add(5));