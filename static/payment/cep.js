'use strict';

const autoCompleteForms = (address) => {
  document.getElementById("street").value = address.logradouro
  document.getElementById("district").value = address.bairro
  document.getElementById("state").value = address.uf
  
  
}


const getCepData = async() =>{
    const cep = document.getElementById('cep').value;
    const url = 'http://viacep.com.br/ws/'+ cep +'/json/'
    const data = await fetch(url)
    const address = await data.json();

    console.log(address)
    autoCompleteForms(address)
}


  document.getElementById('cep')
  .addEventListener('focusout', getCepData)

