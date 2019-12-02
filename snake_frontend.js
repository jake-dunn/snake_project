const snakeRequest = direction =>{
    let uri = 'http://127.0.0.1:5000/';
    if (['up', 'down', 'left', 'right', 'reset'].includes(direction)){
        uri = uri + direction
    }
    $.ajax({
        type: 'GET',
        crossDomain: true,
        url:uri,
        async: false,
        success: function(snakeData){
            snakeData = JSON.parse(snakeData)
            for( let row of snakeData){
                row.push('\n')
            }
            snakeData= snakeData.reduce((acc, val) => acc.concat(val), []).toString();
            snakeData= snakeData.replace(/-1/g,'B');
            snakeData= snakeData.replace(/-2/g,'R');
            snakeData= snakeData.replace(/,/g,'');
            const myDiv = document.getElementById('myDiv');
            myDiv.innerText=snakeData
        }
    })
};

const snakeUpdate = (snakeData)=>{
        for( let row of snakeData){
            row.push('\n')
        }
        snakeData= snakeData.reduce((acc, val) => acc.concat(val), []).toString();
        snakeData= snakeData.replace(/-1/g,'B');
        snakeData= snakeData.replace(/-2/g,'R');
        snakeData= snakeData.replace(/,/g,'');
        console.log(snakeData);
        const myDiv = document.getElementById('myDiv');
        myDiv.innerText=snakeData
};

snakeRequest();