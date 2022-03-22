'use strict';

const getCepData = async() =>{
    const cep = document.getElementById('postCode').value;
    const url = 'http://viacep.com.br/ws/'+ cep +'/json/'
    const data = await fetch(url)
    const address = await data.json();
   
    console.log(address)
}


  document.getElementById('postCode')
  .addEventListener('change', getCepData)

