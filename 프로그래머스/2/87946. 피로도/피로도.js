function solution(k, dungeons) {
    const orders = Array.from({ length: dungeons.length }, (value, index) => index);
    const result = [];
    
    getPermutations(orders, [], result);
    
    let maxDungeon = 0;
    for (const order of result) {
        let energy = k;
        let count = 0;

        for (const index of order) {
            if (energy >= dungeons[index][0]) {
                count++;
                energy -= dungeons[index][1];
            }
        }
        maxDungeon = Math.max(maxDungeon, count);
    }
    return maxDungeon;
}

function getPermutations(arr, current = [], result) {
    if (arr.length === 0) {
        result.push(current);
        return; 
    }
    
    for (let i = 0; i < arr.length; i++) {
        const next = arr.slice(0, i).concat(arr.slice(i + 1));
        getPermutations(next, current.concat(arr[i]), result);
    }
}