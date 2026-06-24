

/**
 REVERSE
function reverse(str) {
    let reversed = ''

    for(let char of str ){
        reversed = char + reversed
    }

    return reversed 
}

function reverse(N){
    const reversed = N.toString().split('').reverse().join('')
    return parseInt(reversed) = Math.sign()
}


PALINDROME


function palindrome(str){
    let reversed = str.split('').reverse().join('')

 return str === reversed
}

console.log(palindrome('madam'));

MAXIMUM CHARACTERS ALIKE

function maxChar(str) {
    const charMap = {}
    let max = 0
    let maxChar = ''
    for(let char of str) {
    
            charMap[char] = ++charMap[char] || 1
        
    }
    for(let key in charMap) {
        if(charMap[key] > max){
            max = charMap[key]
            maxChar = key
        }
    }

    return maxChar
}

console.log(maxChar('apple 12311111'));

//SPIRAL MATRIX

function matrix(n) {
    const result = []
    let counter=1, startRow=0, endRow=n-1, startCol=0, endCol=n-1
    for(let i=0; i<n; i++){
        result.push([])
    }



while (startRow<=endRow && startCol<=endCol) {
    //Top
for (let i =startCol; i <=endCol; i++) {
    result[startRow][i] = counter
    counter++
    
}
startRow++

//Right
for (let i =startRow; i <=endRow; i++) {
    result[i][endCol] = counter
    counter++
    
}
endCol--

//Bottom
for (let i =endCol; i >=startCol; i--) {
    result[endRow][i] = counter
    counter++
    
}
endRow--

//Left
for (let i =endRow; i >=startRow; i--) {
    result[i][startCol] = counter
    counter++
    
}
startCol++

}



    return result
}

console.log(matrix(6))


CHUNKING

function chunk(array , size){
    const result = []
    let index = 0
    while(index<array.length){
     result.push(array.slice(index,index+size))
     index += size
    }
   return result
}

console.log(chunk([1,2,3,4,5,6,7,8], 3))

CAPITALIZING

function capitalize (str){
    const words = str.split(' ')
    const result = []

for(let word of words){
    result.push(word[0].toUpperCase() + word.slice(1))
}

    return result.join(' ')

}
function capitalize(str){
    const words = str.split(' ')

    return words.map(word => word[0].toUpperCase() + word.slice(1)).join(' ')
}



console.log(capitalize('this is mukhtar from coding money'));

ANOGRAMS
SOL 1
function charMap(str){
   const charmap = {}

   str = str.toLowerCase().replace(/[\W]/g, '')
    for(char of str){
        charmap[char] = ++charmap[char] || 1
    }
    return charmap
}


function anograms(stringA, stringB) {
    const charmapA = charMap(stringA)
    
    const charmapB = charMap(stringB)
    
    if(Object.keys(charmapA).length !== Object.keys(charmapB).length) return false
    
    for(let key in charmapA){
        if(charmapA[key] !== charmapB[key]) return false
    }
    
     return true
    
    }
    
    
    console.log(anograms('RAIL! SAFETY!','fairy tales'))
SOL 2

 function cleanStr(str){
    return str.toLowerCase().replace(/[\W]/g,'').split('').sort().join('')
}

function anograms(stringA, stringB) {

    return cleanStr(stringA) === cleanStr(stringB)
}


console.log(anograms('RAIL! SAFETY!', 'fairy tales'));

COUNT VOWELS
SOL 1
function vowels (str) {
    const matches = str.match(/[aeiou]/gi)
    return matches ? matches.length : 0
}
SOL 2
function vowels(str){
    const vowelCheck = ['a', 'e', 'i', 'o', 'u']

    let count = 0

    for(let char of str.toLowerCase()){
       if(vowelCheck.includes(char)) count++
    }

    return count
}


console.log(vowels('Israel is awesome'));

FIZZ BUZZ
function fizzBuzz(n){
   for (let i=1; i<=n; i++){
    if(i % 3 === 0 && i % 5 === 0){
        console.log('fizzBuzz')
    }else if( i % 3 === 0){
        console.log('fizz')
    }else if( i % 5 === 0){
        console.log('buzz')
    }else{
        console.log(i)
    }
   }
}

fizzBuzz(20)

STEPS STRING PATTERN
function steps (n) {
    for(let row=1; row<=n; row++){
        let line = ''
        for(let col=1; col<=n; col++){
            line += '#'
            
        }
        console.log(line)
    }
}

steps(3)
function steps (n) {
    for(let row=1; row<=n; row++){
        let line = ''
        for(let col=1; col<=n; col++){
            if(col==row){
                line += '#'
            }else{
                line += ' '
            }
        }
        console.log(line)
    }
}

steps(3)

PYRAMID STRING PATTERN
function pyramid(n) {
    const mid = Math.floor((2*n-1)/2)
    for(let row=0; row<n; row++){
        let line = ''
        for(let col=0; col<2*n-1; col++){
            if(col >= mid - row && col <=mid + row){
                line += '#'
            }else{
                line += ' '
            }

        }
        console.log(line)
    }
}

pyramid(3)





**/
