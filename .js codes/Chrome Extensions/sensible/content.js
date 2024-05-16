console.log('hello');

(function badWords() {
    let para = document.getElementsByTagName('p');
    var arr = [];
    let start = 0;
    while(start < para.length){
        arr.push(para[start]);
        start++;
    }
    for (let i=0; i<para.length; i++){
        var words = para[i].toString();
        for(let j=0; j<words.length; j++){
            console.log(words);
        }
    }
}) ();
(function word(){
    let para = document.getElementsByTagName('p');
    var array = [];
    let start = 0;
    while(start < para.length){
        new_word = para[start].toString().split(" ");
        console.log(new_word[start]);
        start++;
    }
    for(let i =0; i<para.length; i++){
        var words = para[i].toString().split(' ');
        console.log(words.toString());
    }
}) ();