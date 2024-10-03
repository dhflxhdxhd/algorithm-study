function solution(s){
    var answer = true;
    
    let count = 0;
    for(let i=0; i<s.length; i++){
        let current = s[i];
        
        if(current === '('){
            count++;
        }else if(current === ')'){
            count--;
            
            if(count < 0){
                answer = false;
                break;
            }
        }
    }

    if(count > 0 || count < 0){
        answer = false;
    }else{
        answer = true;
    }
    
    return answer;
}