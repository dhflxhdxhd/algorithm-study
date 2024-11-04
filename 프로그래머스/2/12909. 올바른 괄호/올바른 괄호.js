function solution(s){
    var answer = true;
    
    let stack = [];
    for(let word of s){
        if(word === "("){
            stack.push(word);
        }else if(word === ")"){
            if(stack[stack.length-1] == "("){
                stack.pop();
                continue;
            }
            
            answer = false;
            break;
        }
    }
    
    if(answer){
        if(stack.length > 0){
            return false;
        }
        return answer;
    }else{
        return answer;
    }
}